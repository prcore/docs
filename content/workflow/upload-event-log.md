---
title: "Upload Event Log"
toc: true
---

{{< toc format=html >}}

## Introduction

The first step is to upload the event log files via the API. Currently, the supported formats are standard XES files and CSV files.

We can use any tool or program to access the PrCore API. The following example assumes we are using [VisualPM](https://github.com/VisualPM) and presents the process for uploading files in a sequence diagram.

{{< mermaid class="text-center" >}}
sequenceDiagram
    VisualPM->>PrCore: Upload event log
    PrCore->>VisualPM: Returns first 5 events data with headers attached
    VisualPM->>PrCore: Submit column definitions
    PrCore->>VisualPM: Return the unique activities count, <br>supported outcome selections, <br>and supported treatment selections
    VisualPM->>PrCore: Submit outcome definition and treatment definition
    PrCore->>VisualPM: Event log confirmed, a new project created
{{< /mermaid >}}

Next, the details of each step will be explained.

---

## Uploading

Uploaded event log files will be stored in the PrCore server, and the event log ID will be returned. The event log ID will be used in the following steps.

### Request

File upload is a `multipart/form-data` request, and the file should be attached to the `file` field.

#### General information

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| POST | `/event_log` | `form-data` | Upload event log |

#### Request body porperties

{{< propertylist name=uploading-request >}}

### Response

Based on the event log file, the events attributes will be different, so here is just an example. The response will return the first 5 events data with headers and inferred definitions attached.

The first row of `events_head` is the column names, the second row is the inferred column definitions (some elements can be null), and the following rows are the events data.

{{< tabs "uploading-response-tab-id" >}}
{{< tab "Success" >}}

```json
{
    "message": "Event log uploaded successfully",
    "event_log_id": 123456,
    "events_head": [
        ["Case_ID", "Time", "Action", "Personnel"],
        ["CASE_ID", "TIMESTAMP", "ACTIVITY", null],
        ["1", "2019-01-01 00:00:00", "A", "1"],
        ["1", "2019-01-01 00:00:00", "B", "1"],
        ["1", "2019-01-01 00:00:00", "C", "2"],
        ["1", "2019-01-01 00:00:00", "C", "2"],
        ["1", "2019-01-01 00:00:00", "C", "2"]
    ]
}
```
{{< /tab >}}
{{< tab "Error" >}}
```json
{
    "message": "Event log upload failed",
    "error": "Error message"
}
```
{{< /tab >}}
{{< /tabs >}}

---

## Columns configuration

Since we have the first 5 events data, we can display them in a table, and let the user to define the columns.

### Request

The request body is a JSON object, the key is the column name, and the value is the column definition.

#### General information

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| PUT | `/event_log/{event_log_id}` | `json` | Columns configuration |

#### Request body porperties

{{< propertylist name=columns-request >}}

#### Request body example

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

PrCore will automatically provide treatment selections list based on the algorithm plugins it has. For example, PrCore has the `CasualLift` plugin, so the treatment selections can include `ACTIVITY`, `RESOURCE`, and so on, because the `CasualLift` plugin finally only needs to know whether the case is treated according to your definition, it doesn't care about the treatment details.

{{< tabs "columns-response-tab-id" >}}
{{< tab "Success" >}}
```json
{
    "message": "Columns configuration updated successfully",
    "event_log_id": 123456,
    "activities_count": {
        "A": 53,
        "B": 20,
        "C": 12
    },
    "outcome_selections": [
        "TEXT",
        "NUMBER",
        "BOOLEAN",
        "TIMESTAMP",
        "ACTIVITY",
        "DURATION",
        "COST"
    ],
    "treatment_selections": [
        "ACTIVITY",
        "RESOURCE",
        "DURATION"
    ]
}
```
{{< /tab >}}
{{< tab "Error" >}}
```json
{
    "message": "Columns configuration update failed",
    "error": "Error message"
}
```
{{< /tab >}}
{{< /tabs >}}

---

## Outcome and treatment Definition

After the previous step, we got unique activities count, and supported outcome and treatment selections from PrCore, then we can define what is the positive outcome and what is the treatment.

### Request

This endpoint is for creating a new project, and the definition of outcome and treatment is required.

#### General information

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| POST | `/project` | `json` | Outcome and treatment definition, resulting a created project |

#### Request body porperties

{{< propertylist name=definition-request >}}

{{< hint type=note icon=gdoc_info_outline title="Note for outcome definition" >}}
Following outcome selections has these predefined evaluation methods (operators):

- `TEXT` (also for `ACTIVITY` and `RESOURCE`)
    - `EQUAL`
    - `NOT_EQUAL`
    - `CONTAINS`
    - `NOT_CONTAINS`
- `NUMBER` (also for `DURATION` and `COST`)
    - `EQUAL`
    - `NOT_EQUAL`
    - `GREATER_THAN`
    - `LESS_THAN`
    - `GREATER_THAN_OR_EQUAL`
    - `LESS_THAN_OR_EQUAL`
- `BOOLEAN`
    - `IS_TRUE`
    - `IS_FALSE`
- `DATETIME` (also for `TIMESTAMP`, `START_TIMESTAMP`, and `END_TIMESTAMP`)
    - `EQUAL`
    - `NOT_EQUAL`
    - `LATER_THAN`
    - `EARLIER_THAN`
    - `LATER_THAN_OR_EQUAL`
    - `EARLIER_THAN_OR_EQUAL`

For example, if you want to define the outcome as `Offer sent` activity happened, you can select `ACTIVITY` as the outcome selection, and select `EQUAL` as the operator, and choose `Offer sent` as the value.

```
"positive_outcome": [
    {
        "type": "ACTIVITY",
        "operator": "EQUAL",
        "value": "Offer sent"
    }
]
```

PrCore will evaluate the event log, and find out whether the `Offer sent` activity happened in any event, if it happened, then it knows the event's belonging case has positive outcome, otherwise, it has negative outcome. PrCore will use this information to train the model.

{{< /hint >}}

{{< hint type=note icon=gdoc_info_outline title="Note for treatment definition" >}}
Following treatment selections has these predefined evaluation methods (operators):

- `TEXT` (also for `ACTIVITY` and `RESOURCE`)
    - `EQUAL`
    - `NOT_EQUAL`
    - `CONTAINS`
    - `NOT_CONTAINS`
- `NUMBER` (also for `DURATION` and `COST`)
    - `EQUAL`
    - `NOT_EQUAL`
    - `GREATER_THAN`
    - `LESS_THAN`
    - `GREATER_THAN_OR_EQUAL`
    - `LESS_THAN_OR_EQUAL`
- `BOOLEAN`
    - `IS_TRUE`
    - `IS_FALSE`
- `DATETIME` (also for `TIMESTAMP`, `START_TIMESTAMP`, and `END_TIMESTAMP`)
    - `EQUAL`
    - `NOT_EQUAL`
    - `LATER_THAN`
    - `EARLIER_THAN`
    - `LATER_THAN_OR_EQUAL`
    - `EARLIER_THAN_OR_EQUAL`

For example, if you want to define the treatment as `Change application type` activity happened, you can select `ACTIVITY` as the treatment selection, and select `EQUAL` as the operator, and choose `Change application type` as the value.

```
"treatment": [
    {
        "type": "ACTIVITY",
        "operator": "EQUAL",
        "value": "Change application type"
    }
]
```

PrCore will use this information to check whether a case has the treatment, for the use of some casuality-based algorithms. Also, it will return the treatment information in the prescription result.

{{< /hint >}}

#### Request body example

This is an example of the request body. The `positive_outcome` is an array of arrays. Each array is a condition. The conditions are connected with `OR` operator. The conditions in each array are connected with `AND` operator. This example means that the positive outcome is when the activity is `A` and the duration is less than 100, or the activity is `B`.

The `treament` definition is similar to the `positive_outcome` definition.

```json
{
    "event_log_id": 123456,
    "positive_outcome": [
        [
            {
                "type": "ACTIVITY",
                "operator": "EQUAL",
                "value": "A",
            },
            {
                "type": "DUARTION",
                "operator": "LESS_THAN",
                "value": 100
            }
        ],
        [
            {
                "type": "ACTIVITY",
                "operator": "EQUAL",
                "value": "B"
            }
        ]
    ],
    "treatment": [
        [
            {
                "type": "ACTIVITY",
                "operator": "EQUAL",
                "value": "C"
            }
        ]
    ]
}
```

### Response

In the response, a `project_id` will be returned, which can be used to get the project information later.

{{< hint type=important icon=gdoc_info_outline >}}
Project details will also be returned in the response, when new API details is provided in future.

Like this:

```
{
    "message": "Project created successfully",
    "event_log_id": 123456,
    "project_id": 654321,
    "project": {
        "id": 654321,
        ...
        ...
    }
}
```

So you may want to use the `project.id` instead of `project_id` in the future.

Please not that the `project` in the response is the current newly created project status, the information may be changed if you get the project information later, as the project is still under training.
{{< /hint >}}

{{< tabs "definition-tab-id" >}}
{{< tab "Success" >}}
```json
{
    "message": "Project created successfully",
    "event_log_id": 123456,
    "project_id": 654321
}
```
{{< /tab >}}
{{< tab "Error" >}}
```json
{
    "message": "Project creation failed",
    "error": "Error message"
}
```
{{< /tab >}}
{{< /tabs >}}
