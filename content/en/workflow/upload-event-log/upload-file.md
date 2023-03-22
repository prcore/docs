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
Notably, it is important to recognize that the `test` field is an optional attribute which represents a test dataset file. However, it should be noted that the test file should only include ongoing cases.

Should the user choose to upload the test file after [created the project](../project-creation/), they will receive a `result_key` which can then be utilized to [retrieve the test results](/workflow/get-prescriptions/get-dataset-result/).
{{< /hint >}}


## Response

Since the event log file can have varying event attributes, the following is just an example. Once the API processes the request, the response will include the first 5 events data along with their respective headers and inferred definitions. Please note if the event log file is not used to create a project, this uploaded event log will be deleted by the system regularly every day.

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
