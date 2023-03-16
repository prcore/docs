---
title: "Create Project"
toc: true
weight: 30
---

Following the aforementioned step of obtaining the unique activity count, along with the supported outcome and treatment options, the next course of action involves creating a new project while defining the desired outcome and treatment labels.

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
- `CATEGORICAL`
    - `IS`  

For each types of the definition, the corresponding values are described as below:

{{< tabs "definition-tab" >}}
{{< tab "TEXT" >}}
The value should be a string.

Examples:

- `"A"`
{{< /tab >}}
{{< tab "NUMBER" >}}
The value should be a number, or a number string.

Examples:

- `1`
- `2.2`
- `"1"`
- `"2.2"`
{{< /tab >}}
{{< tab "BOOLEAN" >}}
The value is not required.

If you provide a value, it will be ignored, since the operator is `IS_TRUE` or `IS_FALSE`.
{{< /tab >}}
{{< tab "DATETIME" >}}
The value should be a valid date time string, which conforms to the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard.

Examples: 

- `"2012-04-23T18:25:43.511Z"`
- `"2013-10-21T13:28:06.419Z"`
{{< /tab >}}
{{< tab "CATEGORICAL" >}}
The value should be a string.

So instead of `0`, you should use `"0"`, and instead of `1`, you should use `"1"`.
{{< /tab >}}
{{< tab "DURATION" >}}
The default unit is `second`, and the value should be a integer, or a integer string.

If you want to use other unit, you can use the following format: `value unit`.

Supported units and their abbreviations are:

- `month`: `months`, `month`, `mo`, `m`
- `week`: `weeks`, `week`, `wk`, `w`
- `day`: `days`, `day`, `d`
- `hour`: `hours`, `hour`, `hr`, `h`
- `minute`: `minutes`, `minute`, `min`, `m`
- `second`: `seconds`, `second`, `sec`, `s`

Examples:

- `22`
- `"123"`
- `"1 month"`
- `"2 weeks"`
- `"1 d"`
- `"2 hours"`
- `"3 min"`
- `"4 sec"`
{{< /tab >}}
{{< /tabs >}}

{{< hint type=note icon=gdoc_info_outline >}}
When the column field is filled with `DURATION` (uppercase), then the program will calculate the duration of each case if there is no duration data defined in the original event log.
{{< /hint >}}

For example, if you want to define the outcome as `Offer sent` activity happened, you can select `Action` column (the name is from your original event log), and select `EQUAL` as the operator, and choose `Offer sent` as the value. Since `Action` is defined as `ACTIVITY` in the previous step, PrCore will know it is an activity column, and based on the convention, the `ACTIVITY` (as `TEXT`) supports the `EQUAL` operator, so it is valid.

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

{{< hint type=important icon=gdoc_info_outline >}}
If the outcome/treatment label in a dataset contains only one class (i.e., all cases are either negative or positive), certain algorithms may not be compatible as they expect training data with two classes (1 and 0).

When utilizing the definition, PrCore will search for any event in a case that satisfies the condition. If a case meets the criteria, it will be counted as having a positive outcome/undergoing treatment. This means that certain definitions may result in all cases being classified as positive/negative.

If a dataset only contains one class for outcome or treatment, certain plugins may be marked as "ERROR" and will be ignored during the prescribing process. However, other plugins will continue to function normally, allowing the user to still obtain some results.
{{< /hint >}}

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
    ],
    "additional_info": {
        "plugin-causallift-resource-allocation": {
            "available_resources": ["Resource_A", "Resource_B", "Resource_C", "Resource_D", "Resource_E", "Resource_F", "Resource_G", "Resource_H", "Resource_I", "Resource_J", "Resource_K", "Resource_L", "Resource_M", "Resource_N", "Resource_O", "Resource_P", "Resource_Q", "Resource_R", "Resource_S", "Resource_T", "Resource_U", "Resource_V", "Resource_W", "Resource_X", "Resource_Y", "Resource_Z"],
            "treatment_duration": "1h"
        }
    }
}
```

## Response

In the response, a `project` object will be returned, which can be used later.

```json
{
    "message": "Project created successfully",
    "project": {
        "name": "bpic2012-CSV.zip",
        "description": null,
        "status": "PREPROCESSING",
        "id": 20,
        "created_at": "2023-03-04T09:26:36.572249+00:00",
        "updated_at": null,
        "error": null,
        "event_log": {
            "file_name": "bpic2012-CSV.zip",
            "id": 21,
            "created_at": "2023-03-04T08:56:29.577241+00:00",
            "updated_at": "2023-03-04T09:10:52.987641+00:00",
            "definition": {
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
                    "Case ID",
                    "AMOUNT_REQ"
                ],
                "outcome_definition": [
                    [
                        {
                            "column": "Activity",
                            "operator": "EQUAL",
                            "value": "A_APPROVED"
                        }
                    ]
                ],
                "treatment_definition": [
                    [
                        {
                            "column": "Activity",
                            "operator": "EQUAL",
                            "value": "O_SENT_BACK"
                        }
                    ]
                ],
                "fast_mode": true,
                "start_transition": "START",
                "complete_transition": "COMPLETE",
                "abort_transition": "ATE_ABORT",
                "id": 21,
                "created_at": "2023-03-04T09:10:52.970059+00:00",
                "updated_at": "2023-03-04T09:26:36.564989+00:00"
            }
        },
        "plugins": []
    },
    "result_key": null
}
```
