---
title: "删除项目"
weight: 60
---

You can delete a project by using the enpoint introduced here.

## Request

If there is an ongoing stream operation, it will be stopped before the project is deleted.

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| DELETE | `/project/{project_id}` | `none` | Delete the project |

## Response

The response will be a `JSON` object.

After the deletion, the project and all the related data will be removed from the system.

```json
{
    "message": "Project deleted successfully",
    "project_id": 2
}
```
