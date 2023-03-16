---
title: "停止接收流数据"
weight: 20
---

If the user wishes to halt the streaming of a given project, they can utilize the following endpoint. It is important to note that if a simulation is currently in progress, it will be automatically terminated.

## Request

It is important to note that the user should only call this endpoint when the project's status is set to `STREAMING` or `SIMULATING`.

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/project/{project_id}/stream/stop` | `none` | Disable the stream of the project |

## Response

```json
{
    "message": "Project streaming stopped successfully",
    "project_id": 123
}
```
