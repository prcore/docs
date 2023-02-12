---
title: "Get Prescriptions"
weight: 40
---

This section will be updated soon.

```json
{
    "project_id": 123,
    "data": {
        "id": 12345,
        "timestamp": "2023-01-01 00:02:00",
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
}
```