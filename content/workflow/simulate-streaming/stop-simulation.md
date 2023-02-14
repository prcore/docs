---
title: "Stop Simulation"
weight: 20
---

The simulation can be stopped automatically when all simulation data is consumed, or manually by calling the following endpoint.

## Request

You should only call this endpoint when the project's status is `TRAINED`.

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/project/{project_id}/simulate/stop` | `none` | Start the simulation of the project |

## Response

```json
{
    "message": "Project simulation stopped successfully",
    "project_id": 123
}
```
