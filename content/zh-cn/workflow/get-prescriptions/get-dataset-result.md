---
title: "新数据集结果"
weight: 10
---

Upon successfully [upload a new dataset](/workflow/send-new-data/upload-new-dataset/), the API response will include a `result_key`. In the event that a new test dataset was already uploaded during project creation, a `result_key` would have been provided in the response as well.

The `result_key` can be utilized to retrieve the dataset result.

## Request

The `project_id` and `result_key` are required in the request.

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| GET | `/project/{project_id}/result/{result_key}` | `none` | Get the result of the dataset |

## Response

If the result is not ready, the `cases` field will be `null`.

```json
{
    "message": "Ongoing dataset result is still processing",
    "project_status": "TRAINED",
    "expected_plugins": [
        "plugin-causallift-treatment-effect",
        "plugin-knn-next-activity",
        "plugin-random-forest-alarm"
    ],
    "finished_plugins": [
        "plugin-random-forest-alarm",
        "plugin-knn-next-activity"
    ],
    "cases_count": null,
    "columns": null,
    "columns_definition": null,
    "case_attributes": null,
    "cases": null
}
```

You will also get the current status of the project in the `project_status` field. The `expected_plugins` represents the list of plugins that are expected to give results. The `finished_plugins` field shows the list of plugins that have been successfully returned results.

In addition to these fields, the JSON object also contains the `cases_count` field which provides the number of cases that have been processed. However, if the result is not yet ready, this field will also be set to `null`. Similarly, the `columns` and `columns_definition` fields provide information about the columns in the dataset and their definitions respectively.

Below is an example of a complete result:

```json
{
    "message": "Ongoing dataset result retrieved successfully",
    "project_status": "TRAINED",
    "expected_plugins": [
        "plugin-causallift-treatment-effect",
        "plugin-knn-next-activity",
        "plugin-random-forest-alarm"
    ],
    "finished_plugins": [
        "plugin-random-forest-alarm",
        "plugin-knn-next-activity",
        "plugin-causallift-treatment-effect"
    ],
    "cases_count": 2618,
    "columns": [
        "Case ID",
        "start_time",
        "end_time",
        "AMOUNT_REQ",
        "REG_DATE",
        "Activity",
        "Resource"
    ],
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
        "AMOUNT_REQ",
        "REG_DATE"
    ],
    "cases": {
        "173688": {
            "prescriptions": [
                {
                    "date": "2023-03-04T12:31:53.626402",
                    "type": "ALARM",
                    "output": 0.364,
                    "plugin": {
                        "name": "Random forest negative outcome probability",
                        "model": "count-encoding",
                        "accuracy": 0.5472,
                        "precision": 0.5491,
                        "recall": 0.5472,
                        "f1_score": 0.5481
                    }
                },
                {
                    "date": "2023-03-04T12:31:53.670496",
                    "type": "NEXT_ACTIVITY",
                    "output": "A_ACTIVATED",
                    "plugin": {
                        "name": "KNN next activity prediction",
                        "model": "count-encoding",
                        "accuracy": 0.8446,
                        "precision": 0.8523,
                        "recall": 0.8446,
                        "f1_score": 0.8414
                    }
                },
                {
                    "date": "2023-03-04T12:31:54.638476",
                    "type": "TREATMENT_EFFECT",
                    "output": {
                        "proba_if_treated": 0.6827,
                        "proba_if_untreated": 0.0001,
                        "cate": 0.6826,
                        "treatment": [
                            [
                                {
                                    "value": "O_SENT_BACK",
                                    "column": "Activity",
                                    "operator": "EQUAL"
                                }
                            ]
                        ]
                    },
                    "plugin": {
                        "name": "CasualLift treatment effect",
                        "model": "count-encoding"
                    }
                }
            ],
            "events": [
                [
                    "173688",
                    "2011-09-30 22:38:44.546",
                    "2011-09-30 22:38:44.546",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "A_SUBMITTED",
                    "112"
                ],
                [
                    "173688",
                    "2011-09-30 22:38:44.880",
                    "2011-09-30 22:38:44.880",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "A_PARTLYSUBMITTED",
                    "112"
                ],
                [
                    "173688",
                    "2011-09-30 22:39:37.906",
                    "2011-09-30 22:39:37.906",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "A_PREACCEPTED",
                    "112"
                ],
                [
                    "173688",
                    "2011-10-01 09:36:46.437",
                    "2011-10-01 09:45:13.917",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "W_Completeren aanvraag",
                    "nan"
                ],
                [
                    "173688",
                    "2011-10-01 09:42:43.308",
                    "2011-10-01 09:42:43.308",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "A_ACCEPTED",
                    "10862"
                ],
                [
                    "173688",
                    "2011-10-01 09:45:09.243",
                    "2011-10-01 09:45:09.243",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "O_SELECTED",
                    "10862"
                ],
                [
                    "173688",
                    "2011-10-01 09:45:09.243",
                    "2011-10-01 09:45:09.243",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "A_FINALIZED",
                    "10862"
                ],
                [
                    "173688",
                    "2011-10-01 09:45:11.197",
                    "2011-10-01 09:45:11.197",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "O_CREATED",
                    "10862"
                ],
                [
                    "173688",
                    "2011-10-01 09:45:11.380",
                    "2011-10-01 09:45:11.380",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "O_SENT",
                    "10862"
                ],
                [
                    "173688",
                    "2011-10-01 10:15:41.290",
                    "2011-10-01 10:17:08.924",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "W_Nabellen offertes",
                    "nan"
                ],
                [
                    "173688",
                    "2011-10-08 14:26:57.720",
                    "2011-10-08 14:32:00.886",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "W_Nabellen offertes",
                    "10913"
                ],
                [
                    "173688",
                    "2011-10-10 09:32:22.495",
                    "2011-10-10 09:33:05.791",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "W_Nabellen offertes",
                    "11049"
                ],
                [
                    "173688",
                    "2011-10-10 09:33:03.668",
                    "2011-10-10 09:33:03.668",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "O_SENT_BACK",
                    "11049"
                ],
                [
                    "173688",
                    "2011-10-13 08:05:26.925",
                    "2011-10-13 08:37:37.026",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "W_Valideren aanvraag",
                    "10629"
                ],
                [
                    "173688",
                    "2011-10-13 08:37:29.226",
                    "2011-10-13 08:37:29.226",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "A_REGISTERED",
                    "10629"
                ],
                [
                    "173688",
                    "2011-10-13 08:37:29.226",
                    "2011-10-13 08:37:29.226",
                    "20000",
                    "2011-09-30T22:38:44.546Z",
                    "A_APPROVED",
                    "10629"
                ]
            ]
        },
        "173712": {
            "prescriptions": [
                {
                    "date": "2023-03-04T12:31:53.626431",
                    "type": "ALARM",
                    "output": 0.7246,
                    "plugin": {
                        "name": "Random forest negative outcome probability",
                        "model": "count-encoding",
                        "accuracy": 0.5472,
                        "precision": 0.5491,
                        "recall": 0.5472,
                        "f1_score": 0.5481
                    }
                },
                {
                    "date": "2023-03-04T12:31:53.670533",
                    "type": "NEXT_ACTIVITY",
                    "output": "A_DECLINED",
                    "plugin": {
                        "name": "KNN next activity prediction",
                        "model": "count-encoding",
                        "accuracy": 0.8446,
                        "precision": 0.8523,
                        "recall": 0.8446,
                        "f1_score": 0.8414
                    }
                },
                {
                    "date": "2023-03-04T12:31:54.638498",
                    "type": "TREATMENT_EFFECT",
                    "output": {
                        "proba_if_treated": 0.7061,
                        "proba_if_untreated": 0.0001,
                        "cate": 0.706,
                        "treatment": [
                            [
                                {
                                    "value": "O_SENT_BACK",
                                    "column": "Activity",
                                    "operator": "EQUAL"
                                }
                            ]
                        ]
                    },
                    "plugin": {
                        "name": "CasualLift treatment effect",
                        "model": "count-encoding"
                    }
                }
            ],
            "events": [
                [
                    "173712",
                    "2011-10-01 07:58:30.533",
                    "2011-10-01 07:58:30.533",
                    "30000",
                    "2011-10-01T07:58:30.533Z",
                    "A_SUBMITTED",
                    "112"
                ],
                [
                    "173712",
                    "2011-10-01 07:58:30.678",
                    "2011-10-01 07:58:30.678",
                    "30000",
                    "2011-10-01T07:58:30.533Z",
                    "A_PARTLYSUBMITTED",
                    "112"
                ],
                [
                    "173712",
                    "2011-10-01 08:08:36.700",
                    "2011-10-01 08:10:25.759",
                    "30000",
                    "2011-10-01T07:58:30.533Z",
                    "W_Afhandelen leads",
                    "10912"
                ],
                [
                    "173712",
                    "2011-10-01 08:10:24.737",
                    "2011-10-01 08:10:24.737",
                    "30000",
                    "2011-10-01T07:58:30.533Z",
                    "A_PREACCEPTED",
                    "10912"
                ],
                [
                    "173712",
                    "2011-10-01 10:59:13.844",
                    "2011-10-01 11:03:35.216",
                    "30000",
                    "2011-10-01T07:58:30.533Z",
                    "W_Completeren aanvraag",
                    "11019"
                ]
            ]
        }
    }
}
```