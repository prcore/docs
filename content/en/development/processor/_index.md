---
title: "Processor"
weight: 20
---

The transaction log processor is a component for processing transaction logs, which converts transaction logs into preprocessed datasets.

## Workflow

As shown in the figure below, the workflow is quite simple:

{{< mermaid class="text-center" >}}
sequenceDiagram
Core Application->>Log Processor: PROCESS_REQUEST
Log Processor-->>Core Application: PROCESS_RESULT
{{< /mermaid >}}

The log processor responds to the `PROCESS_REQUEST` request from the core application, then converts the transaction logs into preprocessed datasets, and finally returns the results to the core application.

## PROCESS_REQUEST

The request body is as follows:

```json
{
    "request_key": "random string",
    "df_name": "random.pkl",
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
        "case_attributes": ["Case ID", "AMOUNT_REQ"], 
        "fast_mode": true, 
        "start_transition": "START", 
        "complete_transition": "COMPLETE", 
        "abort_transition": "ATE_ABORT", 
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
        ]
    }
}
```

## PROCESS_RESULT

The response body is as follows:

```json
{
    "request_key": "f4DHYoVI", 
    "df_name": "liatMg7l.pkl", 
    "processed_df": "fLg0FkBF.pkl", 
    "used_time": 2.1
}
```
