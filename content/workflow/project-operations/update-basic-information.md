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
    "message": "Project's basic information updated successfully",
    "project": {
        "name": "New name",
        "description": "This is a custom description",
        "status": "PREPROCESSING",
        "id": 20,
        "created_at": "2023-03-04T09:26:36.572249+00:00",
        "updated_at": "2023-03-04T09:40:25.232989+00:00",
        "event_log": {
            "file_name": "bpic2012-CSV.zip",
            "id": 21,
            "created_at": "2023-03-04T08:56:29.577241+00:00",
            "updated_at": "2023-03-04T09:39:57.374625+00:00",
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
                "updated_at": "2023-03-04T09:39:56.483444+00:00"
            }
        },
        "plugins": [
            {
                "name": "Random forest negative outcome probability",
                "prescription_type": "ALARM",
                "description": "This plugin predicts the alarm probability based on the random forest algorithm.",
                "parameters": {},
                "status": "PREPROCESSING",
                "id": 50,
                "created_at": "2023-03-04T09:26:51.765416+00:00",
                "updated_at": "2023-03-04T09:40:11.787101+00:00"
            },
            {
                "name": "CasualLift treatment effect",
                "prescription_type": "TREATMENT_EFFECT",
                "description": "This plugin uses Uplift Modeling package CasualLift to get the CATE and probability of outcome if treatment is applied or not",
                "parameters": {},
                "status": "TRAINED",
                "id": 51,
                "created_at": "2023-03-04T09:26:51.770798+00:00",
                "updated_at": "2023-03-04T09:40:13.392150+00:00"
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
                "updated_at": "2023-03-04T09:40:23.696220+00:00"
            }
        ]
    }
}
```
