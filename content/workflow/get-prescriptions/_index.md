---
title: "Get Prescriptions"
weight: 40
---

PrCore use [SSE](https://en.wikipedia.org/wiki/Server-sent_events) to stream prescriptions to the client. The SSE endpoint is `/project/{project_id}/streaming/result`.

{{< hint type=note icon=gdoc_info_outline >}}
The status of the project should be `STREAMING` or `SIMULATING`, otherwise the SSE endpoint will return `400` error.
{{< /hint >}}

{{< hint type=warning icon=gdoc_info_outline >}}
If you try to read results from a project that is already being read by another client, the SSE endpoint will return a `400` error. Since it is designed to read results from only one client, you should not try to read results from the **same project** with multiple clients.
{{< /hint >}}

## Example client script

Below is an example script that connects to the PrCore SSE endpoint and prints the prescriptions. You can modify this script to suit your needs. Note that you should change the `PROJECT_ID` value to your project ID.

{{< include file="/static/download/sse-client.py" language="python" >}}

To run this script, please install the `sseclient` package first.

```bash
python3 -m venv venv
./venv/bin/python -m pip install sseclient requests
./venv/bin/python sse-client.py
```

## Example prescriptions

Below is an example of the `event.data' object received from the SSE endpoint.

The `case_completed` is a boolean value indicating whether the case is complete. If the case is completed, then the `prescriptions` array will be empty.

Note that this is a list, which means it can contain multiple events, especially when you're connecting to the SSE endpoint for the first time, as there may be some events already in the queue.

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

For SSE, you can check [here](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) for more information.
