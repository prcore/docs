---
title: "Clear Simulated Data"
weight: 30
---

After the simulation is stopped, you can clear the simulated data by calling the following endpoint.

## Request

You should only call this endpoint when the project's status is `TRAINED`, `STREAMING`, or `SIMULATING`.

If there is a simulation in progress, it will be stopped automatically.

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/project/{project_id}/simulate/clear` | `none` | Remove all simulated data and results |

## Response

```json
{
    "message": "Project simulation data cleared successfully",
    "project_id": 123
}
```
