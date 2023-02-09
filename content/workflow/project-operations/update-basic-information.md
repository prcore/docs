---
title: "Update Basic Information"
weight: 40
---

This step is optional. If you would like to update the basic information of the project, you can do so.

## Request

The `project_id` is the ID of the project we want to update.

### General information

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/project/{project_id}` | `json` | Update the project's name or description |

### Request body parameters

{{< propertylist name=project-update-request >}}

### Example

```json
{
    "name": "My new project",
    "description": "This is my new project"
}
```

## Response

The response will return the project details, including the project status, the status, and plugins status.

### Example

Here is an example of the response.

```json
{
    "message": "Project updated successfully",
    "project": {
        "id": 1,
        "created_at": "2023-02-08T07:40:35.510479+00:00",
        "updated_at": "2023-02-08T07:42:35.510479+00:00",
        "name": "My new project",
        "description": "This is my new project",
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
