---
title: "Upload Event Log"
geekdocCollapseSection: true
weight: 10
---

The first step is to upload the event log files via the API. Currently, the supported formats are standard XES files and CSV files.

We can use any tool or program to access the PrCore API. The following example assumes we are using a frontend app and presents the process for uploading files in a sequence diagram.

{{< mermaid class="text-center" >}}
sequenceDiagram
    Frontend->>PrCore: Upload event log
    PrCore-->>Frontend: Returns first 5 events data with headers attached
    Frontend->>PrCore: Submit column definitions
    PrCore-->>Frontend: Return the unique activities count, <br>supported outcome selections, <br>and supported treatment selections
    Frontend->>PrCore: Submit outcome definition and treatment definition
    PrCore-->>Frontend: Event log confirmed, a new project created
{{< /mermaid >}}

Please see the following sections for more details:

{{< toc-tree >}}
