---
title: "Upload Event Log"
---

The first step is to upload the event log files via the API. Currently, the supported formats are standard XES files and CSV files.

We can use any tool or program to access the PrCore API. The following example assumes we are using [VisualPM](https://github.com/VisualPM) and presents the process for uploading files in a sequence diagram.

{{< mermaid class="text-center" >}}
sequenceDiagram
    VisualPM->>PrCore: Upload event log
    PrCore->>VisualPM: Returns first 20 events data with headers attached
    VisualPM->>PrCore: Submit columns renaming and definition
    PrCore->>VisualPM: Return the unique activities list, <br>supported outcome selections, <br>and supported treatment selections
    VisualPM->>PrCore: Submit outcome definition and treatment definition
    PrCore->>VisualPM: Event log confirmed, a new project created
{{< /mermaid >}}

Next, the details of each step will be explained.

---

## Uploading

### Request

{{< uploading-request >}}

### Response

Based on the event log file, the events attributes will be different, so here is just an example. The response will return the first 20 events data with headers and inferred types attached. The headers and types will be used to rename the columns and define type.

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

Since we have the first 20 events data, we can display them in a table, and let the user to rename the columns and define the type.

### Request

{{< columns-request >}}

### Response

{{< tabs "columns-response-tab-id" >}}
{{< tab "Success" >}}
```json
{
    "message": "Columns configuration updated successfully",
    "event_log_id": 123456,
    "activities": [
        "A",
        "B",
        "C"
    ],
    "outcome_types": [
        "TEXT",
        "NUMBER",
        "BOOLEAN",
        "TIMESTAMP",
        "ACTIVITY",
        "DURATION",
        "COST"
    ],
    "treatment_types": [
        "ACTIVITY"
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

After the previous step, we got unique activities list, and supported outcome and treatment types from backend, then we can define what is the positive outcome and what is the treatment.

Following outcome types has these predefined evaluation methods:

- `TEXT` (`ACTIVITY`)
    - `EQUAL`
    - `NOT_EQUAL`
    - `CONTAINS`
    - `NOT_CONTAINS`
- `NUMBER` (`TIMESTAMP`, `DURATION`, `COST`)
    - `EQUAL`
    - `NOT_EQUAL`
    - `GREATER_THAN`
    - `LESS_THAN`
    - `GREATER_THAN_OR_EQUAL`
    - `LESS_THAN_OR_EQUAL`
- `BOOLEAN`
    - `EQUAL`
    - `NOT_EQUAL`

Following treatment types has these predefined evaluation methods:

- `TEXT` (`ACTIVITY`)
    - `EQUAL`
    - `NOT_EQUAL`
    - `CONTAINS`
    - `NOT_CONTAINS`
- `NUMBER` (`TIMESTAMP`)
    - `EQUAL`
    - `NOT_EQUAL`
    - `GREATER_THAN`
    - `LESS_THAN`
    - `GREATER_THAN_OR_EQUAL`
    - `LESS_THAN_OR_EQUAL`
- `BOOLEAN`
    - `EQUAL`
    - `NOT_EQUAL`

### Request

{{< tabs "definition-request-tab-id" >}}
{{< tab "Endpoint" >}} **POST** `/project` {{< /tab >}}
{{< tab "Request body type" >}} json {{< /tab >}}
{{< tab "Example" >}}
This is an example of the request body. The `positive_outcome` is an array of arrays. Each array is a condition. The conditions are connected with `OR` operator. The conditions in each array are connected with `AND` operator. This example means that the positive outcome is when the activity is `A` and the duration is less than 100, or the activity is `B`.

The `treament` definition is similar to the `positive_outcome` definition.

```json
{
    "event_log_id": 123456,
    "positive_outcome": [
        [
            {
                "type": "ACTIVITY",
                "value": "A",
                "evaluation_method": "EQUAL"
            },
            {
                "type": "DUARTION",
                "value": 100,
                "evaluation_method": "LESS_THAN"
            }
        ],
        [
            {
                "type": "ACTIVITY",
                "value": "B",
                "evaluation_method": "EQUAL"
            }
        ]
    ],
    "treatment": [
        [
            {
                "type": "ACTIVITY",
                "value": "C",
                "evaluation_method": "EQUAL"
            }
        ]
    ]
}
```
{{< /tab >}}
{{< /tabs >}}



### Response

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
