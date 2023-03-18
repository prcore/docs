---
title: "Check Plugins"
weight: 10
---

You can get the plugins that are currently online in PrCore, as well as some basic information about them.

## Request

| Method | Endpoint | Request Body Type	 | Description |
| ------ | -------- | ----------------- | ----------- |
| GET | `/plugin/available` | `none` | Check all available plugins |

## Response

You will get a response similar to the following:

```json
{
    "message": "Available plugins retrieved successfully",
    "plugins": {
        "plugin-knn-next-activity": {
            "prescription_type": "NEXT_ACTIVITY",
            "name": "KNN next activity prediction",
            "description": "This plugin predicts the next activity based on the KNN algorithm.",
            "parameters": {
                "encoding": "SIMPLE_INDEX",
                "n_neighbors": 3
            },
            "needed_columns": [],
            "needed_info_for_training": [],
            "needed_info_for_prediction": [],
            "supported_encoding": [
                "BOOLEAN",
                "FREQUENCY_BASED",
                "SIMPLE_INDEX"
            ],
            "online": "2023-03-18T15:35:38.171211"
        },
        "plugin-random-forest-alarm": {
            "prescription_type": "ALARM",
            "name": "Random forest negative outcome probability",
            "description": "This plugin predicts the alarm probability based on the random forest algorithm.",
            "parameters": {
                "encoding": "SIMPLE_INDEX"
            },
            "needed_columns": [
                "OUTCOME"
            ],
            "needed_info_for_training": [],
            "needed_info_for_prediction": [],
            "supported_encoding": [
                "BOOLEAN",
                "FREQUENCY_BASED",
                "SIMPLE_INDEX"
            ],
            "online": "2023-03-18T15:35:38.271808"
        },
        "plugin-causallift-treatment-effect": {
            "prescription_type": "TREATMENT_EFFECT",
            "name": "CasualLift treatment effect",
            "description": "This plugin uses Uplift Modeling package CasualLift to get the CATE and probability of outcome if treatment is applied or not",
            "parameters": {
                "encoding": "SIMPLE_INDEX"
            },
            "needed_columns": [
                "OUTCOME",
                "TREATMENT"
            ],
            "needed_info_for_training": [],
            "needed_info_for_prediction": [
                "treatment_definition"
            ],
            "supported_encoding": [
                "BOOLEAN",
                "FREQUENCY_BASED",
                "SIMPLE_INDEX"
            ],
            "online": "2023-03-18T15:35:38.372398"
        },
        "plugin-causallift-resource-allocation": {
            "prescription_type": "RESOURCE_ALLOCATION",
            "name": "CasualLift resource allocation",
            "description": "This plugin uses Uplift Modeling package CasualLift to get resource allocation base on CATE",
            "parameters": {
                "encoding": "SIMPLE_INDEX"
            },
            "needed_columns": [
                "OUTCOME",
                "TREATMENT"
            ],
            "needed_info_for_training": [],
            "needed_info_for_prediction": [
                "available_resources",
                "treatment_duration"
            ],
            "supported_encoding": [
                "BOOLEAN",
                "FREQUENCY_BASED",
                "SIMPLE_INDEX"
            ],
            "online": "2023-03-18T15:35:38.473035"
        }
    }
}
```

The `plugins` field contains a dictionary of plugins. The key of each plugin is the plugin ID, and the value is the plugin information.
