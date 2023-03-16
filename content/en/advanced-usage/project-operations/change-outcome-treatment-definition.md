---
title: "Change Outcome And Treatment Definition"
weight: 20
---

{{< hint type=note icon=gdoc_info_outline >}}
If you don't need to change the outcome and treatment definition, you can skip this step.

But, if you just changed the columns definition after the project is created, then you must redefine the outcome and treatment definition here.
{{< /hint >}}

If you think the outcome and treatment definition is not suitable for your project, you can change it. The procedure is very similar with the `Create project` step in the [Upload Event Log](/workflow/upload-event-log/project-creation/) section.

{{< hint type=warning icon=gdoc_info_outline >}}
Upon the modification of the outcome and treatment definitions, the project status will be altered to `WAITING`, and the pre-processing and training tasks will restart from the beginning. If there is any ongoing simulation of streaming data, it will automatically be terminated, and the project will not accept any streaming data until the new training has been completed.
{{< /hint >}}


## Request

This endpoint is for updating the definition for outcome and treatment of the project. The `project_id` is the ID of the project which you want to update.

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/project/{project_id}/definition` | `json` | Outcome and treatment definition, resulting a updated project |

```json
{
    "event_log_id": 123456,
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
    ]
}
```

## Response

In the response, a `project` object will be returned.

```json
{
    "message": "Project definition updated successfully",
    "project": {
        "name": "bpic2012-CSV.zip",
        "description": null,
        "status": "PREPROCESSING",
        "id": 20,
        "created_at": "2023-03-04T09:26:36.572249+00:00",
        "updated_at": "2023-03-04T09:39:56.514738+00:00",
        "event_log": {
            "file_name": "bpic2012-CSV.zip",
            "id": 21,
            "created_at": "2023-03-04T08:56:29.577241+00:00",
            "updated_at": "2023-03-04T09:39:48.660745+00:00",
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
                "name": "KNN next activity prediction",
                "prescription_type": "NEXT_ACTIVITY",
                "description": "This plugin predicts the next activity based on the KNN algorithm.",
                "parameters": {
                    "n_neighbors": "3"
                },
                "status": "WAITING",
                "id": 49,
                "created_at": "2023-03-04T09:26:51.747310+00:00",
                "updated_at": "2023-03-04T09:39:56.469988+00:00"
            },
            {
                "name": "Random forest negative outcome probability",
                "prescription_type": "ALARM",
                "description": "This plugin predicts the alarm probability based on the random forest algorithm.",
                "parameters": {},
                "status": "WAITING",
                "id": 50,
                "created_at": "2023-03-04T09:26:51.765416+00:00",
                "updated_at": "2023-03-04T09:39:56.476862+00:00"
            },
            {
                "name": "CasualLift treatment effect",
                "prescription_type": "TREATMENT_EFFECT",
                "description": "This plugin uses Uplift Modeling package CasualLift to get the CATE and probability of outcome if treatment is applied or not",
                "parameters": {},
                "status": "WAITING",
                "id": 51,
                "created_at": "2023-03-04T09:26:51.770798+00:00",
                "updated_at": "2023-03-04T09:39:48.641647+00:00"
            }
        ]
    },
    "result_key": null
}
```
