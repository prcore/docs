---
title: "Workflow"
weight: -15
---

This section describes the workflow of using the PrCore API.

{{< mermaid class="text-center" >}}
graph TB
    Start([Start]) --> Upload[/Receive log file/]
    Upload --> Parse[Parse file]
    Parse --> IsValidFile[/Is valid file?/]
    IsValidFile --> |Valid file| Brief[/Return basic info/]
    IsValidFile --> |Invalid file| End([End])
    Brief --> ColumnsDefintion[/Receive columns definition/]
    ColumnsDefintion --> Analyze[Analyze file]
    Analyze --> IsValidColumnsDefinition[/Is valid definition?/]
    IsValidColumnsDefinition --> |Valid definition| AnalyzeResult[/Return analysis and options/]
    IsValidColumnsDefinition --> |Invalid definition| End
    AnalyzeResult --> ProjectDefintion[/Receive outcome & treatment definition/]
    ProjectDefintion --> Preprocess{Preprocess}
    Preprocess --> |Valid definition| Train[Train models]
    Preprocess --> |Invalid definition| End
    Train --> Streaming[/Receive streaming data/]
    Streaming --> Prescribe[Prescribe the case]
    Prescribe --> Result[/Return prescriptions/]
    Result --> End
{{< /mermaid >}}

{{< toc-tree >}}
