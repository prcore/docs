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

Please note that there is no `columns_inferred_definition` in the response, instead, there is a `columns_old_definition` which is the old definition of the columns.

```json
{
    "message": "Columns definition retrieved successfully",
    "event_log_id": 123456,
    "columns_header": ["Case_ID", "Time", "Action", "Personnel"],
    "columns_old_definition": ["CASE_ID", "TIMESTAMP", "ACTIVITY", "RESOURCE"],
    "columns_data": [
        ["1", "2019-01-01 00:00:00", "A", "1"],
        ["1", "2019-01-01 00:00:00", "B", "1"],
        ["1", "2019-01-01 00:00:00", "C", "2"],
        ["1", "2019-01-01 00:00:00", "C", "2"],
        ["1", "2019-01-01 00:00:00", "C", "2"]
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
    "Case_ID": "CASE_ID",
    "Time": "TIMESTAMP",
    "Action": "ACTIVITY",
    "Personnel": "RESOURCE"
}
```

### Response

If the request is successful, the response will return the unique activities count, supported outcome selections, and supported treatment selections.

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
