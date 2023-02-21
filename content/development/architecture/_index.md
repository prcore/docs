---
title: "Architecture"
weight: -10
---

{{< mermaid class="text-center" >}}
flowchart LR
    database[(Database)] --- core(Core)
    core --- message_broker((Message<br/>broker))
    message_broker --- plugin1(Plugin 1)
    message_broker --- plugin2(Plugin 2)
    message_broker --- plugin3(Plugin 3)
{{< /mermaid >}}
