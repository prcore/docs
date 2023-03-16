---
title: "输入数据流"
weight: 20
---

To ensure that the prescriptions are up to date and can be utilized by the process work in a timely manner, you also have the option to integrate this endpoint with your business process monitoring system's event stream. By doing so, you can call the endpoint and maintain a seamless flow of information between the two systems.

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
