---
title: "Change Columns Definition"
weight: 10
---

{{< hint type=note icon=gdoc_info_outline >}}
If you don't need to change the columns definition, you can skip this step.
{{< /hint >}}

If you think the columns definition is not suitable for your project, you can change it. The procedure is very similar with the `columns-definition` step in the [Upload Event Log](/workflow/upload-event-log/columns-definition/) section.

{{< hint type=warning icon=gdoc_info_outline >}}
1. You can only change the columns definition after the previous training is finished.
2. After the change of the columns definition, the outcome and treatment definition will be removed. You need to set the outcome and treatment definition again.
3. After the change of the columns definition, the project status will be changed to `WAITING`. It will be expecting new outcome and treatment definition. After the all definitions are submiited, it will restart the pre-processing and training tasks all over again. If there is a running simulation of streaming datas, it will be also turned off automatically. The project will not accept streaming data until the new training is finished.
{{< /hint >}}

---

## Get basic information of the event log

The only difference is that you can get the basic information of the event log via the API before you update the definition.

You may not need to get the basic information of the event log, if your application already has the information.

### Request

Here we need use the `event_log_id` to get the definition of the columns.

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/event_log/{event_log_id}/definition` | Get columns definition |

### Response

Please note that **there is no `columns_inferred_definition` in the response, instead, there is a `columns_old_definition` which is the old definition** of the columns.

```json
{
    "message": "Event log definition retrieved successfully",
    "event_log_id": 21,
    "columns_header": [
        "Case ID",
        "Activity",
        "REG_DATE",
        "Resource",
        "end_time",
        "AMOUNT_REQ",
        "start_time"
    ],
    "columns_old_definition": [
        "CASE_ID",
        "ACTIVITY",
        "DATETIME",
        "RESOURCE",
        "END_TIMESTAMP",
        "NUMBER",
        "START_TIMESTAMP"
    ],
    "columns_data": [
        [
            "173688",
            "2011-09-30T22:38:44.546",
            "2011-09-30T22:38:44.546",
            "20000",
            "2011-09-30T22:38:44.546Z",
            "A_SUBMITTED",
            "112"
        ],
        [
            "173688",
            "2011-09-30T22:38:44.880",
            "2011-09-30T22:38:44.880",
            "20000",
            "2011-09-30T22:38:44.546Z",
            "A_PARTLYSUBMITTED",
            "112"
        ],
        [
            "173688",
            "2011-09-30T22:39:37.906",
            "2011-09-30T22:39:37.906",
            "20000",
            "2011-09-30T22:38:44.546Z",
            "A_PREACCEPTED",
            "112"
        ],
        [
            "173688",
            "2011-10-01T09:36:46.437",
            "2011-10-01T09:45:13.917",
            "20000",
            "2011-09-30T22:38:44.546Z",
            "W_Completeren aanvraag",
            "nan"
        ],
        [
            "173688",
            "2011-10-01T09:42:43.308",
            "2011-10-01T09:42:43.308",
            "20000",
            "2011-09-30T22:38:44.546Z",
            "A_ACCEPTED",
            "10862"
        ]
    ]
}
```

---

## Update the definition

This step is same as the `columns-definition` step in the [Upload Event Log](/workflow/upload-event-log/columns-definition/) section.

### Request

The request body is a JSON object, the key is the column name, and the value is the column definition.

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/event_log/{event_log_id}` | `json` | Columns configuration |

```json
{
    "columns_definition": {
        "Case ID": "CASE_ID",
        "start_time": "START_TIMESTAMP",
        "end_time": "END_TIMESTAMP",
        "AMOUNT_REQ": "NUMBER",
        "REG_DATE": "DATETIME",
        "Activity": "ACTIVITY",
        "Resource": "RESOURCE"
    },
    "case_attributes": ["Case ID", "AMOUNT_REQ"]
}
```

### Response

If the request is successful, the response will return the unique activities count, supported outcome selections, and supported treatment selections.

```json
{
    "message": "Event log updated",
    "event_log_id": 21,
    "received_definition": {
        "Case ID": "CASE_ID",
        "Activity": "ACTIVITY",
        "REG_DATE": "DATETIME",
        "Resource": "RESOURCE",
        "end_time": "END_TIMESTAMP",
        "AMOUNT_REQ": "NUMBER",
        "start_time": "START_TIMESTAMP"
    },
    "activities_count": {
        "W_Completeren aanvraag": 23967,
        "W_Nabellen offertes": 22977,
        "A_SUBMITTED": 13087,
        "A_PARTLYSUBMITTED": 13087,
        "W_Nabellen incomplete dossiers": 11407,
        "W_Valideren aanvraag": 7897,
        "A_DECLINED": 7635,
        "A_PREACCEPTED": 7367,
        "O_SENT": 7030,
        "O_SELECTED": 7030,
        "O_CREATED": 7030,
        "W_Afhandelen leads": 5898,
        "A_ACCEPTED": 5113,
        "A_FINALIZED": 5015,
        "O_CANCELLED": 3655,
        "O_SENT_BACK": 3454,
        "A_CANCELLED": 2807,
        "A_REGISTERED": 2246,
        "A_APPROVED": 2246,
        "A_ACTIVATED": 2246,
        "O_ACCEPTED": 2243,
        "O_DECLINED": 802,
        "W_Beoordelen fraude": 270
    },
    "outcome_options": [
        "Activity",
        "REG_DATE",
        "Resource",
        "end_time",
        "AMOUNT_REQ",
        "start_time",
        "DURATION"
    ],
    "treatment_options": [
        "Activity",
        "REG_DATE",
        "Resource",
        "end_time",
        "AMOUNT_REQ",
        "start_time"
    ]
}
```
