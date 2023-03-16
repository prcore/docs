---
title: "清除流数据"
weight: 30
---

In the event that the user wishes to remove all streamed data and results from a project, they can do so by calling the following endpoint.

## Request

You should only call this endpoint when the project's status is `TRAINED`, `STREAMING`, or `SIMULATING`.

If there is a streaming or simulation in progress, it will be stopped automatically.

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/project/{project_id}/stream/clear` | `none` | Remove all streamed data and results |

## Response

```json
{
    "message": "Project streamed data cleared successfully",
    "project_id": 123
}
```
