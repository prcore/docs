---
title: Welcome to the documentation
geekdocNav: false
geekdocAlign: center
geekdocAnchor: false
---

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD033 -->

<span class="badge-placeholder">[![](https://img.shields.io/github/actions/workflow/status/prcore/prcore/main.yml?label=Docker%20compose%20service)](https://github.com/prcore/prcore/actions/workflows/main.yml)</span> <span class="badge-placeholder">[![](https://img.shields.io/website?label=API%20service&url=https%3A%2F%2Fprcore.chaos.run%2Fdocs)](https://prcore.chaos.run)</span>

<span class="badge-placeholder">[![](https://img.shields.io/codefactor/grade/github/prcore/prcore/main?label=Code%20quality)](https://www.codefactor.io/repository/github/prcore/prcore/overview/main)</span> <span class="badge-placeholder">[![](https://img.shields.io/github/license/prcore/prcore?color=blue&label=License)](LICENSE)</span>

<!-- markdownlint-restore -->

PrCore is a backend application used for prescriptive process monitoring. It takes historical event log files and provides ongoing case prescriptions based on the received event streaming data or new event log dataset. It is flexible and can be applied to event logs in various domains. Its prescribing and predicting algorithms can be easily modified, replaced, or added due to its plugin mechanism. Moreover, its API is easy to use and can be integrated into any application.

{{< mermaid class="text-center" >}}
flowchart LR
    upload(Upload) --> train(Train) --> new(New Data) --> result(Prescriptions)
{{< /mermaid >}}

{{< button size="large" relref="getting-started/" >}}Getting Started{{< /button >}}
