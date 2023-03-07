---
title: "Get Projects"
weight: 50
---

To retrieve a subset of projects, you can specify the page number and size of the page. This allows you to retrieve a specific number of projects at a time instead of retrieving all projects at once.

## Request

Please note that this endpoint has optional path parameters.

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| GET | `/project/all` | `none` | Get projects based on page |

**Path parameters:**

{{< propertylist name=read-projects-request >}}

## Response

The response body of this endpoint contains several fields. The `items` field is a list of projects, while the `total` field represents the total number of projects. The `page` field indicates the current page number, and the `size` field indicates the maximum number of projects in a single page. Finally, the `pages` field represents the total number of pages.

```json
{
    "items": [
        {
            "name": "bpic2012-CSV.zip",
            "description": null,
            "status": "STREAMING",
            "id": 8,
            "created_at": "2023-03-05T15:48:04.759588+00:00",
            "updated_at": "2023-03-05T15:49:00.177047+00:00",
            "error": null,
            "event_log": {
                "file_name": "bpic2012-CSV.zip",
                "id": 9,
                "created_at": "2023-03-05T15:48:00.743589+00:00",
                "updated_at": "2023-03-05T15:48:05.590805+00:00",
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
                        "REG_DATE",
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
                    "id": 9,
                    "created_at": "2023-03-05T15:48:02.687644+00:00",
                    "updated_at": "2023-03-05T15:48:04.744921+00:00"
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
                    "status": "STREAMING",
                    "id": 14,
                    "created_at": "2023-03-05T15:48:19.810563+00:00",
                    "updated_at": "2023-03-05T15:49:00.329850+00:00",
                    "error": null
                },
                {
                    "name": "Random forest negative outcome probability",
                    "prescription_type": "ALARM",
                    "description": "This plugin predicts the alarm probability based on the random forest algorithm.",
                    "parameters": {},
                    "status": "STREAMING",
                    "id": 15,
                    "created_at": "2023-03-05T15:48:19.826009+00:00",
                    "updated_at": "2023-03-05T15:49:00.442122+00:00",
                    "error": null
                },
                {
                    "name": "CasualLift treatment effect",
                    "prescription_type": "TREATMENT_EFFECT",
                    "description": "This plugin uses Uplift Modeling package CasualLift to get the CATE and probability of outcome if treatment is applied or not",
                    "parameters": {},
                    "status": "STREAMING",
                    "id": 16,
                    "created_at": "2023-03-05T15:48:19.831114+00:00",
                    "updated_at": "2023-03-05T15:49:00.217228+00:00",
                    "error": null
                }
            ]
        }
    ],
    "total": 6,
    "page": 2,
    "size": 5,
    "pages": 2
}
```