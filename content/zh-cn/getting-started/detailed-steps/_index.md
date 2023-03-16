---
title: "详细步骤"
weight: 20
---

本节将通过一个假设的使用案例详细介绍 PrCore 的工作流，同时介绍了 PrCore 所具有的主要功能。

假设您手头有已经有一个在某领域内的业务事件日志文件，其中应**只包含已经完成的案例**。您的这份业务事件日志可以是来自于您的业务管理系统，也可以是其他的数据源。文件格式支持 CSV 和 XES。PrCore 可以通过这份日志文件来训练模型，从而为您正在进行的案例提供预测结果以及多种建议。

首先，您需要使用 [上传文件]({{< relref "../../workflow/upload-event-log/upload-file.md" >}}) 一节中介绍的方法，将您的这份文件上传到 PrCore 中。接着，利用 [提供列定义]({{< relref "../../workflow/upload-event-log/columns-definition.md" >}}) 一节中描述的 API，来告诉 PrCore 您日志文件中每个列的含义。最后，您可以通过 [创建项目]({{< relref "../../workflow/upload-event-log/project-creation.md" >}}) 中介绍的方法，告诉 PrCore 符合哪些条件的案例是成功的、符合预期的，而根据您的业务领域，哪些行为和事件是可以作为一个改善案例所可以尝试的干预行为。PrCore 会根据您的事务日志文件和这些信息，创建一个项目，然后自动开始训练模型。

PrCore 可以接入多个插件，每个插件是一个独立的容器，负责提供某种类型的预测或建议。因此，在创建项目时，您可以按照 [设定参数]({{< relref "../../advanced-usage/plugin-operations/set-parameters.md" >}}) 一节的说明指定插件的参数，这将调整插件训练的模型的效果。PrCore 也允许您提供任意的附加信息，这些附加信息可用于插件的训练和预测阶段（如果插件支持识别这些信息），此功能尤其对自行开发的插件有用，因为非默认插件可能需要更多信息以支持工作。关于详情，您可以参考 [提供附加信息]({{< relref "../../advanced-usage/plugin-operations/update-additional-info.md" >}}) 一节。同时，如果您在创建项目后，需要禁用某些插件，以令其在您提供新数据时，不提供任何建议和预测，则请参考 [禁用或启用插件]({{< relref "../../advanced-usage/plugin-operations/disable-or-enable.md" >}}) 一节进行操作。

在项目创建完毕后，您可以通过 [检查项目状态]({{< relref "../../workflow/project-operations/check-project-status.md" >}}) 一节介绍的 API 来获取当前项目信息和状态、所含插件状态，您可以由此获知项目是否处理完毕数据或训练完毕模型。与此同时，您可以通过 [修改基础信息]({{< relref "../../workflow/project-operations/update-basic-information.md" >}}) 的 API 来更改项目的名称、描述，这将帮助您识别和区分具体项目。您还可以通过 [获取所有项目]({{< relref "../../workflow/project-operations/get-projects.md" >}}) 的 API 来以分页的方式查看所有项目信息。

当项目完成训练后，您如果有更改任何列定义或结果定义的需求，还可以通过 [重新提供定义]({{< relref "../../advanced-usage/project-operations/_index.md" >}}) 一节介绍的方法进行重定义，此时项目将根据修改的信息被重新训练，而您无需再次上传任何事务日志。如果您需要保留所有设置的参数和提供的附加信息，但想要重新上传一份新的日志文件，您可以通过 [重新上传日志]({{< relref "../../advanced-usage/event-log-operations/re-upload-file.md" >}}) 中的 API 进行操作。除此之外，如果您想删除该项目，可在 [删除项目]({{< relref "../../workflow/project-operations/delete-project.md" >}}) 一节中找到相应的 API 介绍。

由于项目已训练完毕，此时您可以向 PrCore 提交新的数据来让其对正在进行中的案例给出预测和建议。您有两种选择方案，第一种方案是按照 [上传数据集]({{< relref "../../workflow/send-new-data/upload-new-dataset/_index.md" >}}) 一节的说明上传新的数据集，此数据集中**只能包含正在进行中、尚未结束**的案例，然后再按照 [新数据集结果]({{< relref "../../workflow/get-prescriptions/get-dataset-result.md" >}}) 一节中的 API 获取对该数据集的分析结果；第二种方案则是当您有新的事件数据时，向 [输入数据流]({{< relref "../../advanced-usage/stream-new-events/stream-data.md" >}}) 的 API 发送新事件，您可以整合您的业务管理系统向此 API 持续发送数据，并可以在 [流数据结果]({{< relref "../../workflow/get-prescriptions/get-streaming-result/_index.md" >}}) 一节中介绍的方法获得基于 SSE 的结果数据流。如果您尚未整合业务管理系统，或尚未编写自动发送数据的测试脚本，您可以通过 [模拟数据流]({{< relref "../../workflow/send-new-data/simulate-streaming/_index.md" >}}) 中的方法来让 PrCore 为您自动模拟对流数据的接收，此时，您可以在 [流数据结果]({{< relref "../../workflow/get-prescriptions/get-streaming-result/_index.md" >}}) 的 API 中直接获取结果来测试该功能，而无需进行额外的编程。

至此，您已进行了工作流中的主要操作，并获取了相应结果。

如果您对 PrCore 是如何根据您提供的信息处理和标记您提供的数据集感兴趣的话，您可以通过 [下载数据集]({{< relref "../../advanced-usage/download-datasets/_index.md" >}}) 一节中介绍的 API，来获取 PrCore 预处理过后的数据。同时您还能够下载原始文件、仅包含正在进行中案例的测试文件，以及在 PrCore 模拟流数据时使用到的数据集。这些可以帮助您检查标记和处理是否达到您的预期、以及为您对自定义插件的开发工作提供更多信息。

PrCore 的特点之一是可以支持插件的整合：PrCore 提供了一种简单易用的插件系统，让您可以自行基于某种算法添加给出某种建议或预测的插件。您可以查看 [开发]({{< relref "../../development/_index.md" >}}) 一节的内容来了解更多关于核心应用、插件开发的细节。 
