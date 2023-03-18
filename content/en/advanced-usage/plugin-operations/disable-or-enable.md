---
title: "Disable or Enable"
weight: 40
---

You can disable or enable a plugin after a project is trained. The disabled plugin will not be used in the prediction process. Please note that this operation will only available if the project is in the `TRAINED` status.

## Disable request

| Method | Endpoint | Request Body Type	 | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/plugin/{plugin_id}/disable` | `none` | Disable a plugin |

## Enable request

| Method | Endpoint | Request Body Type	 | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/plugin/{plugin_id}/enable` | `none` | Enable a plugin |

## Response

After the plugin is disabled or enabled, you will get the response as follows:

```json
{
    "message": "Plugin is disabled successfully",
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