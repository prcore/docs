---
title: "Columns Definition"
toc: true
weight: 20
---

Since we have the first 5 events data, we can display them in a table, and let the user to define the columns.

## Request

The request body is a JSON object, the key is the column name, and the value is the column definition.

### General information

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/event_log/{event_log_id}` | `json` | Columns configuration |

### Request body porperties

{{< propertylist name=columns-request >}}

{{< hint type=important icon=gdoc_info_outline >}}
Theses attributes `fast_mode`, `start_transition`, `complete_transition`, `abort_transition` are optional, and are explained in the [Advanced Usage - Log Definition]({{ relref "../../advanced-usage/event-log-operations/log-definition.md" }}) section. Before you check this section, please ignore these attributes, otherwise, some unexpected behaviors may occur.
{{< /hint >}}

### Request body example

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

## Response

Upon a successful request, the API response will provide three distinct pieces of information: the count of unique activities, the available outcome options, and the available treatment options.

It should be noted that the `outcome_options` and `treatment_options` can be utilized to select the specific columns that will generate the outcome and treatment labels when [creating the project]({{ relref "./project-creation.md" }}).

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
