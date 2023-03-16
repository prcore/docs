---
title: "详细步骤"
weight: 20
---

本节将通过一个假设的使用案例详细介绍 PrCore 的工作流，同时介绍了 PrCore 所具有的主要功能。

假设您手头有已经有一个在某领域内的业务事件日志文件，其中只包含已经完成的案例。这份文件可以是 CSV 格式，也可以是 XES 格式。您的这份业务事件日志可以是来自于您的业务管理系统，也可以是来自于其他的数据源。PrCore 可以通过这份日志文件来训练模型，从而为您正在进行的案例提供预测结果以及多种建议。

首先，您可以通过 [Upload Event Log](/zh-cn/workflow/upload-event-log/) 一节中介绍的方法，将您的这份文件上传到 PrCore 中，接着，利用 [Columns Definition](/workflow/upload-event-log/columns-definition/) 提供的 API，来告诉 PrCore 您日志文件中每个 column 的含义。最后，您可以通过 [Create Project](/workflow/upload-event-log/project-creation/) 介绍的方法，告诉 PrCore 符合哪些条件的 case 是成功的 case、符合预期的 case，而根据您的业务领域，哪些行为和事件是可以作为一个改善 case 所可以尝试的 treatment。PrCore 会根据您的 event log file 和这些附加信息，创建一个 project，然后自动开始训练模型。

