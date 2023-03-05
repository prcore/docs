---
title: Welcome to the documentation
geekdocNav: false
geekdocAlign: center
geekdocAnchor: false
---

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD033 -->

<span class="badge-placeholder">[![](https://img.shields.io/pingpong/status/sp_c60bb412baf14b219102581cecc9631f?style=flat)](https://prcore.pingpong.host/en/)</span>

<!-- markdownlint-restore -->

PrCore is a backend application used for prescriptive process monitoring. It takes historical event log files and provides ongoing case prescriptions based on the received event streaming data. It is flexible and can be applied to event logs in various domains. Its prescribing and predicting algorithms can be easily modified, replaced, or added due to its plugin mechanism. The system is designed to be scalable and can be deployed in a distributed environment. Try it out!

{{< mermaid class="text-center" >}}
flowchart LR
    upload(Upload) --> train(Train) --> new(New Data) --> result(Prescriptions)
{{< /mermaid >}}

{{< button size="large" relref="getting-started/" >}}Getting Started{{< /button >}}
