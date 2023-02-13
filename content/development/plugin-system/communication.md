---
title: "Communication"
weight: 10
---

This section will describe how is the communication between the core and the plugins.

All communication between the core and the plugins is done via the RabbitMQ message broker.

## Online status update

The core will send a request to the plugin to update the online status of the plugin. The plugin will respond with the updated status.

{{< mermaid class="text-center" >}}
sequenceDiagram
    loop Every 5 mintues
        Core->>Plugin: ONLINE_INQUIRY
        Plugin-->>Core: ONLINE_REPORT
    end
{{< /mermaid >}}

### ONLINE_INQUIRY

The core will send this request when it starts, and periodically. The request data's body is empty.

```
{}
```

### ONLINE_REPORT

The plugin will send the basic information of the plugin, such as the name, type, and description. For example:

```json
{
    "id": "example-plugin",
    "name": "Example Plugin",
    "type": "EXAMPLE",
    "description": "This is an example plugin",
    "parameters": {
        "param1": "value1",
        "param2": "value2"
    }
}
```

## Training workflow

The core will send a request to the plugin to start the training workflow. This phase will be divided into several steps.

### Dataset sharing

When a new project is created, firstly the core will start preprocessing of the dataset in the background. When the preprocessing is done, the core will send a request to the plugin to share the dataset with the plugin. The plugin will respond with the dataset, to tell the core that if the plugin is applicable for the dataset. During this phase, the core project will be in `PREPROCESSING` status.

{{< mermaid class="text-center" >}}
sequenceDiagram
    VisualPM->>Core: Create project through API
    Core-->>VisualPM: Project created
    Core->>Plugin: TRAINING_DATA
    Plugin-->>Core: DATA_REPORT
{{< /mermaid >}}

#### TRAINING_DATA

The core will share the dataset information in the following format:

```json
{
    "project_id": 123,
    "plugin_id": 345,
    "training_df_name": "radom-string.pkl"
}
```

#### DATA_REPORT

After the plugin receives the dataset, it will process the dataset and return the result to the core. The result will be in the following format:

```json
{
    "project_id": 123,
    "plugin_id": 345,
    "applicable": true
}
```

Then the core application will add the plugin to the project, and mark the plugin as `PREPROCESSING` status.


### Training phase

In this phase, the core will not send any request to the plugin (except for the `ONLINE_INQUIRY` request). The plugin will start the training phase, and report the progress to the core.

{{< mermaid class="text-center" >}}
sequenceDiagram
    Plugin-)Core: TRAINING_START
    Plugin-)Core: MODEL_NAME
{{< /mermaid >}}

#### TRAINING_START

When the plugin preprocessing is done, it will tell the core that it has started the training phase. The core will then mark the plugin as `TRAINING` status. If all plugins are in `TRAINING` status, the core will mark the project as `TRAINING` status.

```json
{
    "project_id": 123,
    "plugin_id": 345
}
```

#### MODEL_NAME

When the plugin training is done, it will tell the core the name of the model file. The core will then mark the plugin as `TRAINED` status. If all plugins are in `TRAINED` status, the core will mark the project as `TRAINED` status, which indicates that the project is ready to be used.

```json
{
    "project_id": 123,
    "plugin_id": 345,
    "model_name": "random-string.pkl"
}
```

## Prescribing workflow

There are two steps in the prescribing workflow. The first step is to activate the project, and the second step is streaming and receiving the results.

### Project activation

If the project is ready, the external user can activiate the project to start the prescribing workflow. The meaning of the activation is that in some cases, the plugin may need to load the model file into the memory, especially after the system restarts. This also can help the system to save resources.

They are two ways to trigger the prescribing workflow. One is to start the simulation, the other is to start the normal streaming.

The simulation is used to test the project. The core will send a request to the plugin to start the preparation.

{{< mermaid class="text-center" >}}
sequenceDiagram
    VisualPM-)Core: Start simulation or turn on streaming mode through API
    Core->>Plugin: STREAMING_PREPARE
    Plugin-->>Core: STREAMING_READY
{{< /mermaid >}}

#### STREAMING_PREPARE

The core will send this request to the plugin to start the preparation. Before the core receives the response, the plugin's status will be set to `ACTIVATING`.

```json
{
    "project_id": 123,
    "model_name": "random-string.pkl"
}
```

#### STREAMING_READY

After the plugin loads the model file into the memory, it will send this message to the core to tell the core that it is ready to start the simulation or streaming. Core will then mark the plugin as `STREAMING` status. 

If all plugins are in `STREAMING` status, the core will mark the project as `STREAMING` or `SIMULATING` status.

```json
{
    "project_id": 123,
    "plugin_id": 345
}
```

### Streaming and receiving results

If you are under the simulation mode, you don't need to send any request to the core. The core will trigger its simulation script to send the simulation data to the plugin. The plugin will process the data and send the results back to the core.

If you are under the normal streaming mode, you need to send the streaming data to the core using the HTTP API. The core will forward the data to the plugin. The plugin will process the data and send the results back to the core.

{{< mermaid class="text-center" >}}
sequenceDiagram
    loop
        Core->>Plugin: PRESCRIPTION_REQUEST
        Plugin-->>Core: PRESCRIPTION_RESULT
    end
{{< /mermaid >}}

#### PRESCRIPTION_REQUEST

The core will send the streaming data to the plugin. The data will be in the following format:

```json
{
    "project_id": 123,
    "model_name": "random-string.pkl",
    "event_id": 123,
    "data": [
        {
            "CASE_ID": "123",
            "ACTIVITY": "ACTIVITY_1",
            "TIMESTAMP": "2023-01-01 00:00:10"
        },
        {
            "CASE_ID": "123",
            "ACTIVITY": "ACTIVITY_2",
            "TIMESTAMP": "2023-01-01 00:00:20"
        },
        {
            "CASE_ID": "123",
            "ACTIVITY": "ACTIVITY_3",
            "TIMESTAMP": "2023-01-01 00:01:00"
        }
    ]
}
```

The `model_name` is still sent to the plugin, because the plugin may need to load the model file into the memory if the system restarts.

#### PRESCRIPTION_RESULT

The plugin will process the data and send the results back to the core. The results will be in the following format:

```json
{
    "project_id": 123,
    "plugin_key": "plugin-1",
    "event_id": 123,
    "data": {
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
```

Based on the different plugins, the `model` field may be different. For example, the `model` field may be the name of the model file, or the length of the prefix during the training phase of that specific model.

### Stop the streaming or simulation

External users can stop the streaming or simulation by sending a request to the core. The core will send a request to the plugin to release the resources.

{{< mermaid class="text-center" >}}
sequenceDiagram
    VisualPM-)Core: Stop simulation or turn off streaming mode through API
    Core-)Plugin: STREAMING_STOP
{{< /mermaid >}}

#### STREAMING_STOP

After the core send this, all statues will be set to `TRAINED` status.

```json
{
    "project_id": 123
}
```

## Error reporting

If the plugin encounters an error, it will send the error message to the core. The core will then mark the plugin's status as the error message. If all plugins are in the error status, the core will mark the project as the error status.

{{< mermaid class="text-center" >}}
sequenceDiagram
    Plugin-)Core: ERROR_REPORT
{{< /mermaid >}}

### ERROR_REPORT

The error message will include the detail field.

```json
{
    "project_id": 123,
    "plugin_id": 345,
    "detail": "error message"
}
```
