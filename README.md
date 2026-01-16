# bitsandbobs
Some of my code kept where I can find it


## test how mermaid graphs are rendered in github markdown

```mermaid
graph LR
    A[README.md]
    B{Find mermaid graphs<br>and image paths}
    C[[docker mermaid-cli]]
    D[[docker mermaid-cli]]
    E(Graph 1 png image)
    F(Graph 2 svg image)

    A -->|passed to| B
    subgraph render-md-mermaid.sh
      B --> |path/to/image1.png<br>+mermaid source| C
      B --> |path/to/image2.svg<br>+mermaid source| D
    end
    C --> E
    D --> F
```

## Attempting to render mermaid with new grouping

```mermaid
%%{init: {'theme':'forest'}}%%

sequenceDiagram
    box Gainsboro Alice & John
    participant A
    participant J
    end
    box Another Group
    participant B
    participant C
    end
    A->>J: Hello John, how are you?
    J->>A: Great!
    A->>B: Hello Bob, how is Charly?
    B->>C: Hello Charly, how are you?
```

## Mermaid with AWS icons

```mermaid
architecture-beta
    service dns(logos:aws-route53)[Route 53]
    service cf(logos:aws-cloudfront)[CloudFront]
    service lb(logos:aws-ec2)[Load Balancer]
    service ui(logos:nextjs)[UI]
    service gateway(logos:aws-api-gateway)[API Gateway]
    service auth(logos:aws-lambda)[Auth Service]
    service authDb(logos:aws-dynamodb)[Auth DB]
    auth:R --> L:authDb
    service blog(logos:aws-lambda)[Blog Service]
    service blogDb(logos:aws-dynamodb)[Blog DB]
    blog:R --> L:blogDb
    service analytics(logos:aws-lambda)[Analytics Service]
    service analyticsIndex(logos:aws-open-search)[OpenSearch]
    analytics:R --> L:analyticsIndex
    dns:R --> L:cf
    cf:R --> L:lb
    lb:B --> T:ui
    cf:R --> L:gateway
    gateway:R --> L:auth
    gateway:R --> L:blog
    gateway:R --> L:analytics
```

## Using links

```mermaid
flowchart TB

subgraph ACCOUNT[AWS Account]
  subgraph GRP1[" "]
    ELB@{ img: "https://api.iconify.design/logos/aws-elb.svg", label: "ELB", pos: "b", w: 60, h: 60, constraint: "on" }
  end
  subgraph GRP2[" "]
    EC2@{ img: "https://api.iconify.design/logos/aws-ec2.svg", label: "EC2", pos: "b", w: 60, h: 60, constraint: "on" }
  end
  subgraph GRP3[" "]
    RDS@{ img: "https://api.iconify.design/logos/aws-rds.svg", label: "RDS", pos: "b", w: 60, h: 60, constraint: "on" }
  end
  ELB --- EC2 --- RDS
end

classDef vpc fill:none,color:#0a0,stroke:#0a0
class ACCOUNT vpc

classDef group fill:none,stroke:none
class GRP1,GRP2,GRP3 group
```

