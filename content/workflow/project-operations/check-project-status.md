---
title: "Check Project Status"
weight: 10
---

After the project is created, PrCore will start to pre-process the data\, and after the pre-processing is done, PrCore will send the dataset to its plugins for training models. The whole process will take some time. We can check the project status to see the progress.

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
    "message": "Project created successfully",
    "project": {
        "id": 1,
        "created_at": "2023-02-08T07:40:35.510479+00:00",
        "updated_at": null,
        "name": "bpic2012-CSV.zip",
        "description": null,
        "status": "PREPROCESSING",
        "event_log": {
            "id": 1,
            "created_at": "2023-02-08T07:40:27.601771+00:00",
            "updated_at": "2023-02-08T07:40:31.332790+00:00",
            "file_name": "bpic2012-CSV.zip",
            "definition": {
                "id": 1,
                "created_at": "2023-02-08T07:40:31.314273+00:00",
                "updated_at": "2023-02-08T07:40:35.489616+00:00",
                "columns_definition": {
                    "Case ID": "CASE_ID",
                    "Activity": "ACTIVITY",
                    "REG_DATE": "DATETIME",
                    "Resource": "TEXT",
                    "end_time": "END_TIMESTAMP",
                    "AMOUNT_REQ": "NUMBER",
                    "start_time": "START_TIMESTAMP"
                },
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
                ]
            }
        },
        "plugins": [
            {
                "id": 1,
                "created_at": "2023-02-08T07:40:35.510479+00:00",
                "updated_at": null,
                "name": "KNN next activity prediction",
                "prescription_type": "NEXT_ACTIVITY",
                "description": "This plugin predicts the next activity based on the KNN algorithm.",
                "status": "WAITING"
            },
            {
                "id": 2,
                "created_at": "2023-02-08T07:40:35.510479+00:00",
                "updated_at": null,
                "name": "Random forest negative outcome probability",
                "prescription_type": "ALARM",
                "description": "This plugin provides the probability of negative outcome.",
                "status": "WAITING"
            },
            {
                "id": 3,
                "created_at": "2023-02-08T07:40:35.510479+00:00",
                "updated_at": null,
                "name": "CasualLift",
                "prescription_type": "TREATMENT_EFFECT",
                "description": "This plugin uses Uplift Modeling package 'CasualLift' to predict the positive outcome probability if the treatment is applied, the positive outcome probability if the treatment is not applied, and the treatment effect (CATE), and suggested treatment based on the user's treatment definition.",
                "status": "WAITING"
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
- If the status is not empty and not one of the above, it means the project is in an error state, and the content will be the error message.

#### Plugin status

The `status` field of the plugin indicates the status of the plugin. The `status` field can be one of the following values:

- `WAITING`: The plugin is waiting for the core application sending the training data.
- `TRAINING`: The plugin is training the model.
- `TRAINED`: The plugin has trained the model and is ready to be used.
- `ACTIVATING`: The plugin is activating, and after the activation, the plugin status will be changed to `STREAMING`.
- `STREAMING`: The plugin is expecting new streaming events.
- If the status is not empty and not one of the above, it means the plugin is in an error state, and the content will be the error message.

#### Prescription type

The `prescription_type` field of the plugin indicates the type of the plugin. The `prescription_type` field can be one of the following values:

- `NEXT_ACTIVITY`: The plugin predicts the next activity.
- `ALARM`: The plugin provides the probability of negative outcome.
- `TREATMENT_EFFECT`: The plugin provides the treatment effect.
