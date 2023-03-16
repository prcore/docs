---
title: "通过模拟数据流"
geekdocCollapseSection: true
weight: 20
---

Once a project's status is marked as `TRAINED`, it becomes capable of receiving a continuous flow of new event data through its [stream data](/advanced-usage/stream-new-events/) API. This feature can be leveraged by business process management systems that generate events in real-time. By utilizing the stream data API, such systems can send new events to the project and receive prescription results promptly.

However, in the absence of such a system, PrCore offers the option to simulate stream data to the project. This obviates the need to set up a system for testing purposes. It is worth noting that PrCore uses 80% of the dataset to train and validate models, while the remaining 20% is reserved for simulating stream data.

It should be noted that the percentage referred to in this context is calculated based on the number of cases, rather than the number of events. As such, there is no need to be concerned that the split dataset will contain any incomplete cases.

For further information, please refer to the sections outlined in the following table of contents:

{{< toc-tree >}}
