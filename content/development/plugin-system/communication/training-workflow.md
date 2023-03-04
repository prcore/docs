---
title: "Training workflow"
weight: 20
---

The core will send a request to the plugin to start the training workflow. This phase will be divided into several steps.

## Dataset sharing

When a new project is created, firstly the core will start preprocessing of the dataset in the background. When the preprocessing is done, the core will send a request to the plugin to share the dataset with the plugin. The plugin will respond with the dataset, to tell the core that if the plugin is applicable for the dataset. During this phase, the core project will be in `PREPROCESSING` status.

{{< mermaid class="text-center" >}}
sequenceDiagram
    VisualPM->>Core: Create project through API
    Core-->>VisualPM: Project created
    Core->>Plugin: TRAINING_DATA
    Plugin-->>Core: DATA_REPORT
{{< /mermaid >}}

### TRAINING_DATA

The core will share the dataset information in the following format:

```json
{
    "project_id": 123,
    "plugin_id": 345,
    "training_df_name": "radom-string"
}
```

### DATA_REPORT

After the plugin receives the dataset, it will process the dataset and return the result to the core. The result will be in the following format:

```json
{
    "project_id": 123,
    "plugin_id": 345,
    "applicable": true
}
```

Then the core application will add the plugin to the project, and mark the plugin as `PREPROCESSING` status.


## Training phase

In this phase, the core will not send any request to the plugin (except for the `ONLINE_INQUIRY` request). The plugin will start the training phase, and report the progress to the core.

{{< mermaid class="text-center" >}}
sequenceDiagram
    Plugin-)Core: TRAINING_START
    Plugin-)Core: MODEL_NAME
{{< /mermaid >}}

### TRAINING_START

When the plugin preprocessing is done, it will tell the core that it has started the training phase. The core will then mark the plugin as `TRAINING` status. If all plugins are in `TRAINING` status, the core will mark the project as `TRAINING` status.

```json
{
    "project_id": 123,
    "plugin_id": 345
}
```

### MODEL_NAME

When the plugin training is done, it will tell the core the name of the model file. The core will then mark the plugin as `TRAINED` status. If all plugins are in `TRAINED` status, the core will mark the project as `TRAINED` status, which indicates that the project is ready to be used.

```json
{
    "project_id": 123,
    "plugin_id": 345,
    "model_name": "random-string.pkl"
}
```
