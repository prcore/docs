---
title: "Change Outcome And Treatment Definition"
weight: 30
---

{{< hint type=note icon=gdoc_info_outline >}}
If you don't need to change the outcome and treatment definition, you can skip this step.

But, if you just changed the columns definition after the project is created, then you must redefine the outcome and treatment definition here.
{{< /hint >}}

If you think the outcome and treatment definition is not suitable for your project, you can change it. The procedure is very similar with the `Create project` step in the [Upload Event Log](/workflow/upload-event-log/project-creation/) section.

{{< hint type=warning icon=gdoc_info_outline >}}
After the change of the outcome and treatment definition, the project status will be changed to `WAITING`. It will restart the pre-processing and training tasks all over again. If there is a running simulation of streaming data, it will be also turned off automatically. The project will not accept streaming data until the new training is finished.
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
                "column": "Action",
                "operator": "EQUAL",
                "value": "A",
            },
            {
                "column": "DUARTION",
                "operator": "LESS_THAN",
                "value": 100
            }
        ],
        [
            {
                "column": "Personnel",
                "operator": "EQUAL",
                "value": "B"
            }
        ]
    ],
    "treatment": [
        [
            {
                "column": "Action",
                "operator": "EQUAL",
                "value": "C"
            }
        ]
    ]
}
```

## Response

In the response, a `project` object will be returned.

```json
{
    "message": "Project's outcome and treatment definition updated successfully",
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
        "plugins": []
    }
}
```
