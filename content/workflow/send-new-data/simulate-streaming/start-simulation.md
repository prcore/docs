---
title: "Start Simulation"
weight: 10
---

PrCore provides endpoints to automatically activate the project, and simulate streaming data to the project.

## Request

You should only call this endpoint when the project's status is `TRAINED`  or `STREAMING`.

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/project/{project_id}/simulate/start` | `none` | Stop the simulation of the project |

## Response

```json
{
    "message": "Project simulation started successfully",
    "project_id": 123
}
```

## Tips

After the simulation is started, you can subscribe to the prescription results by calling the endpoint introduced in [Get Prescriptions](/workflow/get-prescriptions/) section.

The simulation will be stopped when:

1. All simulation data is consumed.
2. The results have not been consumed for 5 minutes.
3. If the reading result connection is closed, the simulation will be stopped in 1 minute. If the connection is re-established in the timeframe, the simulation will not be interrupted.
4. The simulation is stopped by calling the [Stop Simulation](/workflow/send-new-data/simulate-streaming/stop-simulation/) endpoint.
