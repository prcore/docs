---
title: "Upload file"
weight: 10
---

Uploaded event log files will be stored in the PrCore server, and the event log ID will be returned. The event log ID will be used in the following steps.

## Request

File upload is a `multipart/form-data` request, and the file should be attached to the `file` field.

### General information

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| POST | `/event_log` | `form-data` | Upload event log |

### Request body porperties

{{< propertylist name=uploading-request >}}

## Response

Based on the event log file, the events attributes will be different, so here is just an example. The response will return the first 5 events data with headers and inferred definitions attached.

The first row of `events_head` is the column names, the second row is the inferred column definitions (some elements can be null), and the following rows are the events data.

```json
{
    "message": "Event log uploaded successfully",
    "event_log_id": 123456,
    "columns_header": ["Case_ID", "Time", "Action", "Personnel"],
    "columns_inferred_definition": ["CASE_ID", "TIMESTAMP", "ACTIVITY", null],
    "columns_data": [
        ["1", "2019-01-01 00:00:00", "A", "1"],
        ["1", "2019-01-01 00:00:00", "B", "1"],
        ["1", "2019-01-01 00:00:00", "C", "2"],
        ["1", "2019-01-01 00:00:00", "C", "2"],
        ["1", "2019-01-01 00:00:00", "C", "2"]
    ]
}
```
