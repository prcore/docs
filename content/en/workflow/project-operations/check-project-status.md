---
title: "Check Project Status"
weight: 10
---

Upon project creation, PrCore will commence the pre-processing of data. Once pre-processing is completed, PrCore will proceed to send the dataset to its plugins to train models. Given the complexity of this task, the entire process is likely to take a while. The user can keep track of the progress by checking the project status.

## Request

The `project_id` is the ID of the project we want to check.

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| GET | `/project/{project_id}` | `none` | Get the latest details of the specified project |

## Response

The response will return the project details, including the project status, the status, and plugins status.

### Example

Here is an example of the response.

```json
{
    "message": "Project retrieved successfully",
    "project": {
        "name": "bpic2012-CSV.zip",
        "description": null,
        "status": "TRAINED",
        "id": 20,
        "created_at": "2023-03-04T09:26:36.572249+00:00",
        "updated_at": "2023-03-04T09:27:17.961998+00:00",
        "error": null,
        "event_log": {
            "file_name": "bpic2012-CSV.zip",
            "id": 21,
            "created_at": "2023-03-04T08:56:29.577241+00:00",
            "updated_at": "2023-03-04T09:26:37.578501+00:00",
            "definition": {
                "columns_definition": {
                    "Case ID": "CASE_ID",
                    "Activity": "ACTIVITY",
                    "REG_DATE": "DATETIME",
                    "Resource": "RESOURCE",
                    "end_time": "END_TIMESTAMP",
                    "AMOUNT_REQ": "NUMBER",
                    "start_time": "START_TIMESTAMP"
                },
                "case_attributes": [
                    "Case ID",
                    "AMOUNT_REQ"
                ],
                "outcome_definition": [
                    [
                        {
                            "column": "Activity",
                            "operator": "EQUAL",
                            "value": "A_APPROVED"
                        }
                    ]
                ],
                "treatment_definition": [
                    [
                        {
                            "column": "Activity",
                            "operator": "EQUAL",
                            "value": "O_SENT_BACK"
                        }
                    ]
                ],
                "fast_mode": true,
                "start_transition": "START",
                "complete_transition": "COMPLETE",
                "abort_transition": "ATE_ABORT",
                "id": 21,
                "created_at": "2023-03-04T09:10:52.970059+00:00",
                "updated_at": "2023-03-04T09:26:36.564989+00:00"
            }
        },
        "plugins": [
            {
                "name": "CasualLift treatment effect",
                "prescription_type": "TREATMENT_EFFECT",
                "description": "This plugin uses Uplift Modeling package CasualLift to get the CATE and probability of outcome if treatment is applied or not",
                "parameters": {},
                "status": "TRAINED",
                "id": 51,
                "created_at": "2023-03-04T09:26:51.770798+00:00",
                "updated_at": "2023-03-04T09:26:53.239740+00:00"
            },
            {
                "name": "KNN next activity prediction",
                "prescription_type": "NEXT_ACTIVITY",
                "description": "This plugin predicts the next activity based on the KNN algorithm.",
                "parameters": {
                    "n_neighbors": "3"
                },
                "status": "TRAINED",
                "id": 49,
                "created_at": "2023-03-04T09:26:51.747310+00:00",
                "updated_at": "2023-03-04T09:27:03.028610+00:00"
            },
            {
                "name": "Random forest negative outcome probability",
                "prescription_type": "ALARM",
                "description": "This plugin predicts the alarm probability based on the random forest algorithm.",
                "parameters": {},
                "status": "TRAINED",
                "id": 50,
                "created_at": "2023-03-04T09:26:51.765416+00:00",
                "updated_at": "2023-03-04T09:27:17.957868+00:00"
            }
        ]
    }
}
```

{{< hint type=note icon=gdoc_info_outline >}}
The core program will ask its plugins wheter they are applicable to your dataset and definition. If the plugins are not applicable, the plugin will not be added to the `plugins` list. So, before the project status is changed to `TRAINING`, the `plugins` list may be empty and changing from time to time.
{{< /hint >}}

### Explanation

Here we explain some fields in the response.

#### Project status

The `status` field of the project indicates the overall status of the project. The `status` field can be one of the following values:

- `WAITING`: The project is waiting for the new definition to be submitted.
- `PREPROCESSING`: The uploaded data is being pre-processed.
- `TRAINING`: The data is being processed by the plugins.
- `TRAINED`: The models of plugins are trained and ready to be used.
- `ACTIVATING`: The project is activating. After all the plugins are activated, the project status will be changed to `STREAMING`.
- `STREAMING`: The project is expecting new streaming events. This status is only used for the projects that are expecting external streaming events. For the projects that are simulating the streaming events, the project status will be `SIMULATING`.
- `SIMULATING`: The project is simulating the streaming events, and the simulation is not finished yet.
- `ERROR`: The project is in an error state. The error message will be in the `error` field.

#### Plugin status

The `status` field of the plugin indicates the status of the plugin. The `status` field can be one of the following values:

- `WAITING`: The plugin is waiting for the core application sending the training data.
- `TRAINING`: The plugin is training the model.
- `TRAINED`: The plugin has trained the model and is ready to be used.
- `ACTIVATING`: The plugin is activating, and after the activation, the plugin status will be changed to `STREAMING`.
- `STREAMING`: The plugin is expecting new streaming events.
- `ERROR`: The plugin is in an error state. The error message will be in the `error` field.

#### Prescription type

The `prescription_type` field of the plugin indicates the type of the plugin. The `prescription_type` field can be one of the following values:

- `NEXT_ACTIVITY`: The plugin predicts the next activity.
- `ALARM`: The plugin provides the probability of negative outcome.
- `TREATMENT_EFFECT`: The plugin provides the treatment effect.
- `RESOURCE_ALLOCATION`: The plugin provides the resource allocation suggestion.

For more information about the prescription types, please refer to [Result Explanation]({{< relref "../../workflow/get-prescriptions/result-explanation.md" >}}).

If you're using your own plugins, it will return the type string you defined in the plugin.
