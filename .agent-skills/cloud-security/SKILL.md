---
name: cloud-security
description: Cloud security best practices for AWS, GCP, and Azure. Use when securing cloud infrastructure, configuring IAM, hardening S3 buckets, setting up VPC security, compliance (SOC2, ISO 27001), or auditing cloud resources for misconfigurations.
metadata:
  tags:
  - security
  - cloud
  - aws
  - gcp
  - azure
  - compliance
  version: 1.0.0
---

# Cloud Security

Comprehensive cloud security guidance for AWS, GCP, and Azure. Covers IAM, network security, data protection, compliance, and automated security scanning.

> "Cloud security is a shared responsibility. Know your side of the shared model."

---

## 🎯 When to Use

- Securing cloud infrastructure (AWS/GCP/Azure)
- Configuring IAM policies and roles
- Hardening storage (S3, GCS, Blob)
- Setting up network security (VPC, NSG, firewall rules)
- Compliance preparation (SOC2, ISO 27001, PCI-DSS)
- Auditing cloud resources for misconfigurations
- Incident response in cloud environments

---

## ☁️ Shared Responsibility Model

```
┌─────────────────────────────────────────────────────────────┐
│                      CUSTOMER                               │
│  ├─ Data security & encryption                              │
│  ├─ Identity & access management                            │
│  ├─ Application security                                    │
│  ├─ OS, network, firewall configuration                     │
│  ├─ Client-side encryption                                  │
│  └─ Server-side encryption (customer-managed keys)          │
├─────────────────────────────────────────────────────────────┤
│                      CLOUD PROVIDER                         │
│  ├─ Physical infrastructure                                 │
│  ├─ Host OS & virtualization                                │
│  ├─ Network infrastructure                                  │
│  └─ Data center security                                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔐 AWS Security

### IAM Best Practices

```json
// Least privilege policy example
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::my-bucket/${aws:username}/*",
            "Condition": {
                "Bool": {
                    "aws:MultiFactorAuthPresent": "true"
                }
            }
        }
    ]
}
```

```bash
# IAM audit commands
aws iam list-users --output table
aws iam list-roles --output table
aws iam list-policies --scope Local --output table
aws iam get-account-authorization-details

# Check for unused credentials
aws iam generate-credential-report
aws iam get-credential-report --query 'Content' --output text | base64 -d | column -t -s,

# Find policies with wildcards
aws iam list-policies --scope Local | jq '.Policies[] | select(.Arn | contains("arn:aws:iam")) | .PolicyName'
```

### S3 Bucket Security

```bash
# Check bucket permissions
aws s3api get-bucket-acl --bucket my-bucket
aws s3api get-bucket-policy --bucket my-bucket
aws s3api get-public-access-block --bucket my-bucket

# Secure bucket configuration
aws s3api put-public-access-block \
    --bucket my-bucket \
    --public-access-block-configuration \
    "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"

# Enable encryption
aws s3api put-bucket-encryption \
    --bucket my-bucket \
    --server-side-encryption-configuration '{
        "Rules": [{
            "ApplyServerSideEncryptionByDefault": {
                "SSEAlgorithm": "aws:kms",
                "KMSMasterKeyID": "arn:aws:kms:region:account:key/key-id"
            },
            "BucketKeyEnabled": true
        }]
    }'

# Enable versioning and logging
aws s3api put-bucket-versioning --bucket my-bucket --versioning-configuration Status=Enabled
aws s3api put-bucket-logging --bucket my-bucket --bucket-logging-status '{
    "LoggingEnabled": {
        "TargetBucket": "my-logs-bucket",
        "TargetPrefix": "s3-access-logs/"
    }
}'
```

### VPC Security

```bash
# Security group audit
aws ec2 describe-security-groups --query 'SecurityGroups[?length(IpPermissions[?IpRanges[?CidrIp==`0.0.0.0/0`]]) > `0`].[GroupName,GroupId]'

# Remove overly permissive rules
aws ec2 revoke-security-group-ingress \
    --group-id sg-xxxxxxxx \
    --protocol tcp \
    --port 22 \
    --cidr 0.0.0.0/0

# VPC Flow Logs
aws ec2 create-flow-logs \
    --resource-type VPC \
    --resource-ids vpc-xxxxxxxx \
    --traffic-type ALL \
    --log-destination-type cloud-watch-logs \
    --log-group-name vpc-flow-logs \
    --deliver-logs-permission-arn arn:aws:iam::account:role/FlowLogsRole
```

### AWS Security Tools

```bash
# AWS Config for compliance monitoring
aws configservice put-config-rule \
    --config-rule '{
        "ConfigRuleName": "s3-bucket-public-read-prohibited",
        "Source": {
            "Owner": "AWS",
            "SourceIdentifier": "S3_BUCKET_PUBLIC_READ_PROHIBITED"
        }
    }'

# GuardDuty (threat detection)
aws guardduty create-detector --enable

# Security Hub (centralized security findings)
aws securityhub enable-import-findings-for-product --product-arn arn:aws:securityhub:region::product/aws/guardduty

# Inspector (vulnerability scanning)
aws inspector create-assessment-target --assessment-target-name production-target
```

---

## 🔐 GCP Security

### IAM & Access Control

```bash
# List IAM policies
gcloud projects get-iam-policy PROJECT_ID
gcloud resource-manager folders get-iam-policy FOLDER_ID
gcloud organizations get-iam-policy ORGANIZATION_ID

# Check for overly permissive bindings
gcloud projects get-iam-policy PROJECT_ID --format=json | jq '.bindings[] | select(.role=="roles/owner" or .role=="roles/editor")'

# Service account audit
gcloud iam service-accounts list
gcloud iam service-accounts keys list --iam-account=sa@project.iam.gserviceaccount.com
```

### Cloud Storage Security

```bash
# Check bucket IAM
gsutil iam get gs://my-bucket

# Enable uniform bucket-level access
gsutil uniformbucketlevelaccess set on gs://my-bucket

# Enable encryption
gsutil kms encryption -k projects/PROJECT/locations/LOCATION/keyRings/RING/cryptoKeys/KEY gs://my-bucket

# Enable access logging
gsutil logging set on -b gs://logs-bucket -o access_log/ gs://my-bucket
```

### VPC & Network Security

```bash
# Firewall rules audit
gcloud compute firewall-rules list --format='table(name,sourceRanges,allowed)'

# Check for overly permissive rules
gcloud compute firewall-rules list --filter="sourceRanges='0.0.0.0/0'"

# VPC Flow Logs
gcloud compute networks subnets update SUBNET \
    --region=REGION \
    --enable-flow-logs
```

### GCP Security Tools

```bash
# Security Command Center
# Enable in console or via gcloud

# Cloud Asset Inventory
gcloud asset list --content-type resource --asset-types="compute.googleapis.com/Instance"

# Policy Analyzer
gcloud asset analyze-iam-policy --organization=ORGANIZATION_ID
```

---

## 🔐 Azure Security

### RBAC & Access Control

```powershell
# List role assignments
Get-AzRoleAssignment | Where-Object { $_.Scope -eq "/subscriptions/$subscriptionId" }

# Check for Owner/Contributor roles
Get-AzRoleAssignment | Where-Object { $_.RoleDefinitionName -in @("Owner","Contributor") }

# Custom role with least privilege
$role = Get-AzRoleDefinition "Reader"
$role.Id = $null
$role.Name = "Custom VM Operator"
$role.Description = "Can start/stop VMs"
$role.Actions = @("Microsoft.Compute/virtualMachines/start/action", "Microsoft.Compute/virtualMachines/deallocate/action")
$role.NotActions = @()
$role.AssignableScopes = @("/subscriptions/$subscriptionId")
New-AzRoleDefinition -Role $role
```

### Storage Account Security

```powershell
# Enable secure transfer
Set-AzStorageAccount -Name mystorage -ResourceGroupName myrg -EnableHttpsTrafficOnly $true

# Enable encryption
Set-AzStorageAccount -Name mystorage -ResourceGroupName myrg -StorageEncryption

# Network rules
$rule = New-AzStorageAccountNetworkRuleSet -DefaultAction Deny
Add-AzStorageAccountNetworkRule -ResourceGroupName myrg -Name mystorage -VirtualNetworkResourceId $subnetId
```

### Network Security

```powershell
# NSG audit
Get-AzNetworkSecurityGroup | ForEach-Object { $_.SecurityRules | Where-Object { $_.SourceAddressPrefix -eq "*" } }

# Enable NSG flow logs
Set-AzNetworkWatcherConfigFlowLog -NetworkWatcher $nw -TargetResourceId $nsg.Id -StorageAccountId $storage.Id -EnableFlowLog $true
```

### Azure Security Tools

```powershell
# Azure Security Center (Defender for Cloud)
Set-AzSecurityPricing -Name "VirtualMachines" -PricingTier "Standard"

# Azure Policy for compliance
New-AzPolicyAssignment -Name "require-https-storage" -PolicyDefinition $policy -Scope "/subscriptions/$subscriptionId"

# Azure Sentinel (SIEM)
# Deploy via Azure Portal or ARM templates
```

---

## 🔍 Automated Security Scanning

### Cloud Security Posture Management (CSPM)

```bash
# Prowler (AWS)
prowler aws --category identity --severity critical
prowler aws --checks s3_bucket_public_read_acl

# ScoutSuite (AWS/GCP/Azure)
scout aws --report-dir ./scout-report
scout gcp --report-dir ./scout-report
scout azure --report-dir ./scout-report

# CloudSploit (AWS/GCP/Azure)
# Requires API keys, runs as SaaS or self-hosted

# Steampipe (AWS/GCP/Azure)
steampipe query "select * from aws_s3_bucket where block_public_acls = false"
steampipe check aws_compliance.benchmark.cis_v130
```

### Infrastructure as Code (IaC) Scanning

```bash
# Checkov
checkov -d ./terraform --framework terraform

# tfsec
tfsec ./terraform

# Terrascan
terrascan scan -i terraform -d ./terraform

# Semgrep for cloud configs
semgrep --config=auto --json ./terraform
```

---

## 📋 Compliance Mapping

### SOC 2 Controls

| Control | AWS | GCP | Azure |
|---------|-----|-----|-------|
| Access Control | IAM + MFA | IAM + 2FA | RBAC + MFA |
| Encryption | KMS + S3 SSE | CMEK + Cloud KMS | Key Vault |
| Monitoring | CloudTrail + Config | Cloud Audit Logs | Activity Log |
| Logging | CloudWatch + S3 | Cloud Logging | Log Analytics |

### CIS Benchmarks

```bash
# AWS CIS Benchmark
prowler aws --compliance cis_1.5_aws

# GCP CIS Benchmark
gcloud compute instances list --format=json | jq -r '.[] | .name'
# Use Forseti or CIS-CAT for automated scanning

# Azure CIS Benchmark
# Use Azure Policy built-in initiatives
```

---

## 🚨 Incident Response in Cloud

```
1. Detection
   ├─ CloudWatch/Cloud Logging alerts
   ├─ GuardDuty/Security Center findings
   └─ SIEM correlation rules

2. Containment
   ├─ Isolate compromised instances (security group rules)
   ├─ Revoke compromised credentials
   ├─ Disable compromised accounts
   └─ Snapshot affected resources for forensics

3. Eradication
   ├─ Patch vulnerabilities
   ├─ Rotate all potentially exposed secrets
   ├─ Rebuild compromised instances from clean images
   └─ Update IAM policies

4. Recovery
   ├─ Restore from clean backups
   ├─ Verify integrity of restored systems
   └─ Gradually restore access

5. Lessons Learned
   ├─ Update threat models
   ├─ Improve detection rules
   └─ Update runbooks
```

---

## 📚 References

- [AWS Security Best Practices](https://docs.aws.amazon.com/security/)
- [GCP Security Foundations](https://cloud.google.com/security)
- [Azure Security Documentation](https://docs.microsoft.com/en-us/azure/security/)
- [CIS Cloud Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [Cloud Security Alliance](https://cloudsecurityalliance.org/)
