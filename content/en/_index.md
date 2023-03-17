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

PrCore is a backend application used for prescriptive process monitoring. It takes historical event log files and provides ongoing case prescriptions based on the received event streaming data or new event log dataset. It is flexible and can be applied to event logs in various domains. Its prescribing and predicting algorithms can be easily modified, replaced, or added due to its plugin mechanism. Moreover, its API is easy to use and can be integrated into any application.

{{< mermaid class="text-center" >}}
flowchart LR
    upload(Upload) --> train(Train) --> new(New Data) --> result(Prescriptions)
{{< /mermaid >}}

{{< button size="large" relref="getting-started/" >}}Getting Started{{< /button >}}
