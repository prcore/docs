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
    "event_log_id": 73,
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
    "resources_count": {
        "112": 36029,
        "10138": 5241,
        "11169": 4739,
        "10861": 4383,
        "11181": 4326,
        "10972": 4215,
        "10609": 4185,
        "11189": 4139,
        "10913": 4004,
        "11119": 3978,
        "11180": 3957,
        "10909": 3844,
        "11203": 3661,
        "10982": 3582,
        "11201": 3550,
        "11122": 3426,
        "10629": 3234,
        "10910": 2936,
        "10809": 2772,
        "10932": 2629,
        "11049": 2580,
        "11121": 2451,
        "10881": 2446,
        "11179": 2399,
        "11000": 2393,
        "11259": 2237,
        "11003": 2204,
        "11009": 2198,
        "10929": 2155,
        "10889": 2136,
        "10899": 2072,
        "10863": 1828,
        "11202": 1734,
        "10939": 1682,
        "10912": 1583,
        "11200": 1486,
        "11019": 1419,
        "11289": 1200,
        "11002": 1127,
        "10933": 1100,
        "10931": 1097,
        "11120": 705,
        "10789": 680,
        "10880": 660,
        "11300": 596,
        "11302": 591,
        "10935": 584,
        "10862": 492,
        "11299": 469,
        "11319": 446,
        "11309": 427,
        "10971": 410,
        "11029": 370,
        "10859": 338,
        "10228": 323,
        "10188": 267,
        "10914": 243,
        "11001": 184,
        "10779": 74,
        "11339": 60,
        "11111": 39,
        "11079": 20,
        "11304": 19,
        "10124": 5,
        "11254": 3,
        "11269": 3,
        "10125": 2,
        "10821": 1
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
