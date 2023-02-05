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

### Request body example

```json
{
    "Case_ID": "CASE_ID",
    "Time": "TIMESTAMP",
    "Action": "ACTIVITY",
    "Personnel": "RESOURCE"
}
```

## Response

If the request is successful, the response will return the unique activities count, supported outcome selections, and supported treatment selections.

PrCore will automatically provide treatment selections list based on the algorithm plugins it has. For example, PrCore has the `CasualLift` plugin, so the treatment selections can include `Action` (`ACTIVITY`), `Personnel` (`RESOURCE`), and so on, because the `CasualLift` plugin finally only needs to know whether the case is treated according to your definition, it doesn't care about the treatment details.

```json
{
    "message": "Columns configuration updated successfully",
    "event_log_id": 123456,
    "received_definition": {
        "Case_ID": "CASE_ID",
        "Time": "TIMESTAMP",
        "Action": "ACTIVITY",
        "Personnel": "RESOURCE"
    },
    "activities_count": {
        "A": 53,
        "B": 20,
        "C": 12
    },
    "outcome_selections": [
        "Time",
        "Action",
        "Personnel",
        "DURATION",
    ],
    "treatment_selections": [
        "Time",
        "Action",
        "Personnel"
    ]
}
```
