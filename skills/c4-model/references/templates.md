# C4 Model Templates

This file provides basic code templates for Mermaid and Structurizr DSL to quickly start drawing C4 diagrams.

## 1. Mermaid C4 Templates

### Level 1: System Context
```mermaid
C4Context
    title System Context Diagram for [System Name]
    
    Person(customer, "Customer", "A brief description of their role.")
    System(mySystem, "System Name", "The system you are developing.")
    System_Ext(externalSystem, "External System", "e.g., Bank, Email provider.")

    Rel(customer, mySystem, "Uses", "HTTPS/Web")
    Rel(mySystem, externalSystem, "Sends requests to", "REST API")
```

### Level 2: Container
```mermaid
C4Container
    title Container Diagram for [System Name]

    Person(customer, "Customer", "The user of the system")
    
    System_Boundary(c1, "System Name") {
        Container(web_app, "Web App", "React/TS", "User interface")
        Container(api, "API Application", "NodeJS/Go/Java", "Main business logic processing")
        ContainerDb(db, "Database", "PostgreSQL/MongoDB", "Data storage")
    }

    Rel(customer, web_app, "Uses", "HTTPS")
    Rel(web_app, api, "Calls API", "JSON/HTTPS")
    Rel(api, db, "Reads/Writes data", "JDBC/TCP")
```

### Level 3: Component
```mermaid
C4Component
    title Component Diagram for [Container Name]

    Container(spa, "Single Page App", "React", "Provides user interface")
    
    Container_Boundary(api, "API Application") {
        Component(sign_in_controller, "Sign-in Controller", "REST Controller", "Allows users to sign in")
        Component(security_service, "Security Service", "Service", "Access control checks")
        Component(user_repository, "User Repository", "Repository", "User data access")
    }

    Rel(spa, sign_in_controller, "Sends sign-in info", "JSON/HTTPS")
    Rel(sign_in_controller, security_service, "Authentication request", "Internal call")
    Rel(security_service, user_repository, "Fetches info", "Internal call")
```

## 2. Structurizr DSL Templates

```structurizr
workspace {
    model {
        customer = person "Customer" "User description"
        softwareSystem = softwareSystem "System Name" "System description" {
            webApp = container "Web App" "Provides user interface" "React"
            apiApp = container "API Application" "Provides API for Web App" "NodeJS"
            database = container "Database" "Stores user data" "PostgreSQL" "Database"
            
            webApp -> apiApp "Sends requests" "JSON/HTTPS"
            apiApp -> database "Reads/Writes data" "SQL/TCP"
        }
        
        externalSystem = softwareSystem "External System" "e.g., Bank API"

        customer -> softwareSystem "Uses"
        customer -> webApp "Accesses" "HTTPS"
        softwareSystem -> externalSystem "Sends info" "HTTPS"
    }

    views {
        systemContext softwareSystem "SystemContext" {
            include *
            autoLayout
        }
        
        container softwareSystem "Containers" {
            include *
            autoLayout
        }

        theme default
    }
}
```
