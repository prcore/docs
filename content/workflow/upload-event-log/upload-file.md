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

{{< hint type=note icon=gdoc_info_outline >}}
As you can see, the `test` field is optional. It represents a test dataset file. **The test file should only contain ongoing cases.** If the test file is uploaded, after you [created the project](../project-creation/) you will also receive a `result_key`, which can be used to [get the test results](../../get-prescriptions/get-dataset-result/).
{{< /hint >}}


## Response

Based on the event log file, the events attributes will be different, so here is just an example. The response will return the first 5 events data with headers and inferred definitions attached.

The first row of `events_head` is the column names, the second row is the inferred column definitions (some elements can be null), and the following rows are the events data.

```json
{
    "message": "Event log uploaded",
    "event_log_id": 21,
    "columns_header": [
        "Case ID",
        "start_time",
        "end_time",
        "AMOUNT_REQ",
        "REG_DATE",
        "Activity",
        "Resource"
    ],
    "columns_inferred_definition": [
        "CASE_ID",
        "START_TIMESTAMP",
        "END_TIMESTAMP",
        null,
        null,
        "ACTIVITY",
        "RESOURCE"
    ],
    "columns_data": [
        [
            "173688",
            "2011-09-30T22:38:44.546",
            "2011-09-30T22:38:44.546",
            "20000",
            "2011-09-30T22:38:44.546Z",
            "A_SUBMITTED",
            "112"
        ],
        [
            "173688",
            "2011-09-30T22:38:44.880",
            "2011-09-30T22:38:44.880",
            "20000",
            "2011-09-30T22:38:44.546Z",
            "A_PARTLYSUBMITTED",
            "112"
        ],
        [
            "173688",
            "2011-09-30T22:39:37.906",
            "2011-09-30T22:39:37.906",
            "20000",
            "2011-09-30T22:38:44.546Z",
            "A_PREACCEPTED",
            "112"
        ],
        [
            "173688",
            "2011-10-01T09:36:46.437",
            "2011-10-01T09:45:13.917",
            "20000",
            "2011-09-30T22:38:44.546Z",
            "W_Completeren aanvraag",
            "nan"
        ],
        [
            "173688",
            "2011-10-01T09:42:43.308",
            "2011-10-01T09:42:43.308",
            "20000",
            "2011-09-30T22:38:44.546Z",
            "A_ACCEPTED",
            "10862"
        ]
    ]
}
```
