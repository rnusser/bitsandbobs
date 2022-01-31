# bitsandbobs
Some of my code kept where I can find it


![mermaid flowchart](diagrams/flow1.png)
<details>
  <summary>diagram source</summary>
```mermaid
sequenceDiagram
    participant John
    
    Alice ->>+ John: Hello John, how are you?
    Alice ->>+ John: John, can you hear me?
    John -->>- Alice: Hi Alice, I can hear you!
    John-->>-Alice: I feel great!
            
```
</details>



![rendered image description](diagrams/diag.png)

<details>
  <summary>diagram source</summary>
  This details block is collapsed by default when viewed in GitHub. This hides the mermaid graph definition, while the rendered image
  linked above is shown. The details tag has to follow the image tag. (newlines allowed)

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
</details>


