---
title: "Prescribe dataset"
weight: 10
---

If the user has uploaded a test dataset which only contains ongoing cases, this workflow is triggered.

{{< mermaid class="text-center" >}}
sequenceDiagram
    Consumer-)Core: Upload test dataset
    Core->>Plugin: DATASET_PRESCRIPTION_REQUEST
    Plugin-->>Core: DATASET_PRESCRIPTION_RESULT
{{< /mermaid >}}


### DATASET_PRESCRIPTION_REQUEST

The core will send uploaded dataset to plugin. The data will be in the following format:

```json
{
    "project_id": 123,
    "result_key": "random-string",
    "model_name": "random-string.pkl",
    "ongoing_df_name": "random-string",
    "additional_info": {}
```

The `model_name` is still sent to the plugin, because the plugin may need to load the model file into the memory if the system restarts.

### DATASET_PRESCRIPTION_RESULT

The plugin will process the data and send the results back to the core. The results will be in the following format:

```json
{
    "project_id": 123,
    "plugin_key": "plugin-1",
    "result_key": "random-string",
    "data": {
        "CASE_ID_1": {
            "datetime": "2023-01-01 00:02:00",
            "type": "NEXT_ACTIVITY",
            "output": "ACTIVITY_4",
            "plugin": {
                "name": "plugin_1",
                "model": 3,
                "accuracy": 0.7,
                "precision": 0.7,
                "recall": 0.7,
                "precision": 0.7
            }
        },
        "CASE_ID_2": {
            "datetime": "2023-01-01 00:02:00",
            "type": "NEXT_ACTIVITY",
            "output": "ACTIVITY_4",
            "plugin": {
                "name": "plugin_1",
                "model": 3,
                "accuracy": 0.7,
                "precision": 0.7,
                "recall": 0.7,
                "precision": 0.7
            }
        }
    }
}
```
