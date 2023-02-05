---
title: "Upload Event Log"
---

The first step is to upload the event log files via the API. Currently, the supported formats are standard XES files and CSV files.

We can use any tool or program to access the PrCore API. The following example assumes we are using [VisualPM](https://github.com/VisualPM) and presents the process for uploading files in a sequence diagram.

{{< mermaid class="text-center" >}}
sequenceDiagram
    VisualPM->>PrCore: Upload event log
    PrCore->>VisualPM: Returns first 5 events data with headers attached
    VisualPM->>PrCore: Submit column definitions
    PrCore->>VisualPM: Return the unique activities count, <br>supported outcome selections, <br>and supported treatment selections
    VisualPM->>PrCore: Submit outcome definition and treatment definition
    PrCore->>VisualPM: Event log confirmed, a new project created
{{< /mermaid >}}
