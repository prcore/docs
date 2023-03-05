---
title: "Start Simulation"
weight: 10
---

If the user prefers to manually stream data to PrCore or utilize a program to do so, they may consult the [Stream Data](/workflow/send-new-data/) section. Alternatively, if the user wishes to test the streaming feature prior to conducting any manual streaming, they may utilize the following endpoint to simulate streaming data.

## Request

You should only call this endpoint when the project's status is `TRAINED`.

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/project/{project_id}/stream/start/simulating` | `none` | Start the simulation of the project |

## Response

```json
{
    "message": "Project simulation started successfully",
    "project_id": 123
}
```

## Tips

To retrieve the results of the simulation, users can subscribe to the prescription results by calling the endpoint introduced in the [Get Streaming Result](/workflow/get-prescriptions/get-streaming-result/) section.

It should be noted that the simulation will come to a stop under the following conditions:

1. All simulation data has been consumed.
2. Results have not been consumed within a 5-minute window.
3. If the reading result connection is closed, the simulation will be stopped in 1 minute. However, if the connection is re-established within this timeframe, the simulation will continue uninterrupted.
4. The simulation is stopped by calling the [Stop Streaming](/workflow/send-new-data/simulate-streaming/stop-streaming/) endpoint.
