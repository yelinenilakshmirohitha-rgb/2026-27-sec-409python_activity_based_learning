Here is the flowchart in a simple format that you can copy and draw in your assignment.

### Railway Fare Calculator – Flowchart

```mermaid

flowchart TD
    A([START]) --> B[/Enter Distance/]
    B --> C[/Enter Age/]
    C --> D[/Enter Class Choice/]
    D --> E{Choice = 1?}
    E -->|Yes| F[Fare = Distance * 1.5]
    E -->|No| G{Choice = 2?}
    G -->|Yes| H[Fare = Distance * 3]
    G -->|No| I[Display Invalid Class]
    F --> J{Fare > 0?}
    H --> J
    I --> K([STOP])
    J -->|No| K
    J -->|Yes| L{Age >= 60?}
    L -->|Yes| M[Fare = Fare * 0.90]
    L -->|No| N[No Concession]
    M --> O[Fare = Fare + 50]
    N --> O
    O --> P[/Display Final Fare/]
    P --> K
```

Flowchart symbols to use when drawing:

| Symbol        | Purpose               |
| ------------- | --------------------- |
| Oval          | Start / Stop          |
| Parallelogram | Input / Output        |
| Rectangle     | Calculation / Process |
| Diamond       | Decision              |

You can use this flowchart directly as a reference for drawing it neatly in your record book.
