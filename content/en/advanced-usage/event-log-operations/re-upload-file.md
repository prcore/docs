---
title: "Re-upload File"
weight: 10
---

If you need to retrain the model with a new dataset after the project has already been trained, you can use the function to re-upload logs.

## Request

Please note that you can only re-upload logs when the project status is `TRAINED`, `SIMULATING`, or `STREAMING`. If there is an ongoing streaming mode, it will be automatically stopped. The sent file should contain all previously defined columns, otherwise an error will be returned.

### General information

| Method | Endpoint | Request Body Type	 | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/event_log/{event_log_id}/upload` | `form-data` | Re-upload log file |

### Request Body Properties

{{< propertylist name=re-upload-request >}}

## Response

If the upload is successful, you will get the following response, and the project will automatically start retraining, using the definitions, parameters, and additional information you have previously provided.

```json
{
    "message": "Event log updated",
    "event_log_id": 22,
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
