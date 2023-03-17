---
title: PrCore 文档
geekdocNav: false
geekdocAlign: center
geekdocAnchor: false
---

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD033 -->

<span class="badge-placeholder">[![](https://img.shields.io/pingpong/status/sp_c60bb412baf14b219102581cecc9631f?style=flat)](https://prcore.pingpong.host/en/)</span>

<!-- markdownlint-restore -->x

PrCore是一个用于规范性过程监控的后端应用程序。它接收历史事件日志文件，并根据收到的事件流数据或新的事件日志数据集提供持续的案例处方。它具有灵活性，可应用于各种领域的事件日志。由于其插件机制，其建议和预测算法可以轻松修改、替换或添加。此外，其API易于使用，可集成到任何应用程序中。

{{< mermaid class="text-center" >}}
flowchart LR
    upload(Upload) --> train(Train) --> new(New Data) --> result(Prescriptions)
{{< /mermaid >}}

{{< button size="large" relref="getting-started/" >}}Getting Started{{< /button >}}
