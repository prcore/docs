---
title: "架构"
weight: -10
---

The core functionality of the application encompasses several tasks, including preprocessing of the event log, establishment of API endpoints, interfacing with the database, and facilitating communication between plugins via a message broker. The plugins, on the other hand, are self-contained modules that perform a specific type of prescription for ongoing cases.

{{< mermaid class="text-center" >}}
flowchart LR
    api[API] --- core
    database[(Database)] --- core((Core<br/>Application))
    core --- message_broker(Message<br/>broker)
    processor(Dataset processor) --- message_broker
    message_broker --- plugin1(Plugin 1)
    message_broker --- plugin2(Plugin 2)
    message_broker --- plugin3(Plugin 3)
{{< /mermaid >}}

At present, the backend workflow has been implemented in its entirety, and three distinct plugins have been developed to extend the application's capabilities. The first plugin is responsible for predicting the next activity in the ongoing case, while the second plugin assesses the likelihood of negative outcomes. The third plugin, in turn, provides a score that indicates the need for intervention.
