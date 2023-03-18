---
title: "架构"
weight: -10
---

PrCore 由几个主要组件组成：核心应用、processor，插件，数据库，和消息代理。

核心应用负责协调整个系统的工作流程。核心应用主要负责和 processor 合作进行事务日志的预处理、提供 API 给外部应用，将必要数据存储到数据库中，以及通过消息代理与插件进行通信，提供插件所需要的数据，并处理插件返回的结果。核心应用的部分组件同时也作为插件的通用代码库，供插件使用，以便自动处理一些通用的任务，降低插件的开发难度，使插件开发者可以只专注插件的算法实现。

Processor 是一个独立的组件，负责处理事务日志文件，将其转换为可供插件使用的数据格式。其利用了多进程的方式来有效地利用多核 CPU，提高处理效率。

插件则是独立的模块，负责为正在进行的事务提供一种特定类型的处方。

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
