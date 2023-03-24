---
title: "Update Additional Info"
weight: 30
---

You can set the additional info of a plugin in three ways.

## 1. Set when creating a project

You can set the additional info of a plugin when you are [creating a project]({{< relref "../../workflow/upload-event-log/project-creation.md" >}}).

As you can see in the request body properties, it accepts a field called `additional_info`, which is a JSON object. The keys of this object are the plugin IDs, and the values are the additional info of the plugin, which is also a JSON object.

For example, when you create a project, if you want to set the additional_info of the `plugin-causallift-resource-allocation` plugin, you can set the `additional_info` field as follows:

```json
{
    "event_log_id": 1,
    "positive_outcome": [
        [
            {
                "column": "Activity",
                "operator": "EQUAL",
                "value": "A_APPROVED"
            }
        ]
    ],
    "treatment": [
        [
            {
                "column": "Activity",
                "operator": "EQUAL",
                "value": "O_SENT_BACK"
            }
        ]
    ],
    "additional_info": {
        "plugin-causallift-resource-allocation":{
            "available_resources":[
                "Resource_A",
                "Resource_B",
                "Resource_C"
            ],
            "treatment_duration":"1h"
        }
    }
}
```

## 2. Set after a project is trained

You can change the additional_info of plugins after a project is trained. You can do this by using the method introduced in [Change Outcome And Treatment Definition]({{< relref "../project-operations/change-outcome-treatment-definition.md" >}}) while redefining the project.

## 3. Set the additional info of a plugin separately

After the project is trained, you can also only change the additional info of a specific plugin.

### Request

| Method | Endpoint | Request Body Type	 | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/plugin/{plugin_id}` | `json` | Update the settings of a plugin |

Request body example:

```json
{
    "additional_info": {
        "random": 10
    }
}
```

### Response

After the `additional_info` are updated, if necessary, the plugin will be retrained. It depends on whether the plugin needs the information your newly provided to train the model.

```json
{
    "message": "Plugin is updated successfully",
    "plugin": {
        "id": 12,
        "created_at": "2023-03-17T09:28:54.940916+00:00",
        "updated_at": "2023-03-18T14:06:10.934765+00:00",
        "key": "plugin-causallift-resource-allocation",
        "prescription_type": "RESOURCE_ALLOCATION",
        "name": "CasualLift resource allocation",
        "description": "This plugin uses Uplift Modeling package CasualLift to get resource allocation base on CATE",
        "additional_info": {
            "random": 10
        },
        "status": "TRAINED",
        "error": null,
        "disabled": false
    }
}
```

### Note

At the same time, with the same endpoint, you can also change the `parameters` of the plugin. Please refer to [Set Parameters]({{< relref "./set-parameters.md" >}}) section.
