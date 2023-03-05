---
title: "Stream Data"
weight: 20
---

It is recommended to call this endpoint by integrating it with your business process monitoring system's event stream. This way, you can ensure that the data is up to date.

## Request

You should only call this endpoint when the project's status is `STREAMING`.

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| POST | `/event/{project_id}` | `json` | Post new event to project |

Expample of the request body:

```json
{
    "Case ID": "{{randomString}}",
    "start_time": "2011-09-30T22:38:44.546",
    "end_time": "2011-09-30T22:38:44.546",
    "AMOUNT_REQ": "20000",
    "REG_DATE": "2011-09-30T22:38:44.546Z",
    "Activity": "A_SUBMITTED",
    "Resource": "112",
    "COMPLETE_INDICATOR": false
}
```

The request body keys correspond to the event attributes, with their respective values matching the attribute values, as shown above. The `COMPLETE_INDICATOR` attribute is utilized to specify whether the event is the last event in the case. If this attribute is not included, it will be assumed to be `false`.

## Response

```json
{
    "message": "Event received successfully",
    "event": {
        "project_id": 7,
        "attributes": {
            "CASE_ID": "HXQLYpqJTGGFLJCxUvVD",
            "ACTIVITY": "A_SUBMITTED",
            "CASE_ATTRIBUTE_DATETIME_REG_DATE": "2011-09-30T22:38:44.546Z",
            "RESOURCE": "112",
            "END_TIMESTAMP": "2011-09-30T22:38:44.546",
            "CASE_ATTRIBUTE_NUMBER_AMOUNT_REQ": "20000",
            "START_TIMESTAMP": "2011-09-30T22:38:44.546",
            "COMPLETE_INDICATOR": "False"
        },
        "id": 156,
        "created_at": "2023-03-05T15:44:13.921972+00:00",
        "updated_at": null
    }
}
```

After you post a new event, the event will be processed by the system. You can get the prescriptions of the event by calling the [Get Streaming Result](/workflow/get-prescriptions/get-streaming-result/) endpoint.
