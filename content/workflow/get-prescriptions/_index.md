---
title: "Get Prescriptions"
weight: 40
---

PrCore use [SSE](https://en.wikipedia.org/wiki/Server-sent_events) to stream prescriptions to the client. The SSE endpoint is `/project/{project_id}/streaming/result`. Below is an example script that connects to the SSE endpoint and prints the prescriptions. You can modify this script to fit your needs. Please note that you should to change the `PROJECT_ID` value to your project ID.

{{< hint type=note icon=gdoc_info_outline >}}
The status of the project should be `STREAMING` or `SIMULATING`, otherwise the SSE endpoint will return `400` error.
{{< /hint >}}

{{< hint type=warning icon=gdoc_info_outline >}}
If you are trying to read results from a project that is already being read by another client, the SSE endpoint will return `400` error. Since in design, the SSE endpoint is only for one client to read the results, you should not try to read the results from the same project from multiple clients.
{{< /hint >}}

{{< include file="/static/download/sse-client.py" language="python" >}}

Below is an example of the `event.data` object that is received from the SSE endpoint.

The `case_completed` is a boolean value that indicates whether the case is completed. If the case is completed, then the `prescriptions` array will be empty.

```json
[
    {
        "id": 12345,
        "timestamp": "2023-01-01 00:02:00",
        "case_completed": false,
        "data": {
            "case_id": "123",
            "activity": "ACTIVITY_3",
            "timestamp": "2023-01-01 00:01:00",
            "data_attribute_1": 1,
            "data_attribute_2": 2
        },
        "prescriptions": [
            {
                "id": 1213,
                "datetime": "2023-01-01 00:02:00",
                "type": "NEXT_ACTIVITY",
                "output": "ACTIVITY_4",
                "plugin": {
                    "name": "plugin_1",
                    "description": "plugin_1",
                    "accuracy": 0.9,
                    "precision": 0.9,
                    "recall": 0.9,
                    "precision": 0.9
                }
            }
        ]
    }
]
```
