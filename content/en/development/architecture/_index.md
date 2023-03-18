---
title: "Architecture"
weight: -10
---

PrCore consists of several main components: core application, processor, plugins, database, and message broker.

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

The core application is responsible for coordinating the workflow of the entire system. The core application mainly collaborates with the processor to preprocess transaction logs, provide APIs to external applications, store necessary data in the database, communicate with plugins through the message broker, provide data required by plugins, and process the results returned by plugins. Some components of the core application also serve as a common code library for plugins, which can be used by plugins to automatically handle some common tasks, reduce the difficulty of plugin development, and allow plugin developers to focus solely on implementing the plugin algorithm.

The processor is an independent worker that is responsible for processing transaction log files and converting them into data formats that can be used by plugins. It utilizes a multi-process approach to effectively use multi-core CPUs and improve processing efficiency.

Plugins are independent modules that are responsible for providing a specific type of prescription for ongoing transactions.

At present, the backend workflow has been implemented in its entirety, and four distinct plugins have been developed to extend the application's capabilities. The first plugin is responsible for predicting the next activity in the ongoing case, while the second plugin assesses the likelihood of negative outcomes. The third plugin provides a score that indicates the need for intervention. The fourth plugin, in turn, allocates resources based on the gains of the ongoing case.
