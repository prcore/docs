---
title: "上传事件日志"
geekdocCollapseSection: true
weight: 10
---

To initiate the process, the first step involves uploading the event log files via the API. It is important to note that currently, the supported formats are standard XES files and CSV files. Moreover, ZIP files containing a single XES or CSV file are also compatible. However, it is recommended to utilize the ZIP file format since it is smaller in size and thus faster to upload.

As for accessing the PrCore API, there are various tools and programs that can be used. Assuming a frontend application is being used, the subsequent sequence diagram presents a step-by-step process for uploading the files.

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
