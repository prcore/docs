---
title: "Workflow"
icon: "⚙️"
weight: -15
---

This section describes the workflow of using the PrCore API.

Below is a flowchart of the workflow. The workflow can be divided into 3 main parts: uploading and defining the log file, preprocessing and training, and prescribing the case.

{{< mermaid class="text-center" >}}
flowchart TB
    Start([Start]) --> Upload[/Receive log file/]
    Upload --> Parse[Parse file]
    Parse --> IsValidFile{Valid file?}
    IsValidFile --> |Valid file| Brief[/Return basic info/]
    IsValidFile --> |Invalid file| End([End])
    Brief --> ColumnsDefintion[/Receive columns definition/]
    ColumnsDefintion --> Analyze[Analyze file]
    Analyze --> IsValidColumnsDefinition{Valid definition?}
    IsValidColumnsDefinition --> |Valid definition| AnalyzeResult[/Return analysis and options/]
    IsValidColumnsDefinition --> |Invalid definition| End
    AnalyzeResult --> ProjectDefintion[/Receive outcome & treatment definition/]
    ProjectDefintion --> Preprocess[Preprocess by definition]
    Preprocess --> IsValidProjectDefinition{Valid definition?}
    IsValidProjectDefinition --> |Valid definition| Train[Train models]
    IsValidProjectDefinition --> |Invalid definition| End
    Train --> Streaming[/Receive streaming data/]
    Streaming --> Prescribe[Prescribe the case]
    Prescribe --> Result[/Return prescriptions/]
    Result --> End
{{< /mermaid >}}

Please refer to the following sections for more details:

{{< toc-tree >}}
