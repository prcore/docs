---
title: "事务日志处理器"
weight: 20
---

事务日志处理器是一个用于处理事务日志的组件，它将事务日志转换为预处理数据集。

## 工作流程

如下图所示，其工作流程很简单

{{< mermaid class="text-center" >}}
sequenceDiagram
    核心应用->>日志处理器: PROCESS_REQUEST
    日志处理器-->>核心应用: PROCESS_RESULT 
{{< /mermaid >}}

日志处理器响应核心应用的 `PROCESS_REQUEST` 请求，然后将事务日志转换为预处理数据集，最后将结果返回给核心应用。

## PROCESS_REQUEST

请求体如下：

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

响应体如下：

```json
{
    "request_key": "f4DHYoVI", 
    "df_name": "liatMg7l.pkl", 
    "processed_df": "fLg0FkBF.pkl", 
    "used_time": 2.1
}
```
