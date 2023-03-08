---
title: "Error reporting"
weight: 40
---


In the event of the plugin encountering an error, the error message will be promptly relayed to the core. Subsequently, the core will proceed to update the status of the plugin to reflect the `ERROR` status, with the error message being attached to the plugin. This implies that the plugin will be rendered unusable unless certain project definitions are modified by the user. In the event that all plugins have been marked with the ERROR status, the core will designate the entire project as being in an error state, necessitating intervention by the user.

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
