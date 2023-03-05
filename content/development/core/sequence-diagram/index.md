---
title: "Sequence Diagram"
weight: 30
resources:
  - name: "diagram"
    src: "images/sequence-diagram.png"
    title: "Sequence Diagram"
---

This diagram depicts the interactions between clients and the PrCore API. The workflow assumes that the user will first use a new test dataset to obtain all prescriptions in one call. Subsequently, the user will use the streaming API to post new events and receive new prescriptions in a streaming manner.

{{< img name="diagram" size="origin" lazy=false >}}
