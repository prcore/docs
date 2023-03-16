---
title: "Steps"
weight: 10
---

Here, we will simplify the usage process for better understanding. The process is divided into two steps: upload the event log and send new data.

## Step 1: Upload the event log

This event log file should only contains already completed cases. Together with the event log, the some definitions are needed: columns definition, case attributes, outcome definition, and treatment definition. Then the system will train the models for later use.

{{< mermaid class="text-center" >}}
flowchart LR
    log(Event log) --> project(Project)
    def(Definitions) --> project
    project --> model(Trained models)
{{< /mermaid >}}

## Step 2: Send new data

There are two ways to send new data to the system.

### Upload test dataset

You can upload a new dataset to get the results. The new dataset should only contains ongoing cases. The system will prescribe the results for these cases.

{{< mermaid class="text-center" >}}
flowchart LR
    log(New dataset) --> project(Project)
    project --> result(Results)
{{< /mermaid >}}

### Stream new events data

You also can let your business management system stream the new events data to PrCore. PrCore will process the new events data and provide prescription results after the data is processed.


{{< mermaid class="text-center" >}}
flowchart LR
    data(Stream data) -.-> project(Project)
    project -.-> result(Results)
{{< /mermaid >}}

## What's next

Now you have a basic understanding of the PrCore system. You can go to the [detailed steps](/getting-started/detailed-steps/) page to learn more about the usage process.
