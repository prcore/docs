---
title: "Prescribe stream"
weight: 20
---

There are two steps in the prescribing workflow. The first step is to activate the project, and the second step is streaming and receiving the results.

## Project activation

If the project is ready, the external user can activiate the project to start the prescribing workflow. The meaning of the activation is that in some cases, the plugin may need to load the model file into the memory, especially after the system restarts. This also can help the system to save resources.

They are two ways to trigger the prescribing workflow. One is to start the simulation, the other is to start the normal streaming.

The simulation is used to test the project. The core will send a request to the plugin to start the preparation.

{{< mermaid class="text-center" >}}
sequenceDiagram
    Consumer-)Core: Start simulation or turn on streaming mode through API
    Core->>Plugin: STREAMING_PREPARE
    Plugin-->>Core: STREAMING_READY
{{< /mermaid >}}

### STREAMING_PREPARE

The core will send this request to the plugin to start the preparation. Before the core receives the response, the plugin's status will be set to `ACTIVATING`.

```json
{
    "project_id": 123,
    "model_name": "random-string.pkl",
    "additional_info": {}
}
```

### STREAMING_READY

After the plugin loads the model file into the memory, it will send this message to the core to tell the core that it is ready to start the simulation or streaming. Core will then mark the plugin as `STREAMING` status. 

If all plugins are in `STREAMING` status, the core will mark the project as `STREAMING` or `SIMULATING` status.

```json
{
    "project_id": 123,
    "plugin_id": 345
}
```

## Streaming and receiving results

If you are under the simulation mode, you don't need to send any request to the core. The core will trigger its simulation script to send the simulation data to the plugin. The plugin will process the data and send the results back to the core.

If you are under the normal streaming mode, you need to send the streaming data to the core using the HTTP API. The core will forward the data to the plugin. The plugin will process the data and send the results back to the core.

{{< mermaid class="text-center" >}}
sequenceDiagram
    loop
        Core->>Plugin: STREAMING_PRESCRIPTION_REQUEST
        Plugin-->>Core: STREAMING_PRESCRIPTION_RESULT
    end
{{< /mermaid >}}

### STREAMING_PRESCRIPTION_REQUEST

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
    ],
    "additional_info": {}
}
```

The `model_name` is still sent to the plugin, because the plugin may need to load the model file into the memory if the system restarts.

### STREAMING_PRESCRIPTION_RESULT

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

## Stop the streaming or simulation

External users can stop the streaming or simulation by sending a request to the core. The core will send a request to the plugin to release the resources.

{{< mermaid class="text-center" >}}
sequenceDiagram
    Consumer-)Core: Stop simulation or turn off streaming mode through API
    Core-)Plugin: STREAMING_STOP
{{< /mermaid >}}

### STREAMING_STOP

After the core send this, all statues will be set to `TRAINED` status.

When plugin receives this request, it will release the resources.

```json
{
    "project_id": 123
}
```
