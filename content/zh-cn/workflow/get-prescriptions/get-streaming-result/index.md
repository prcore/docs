---
title: "流数据结果"
weight: 20
resources:
  - name: "postman"
    src: "images/streaming-collection.png"
    title: "Postman Collection"
---

PrCore employs [SSE](https://en.wikipedia.org/wiki/Server-sent_events) to stream prescriptions to the client in a timely manner. For SSE, you can check [here](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) for more information.

{{< hint type=note icon=gdoc_info_outline >}}
The status of the project should be `STREAMING` or `SIMULATING`, otherwise the SSE endpoint will return `400` error.
{{< /hint >}}

{{< hint type=warning icon=gdoc_info_outline >}}
If the user attempts to read results from a project that is already being read by another client, the SSE endpoint will return a `400` error. As it is specifically designed to read results from only one client at a time, it is not advisable to attempt to read results from the **same project** using multiple clients.
{{< /hint >}}

## Request

Please note that the SSE endpoint is not a REST endpoint. It is a persistent connection endpoint. You should use a client that supports SSE to connect to the endpoint.

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| GET | `/project/{project_id}/stream/result` | `none` | Get event stream of the prescriptions |

## Response

A message will be sent to the client every time a new prescription is available. The message will be in the following format:

```
event: message
id: 1234
data: []
```

The `data` field is a list containing prescriptions. The format of the prescription is described in the [following](#example-prescriptions) section.

Also, when connection is established, the client will receive a message with the following format:

```
event: notification
id: 0
data: CONNECTED
```

After the simulation is stopped, the client will receive a message with the following format:

```
event: notification
id: 54321
data: FINISHED
```

The program will also send `ping` messages to the client every 15 seconds:

```
event: ping
id: 12345
data: 2023-03-05 06:04:54.698763
```

## Test with Postman

If the user's Postman version is v10 or higher, they may utilize the following collection to test the SSE endpoint. Since Postman has altered the method for testing SSE, additional information on this topic can be found [here](https://blog.postman.com/support-for-server-sent-events/).

{{< stream-postman >}}

Below is a GIF that shows the prescriptions SSE endpoint being tested with Postman:

{{< sse-gif >}}

## Example client script

Here is a sample script that connects to the PrCore SSE endpoint and outputs the prescriptions. This script can be customized to meet the user's specific requirements. It is important to note that the `PROJECT_ID` value should be replaced with the actual project ID.

{{< include file="/static/download/sse-client.py" language="python" >}}

To run this script, please install the `sseclient` package first.

```bash
python3 -m venv ./venv
./venv/bin/python -m pip install requests sseclient-py
./venv/bin/python sse-client.py
```

## Example prescriptions

The following is an example of the `event.data` object that is received from the SSE endpoint.

The `case_completed` attribute is a boolean value that indicates whether or not the case has been completed. If the case is complete, the `prescriptions` array will be empty.

It is worth noting that event.data is a list, which implies that it may contain multiple events, particularly when the user is connecting to the SSE endpoint for the first time, as there may be some events already in the queue.

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
