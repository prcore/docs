---
title: "流程图"
weight: 10
---

The first stage involves uploading the event log file, which should contain only completed cases, and defining the columns and project parameters. This stage also includes parsing the log file and checking for its validity. If the log file is valid, basic information is returned to the user, while an invalid file results in the end of the process.

The second stage of the process is preprocessing and training. After defining the columns and project parameters, the system preprocesses the data according to the definitions provided. The outcome and treatment definitions are also defined in this stage, which the system uses to train the models. The system validates the project definition and checks if it is valid or not. If the definition is valid, the models are trained; otherwise, the process ends.

The third stage of the process involves sending new data to the system. Users can either upload a new dataset or stream new events data to obtain prescriptions for ongoing cases. If users choose to upload a new dataset, the system validates the dataset and prepares it for processing. If the dataset is valid, the system provides prescriptions for valid cases; otherwise, the process ends. Alternatively, if users choose to stream new events data to the system, the system validates the data and saves it to the database. If the data is valid, the system provides prescriptions for valid cases; otherwise, the process ends.

Finally, in the fourth stage, the system returns the prescriptions to the user. The user can then use these prescriptions to improve their processes.

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
    Train --> NewDataset[/Receive new dataset/]
    NewDataset --> Prepare[Prepare dataset]
    Prepare --> IsValidDataset{Valid dataset?}
    IsValidDataset --> |Valid dataset| Prescribe[Prescribe cases]
    IsValidDataset --> |Invalid dataset| End
    Prescribe --> Result[/Return prescriptions/]
    Result --> End
    Train --> Streaming[/Receive streaming data/]
    Streaming --> Check[Check streaming data]
    Check --> IsValidData{Valid data?}
    IsValidData --> |Valid data| SaveToDB[Save to database]
    IsValidData --> |Invalid data| End
    SaveToDB --> PrescribeStreaming[Prescribe streaming data]
    PrescribeStreaming --> ResultStream[/Return prescriptions stream/]
    ResultStream --> End
{{< /mermaid >}}

Throughout the entire workflow, the system validates the data and definitions provided by the user to ensure the quality and accuracy of the results.
