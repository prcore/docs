---
title: "Start Streaming"
weight: 10
---

Before you start posting new data to the project, you need to firstly enable the streaming mode by calling the following endpoint. This can make sure all models are loaded and ready to receive new data.

## Request

You should only call this endpoint when the project's status is `TRAINED`.

{{< hint type=note icon=gdoc_info_outline >}}
Please note that the simulation and streaming modes are mutually exclusive. If you want to enable streaming mode, you should first stop the simulation by calling the [Stop Streaming]({{< relref "../../workflow/send-new-data/simulate-streaming/stop-streaming.md" >}}) endpoint. Vice verse.
{{< /hint >}}

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/project/{project_id}/stream/start` | `none` | Enable the stream mode |

## Response

```json
{
    "message": "Project streaming started successfully",
    "project_id": 42
}
```

After the streaming mode is enabled, you can start posting new data to the project by calling the [Stream Data]({{< relref "./stream-data.md" >}}) endpoint.

If you want to stop the streaming mode, you can call the [Stop Streaming]({{< relref "../../workflow/send-new-data/simulate-streaming/stop-streaming.md" >}}) endpoint.
