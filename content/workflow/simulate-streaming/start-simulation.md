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

## Note

After the simulation is started, you can subscribe to the prescription results by calling the endpoint introduced in [Get Prescriptions](/workflow/get-prescriptions/)

The simulation can be stopped automatically when:

1. All simulation data is consumed
2. The results have not been consumed for 5 minutes
3. The reading connection is closed, so if the getting prescriptions calling is interrupted, the simulation will be stopped automatically
