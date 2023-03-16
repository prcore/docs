---
title: "Online status update"
weight: 10
---

The core will send a request to the plugin to update the online status of the plugin. The plugin will respond with the updated status.

{{< mermaid class="text-center" >}}
sequenceDiagram
    loop Every 5 mintues
        Core->>Plugin: ONLINE_INQUIRY
        Plugin-->>Core: ONLINE_REPORT
    end
{{< /mermaid >}}

### ONLINE_INQUIRY

The core will send this request when it starts, and periodically. The request data's body is empty.

```
{}
```

### ONLINE_REPORT

The plugin will send the basic information of the plugin, such as the name, type, and description. For example:

```json
{
    "id": "example-plugin",
    "name": "Example Plugin",
    "type": "EXAMPLE",
    "description": "This is an example plugin",
    "parameters": {
        "param1": "value1",
        "param2": "value2"
    }
}
```
