---
title: "Set Parameters"
weight: 20
---

You can set the parameters of a plugin in three ways.

## 1. Set when creating a project

You can set the parameters of a plugin when you are [creating a project]({{< relref "../../workflow/upload-event-log/project-creation.md" >}}).

As you can see in the request body properties, it accepts a field called `parameters`, which is a JSON object. The keys of this object are the plugin IDs, and the values are the parameters of the plugin, which is also a JSON object.

For example, when you create a project, if you want to set the parameters of the `plugin-knn-next-activity` plugin, you can set the `parameters` field as follows:

```json
{
    "event_log_id": 1,
    "positive_outcome": [
        [
            {
                "column": "DURATION",
                "operator": "LESS_THAN_OR_EQUAL",
                "value": "2 weeks"
            }
        ],
        [
            {
                "column": "REG_DATE",
                "operator": "EARLIER_THAN_OR_EQUAL",
                "value": "2023-03-07T20:50:00Z"
            }
        ]
    ],
    "treatment": [
        [
            {
                "column": "Resource",
                "operator": "EQUAL",
                "value": "112"
            }
        ]
    ],
    "parameters": {
        "plugin-knn-next-activity": {
            "n_neighbors": 5
        }
    }
}
```

You can check the default parameters of each plugin by using [Check Plugins]({{< relref "./check-plugins.md" >}}) API.

## 2. Set after a project is trained

You can change the parameters of plugins after a project is trained. You can do this by using the method introduced in [Change Outcome And Treatment Definition]({{< relref "../project-operations/change-outcome-treatment-definition.md" >}}) while recreating the project.

## 3. Set the parameters of a plugin separately

After the project is trained, you can also only change the parameters of a specific plugin.

### Request

| Method | Endpoint | Request Body Type	 | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/plugin/{plugin_id}` | `json` | Update the settings of a plugin |

Request body example:

```json
{
    "parameters": {
        "encoding": "BOOLEAN"
    }
}
```

### Response

After the parameters are updated, the plugin will be retrained.

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
        "parameters": {
            "encoding": "BOOLEAN"
        },
        "status": "TRAINING",
        "error": null,
        "disabled": false
    }
}
```

### Note

At the same time, with the same endpoint, you can also change the `additional_info` of the plugin. Please refer to [Update Additional Info]({{< relref "./update-additional-info.md" >}}) section.
