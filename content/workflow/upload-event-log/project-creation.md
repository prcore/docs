---
title: "Create Project"
toc: true
weight: 30
---

After the previous step, we got unique activities count, and supported outcome and treatment selections from PrCore, then we can create a new project **by defining the outcome and treatment**.

## Request

This endpoint is for creating a new project, and the definition of outcome and treatment is required.

### General information

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| POST | `/project` | `json` | Outcome and treatment definition, resulting a created project |

### Request body porperties

{{< propertylist name=definition-request >}}

### Explanation

Following column definitions supports these predefined evaluation operators for outcome and treatment evaluation:

- `TEXT` (also for `ACTIVITY` and `RESOURCE`)
    - `EQUAL`
    - `NOT_EQUAL`
    - `CONTAINS`
    - `NOT_CONTAINS`
- `NUMBER` (also for `DURATION` and `COST`)
    - `EQUAL`
    - `NOT_EQUAL`
    - `LESS_THAN`
    - `LESS_THAN_OR_EQUAL`
    - `GREATER_THAN`
    - `GREATER_THAN_OR_EQUAL`
- `BOOLEAN`
    - `IS_TRUE`
    - `IS_FALSE`
- `DATETIME` (also for `TIMESTAMP`, `START_TIMESTAMP`, and `END_TIMESTAMP`)
    - `EQUAL`
    - `NOT_EQUAL`
    - `EARLIER_THAN`
    - `EARLIER_THAN_OR_EQUAL`
    - `LATER_THAN`
    - `LATER_THAN_OR_EQUAL`

For example, if you want to define the outcome as `Offer sent` activity happened, you can select `Action` column (the name is from your original event log), and select `EQUAL` as the operator, and choose `Offer sent` as the value. Since `Action` is defined as `ACTIVITY` in the previous step, PrCore will know it is an activity column, and based on the convention, the `ACTIVITY` (as `TEXT`) supports the `EQUAL` operator, so it is valid.

{{< hint type=note icon=gdoc_info_outline title="Special case" >}}
1. When the column field is filled with `DURATION` (uppercase), then the program will calculate the duration of each case if there is no duration data defined in the original event log.
2. When the definition of the selected column is `BOOLEAN`, then the value field can be ignored if the operator is `IS_TRUE` or `IS_FALSE`.
{{< /hint >}}

```
"positive_outcome": [
    {
        "column": "Action",
        "operator": "EQUAL",
        "value": "Offer sent"
    }
]
```

PrCore will evaluate the event log, and find out whether the `Offer sent` activity happened in any event, if it happened, then it knows the event's belonging case has positive outcome, otherwise, it has negative outcome. PrCore will use this information to train the model.

Regarding treatment, for example, if you want to define the treatment as `Change application type` activity happened, you can select column `Action`, and select `EQUAL` as the operator, and choose `Change application type` as the value.

```
"treatment": [
    {
        "column": "Action",
        "operator": "EQUAL",
        "value": "Change application type"
    }
]
```

PrCore will use this information to check whether a case has the treatment, for the use of some casuality-based algorithms. Also, it will return the treatment information in the prescription result.

### Request body example

This is an example of the request body. The `positive_outcome` is an array of arrays. Each array is a condition. The conditions are connected with `OR` operator. The conditions in each array are connected with `AND` operator. This example means that the positive outcome is when the activity is `A` and the duration is less than 100, or the activity is `B`.

The `treament` definition is similar to the `positive_outcome` definition.

```json
{
    "event_log_id": 123456,
    "positive_outcome": [
        [
            {
                "column": "Action",
                "operator": "EQUAL",
                "value": "A",
            },
            {
                "column": "DUARTION",
                "operator": "LESS_THAN",
                "value": 100
            }
        ],
        [
            {
                "column": "Personnel",
                "operator": "EQUAL",
                "value": "B"
            }
        ]
    ],
    "treatment": [
        [
            {
                "column": "Action",
                "operator": "EQUAL",
                "value": "C"
            }
        ]
    ]
}
```

## Response

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
