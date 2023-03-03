---
title: "Error reporting"
weight: 40
---


If the plugin encounters an error, it will send the error message to the core. The core will then mark the plugin's status as the error message. If all plugins are in the error status, the core will mark the project as the error status.

{{< mermaid class="text-center" >}}
sequenceDiagram
    Plugin-)Core: ERROR_REPORT
{{< /mermaid >}}

### ERROR_REPORT

The error message will include the detail field.

```json
{
    "project_id": 123,
    "plugin_id": 345,
    "detail": "error message"
}
```
