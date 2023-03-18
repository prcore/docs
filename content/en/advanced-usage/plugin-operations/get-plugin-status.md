---
title: "Get Plugin Status"
weight: 50
---

You can get the status of a plugin after a project is trained. This can be useful to check if the plugin is trained successfully or not after you set the parameters or additional info of the plugin separately.

## Request

| Method | Endpoint | Request Body Type	 | Description |
| ------ | -------- | ----------------- | ----------- |
| GET | `/plugin/{plugin_id}` | `none` | Get the status of a plugin |

## Response

Exmaple response:

```json
{
    "message": "Plugin retrieved successfully",
    "plugin": {
        "id": 12,
        "created_at": "2023-03-17T09:28:54.940916+00:00",
        "updated_at": "2023-03-18T14:20:58.974405+00:00",
        "key": "plugin-causallift-resource-allocation",
        "prescription_type": "RESOURCE_ALLOCATION",
        "name": "CasualLift resource allocation",
        "description": "This plugin uses Uplift Modeling package CasualLift to get resource allocation base on CATE",
        "parameters": {
            "encoding": "BOOLEAN"
        },
        "additional_info": {
            "random": 10
        },
        "status": "TRAINED",
        "error": null,
        "disabled": true
    }
}
```
