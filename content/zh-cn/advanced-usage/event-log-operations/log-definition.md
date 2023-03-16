---
title: "关于日志定义"
weight: 20
---

When setting the columns definition for the event log, there are other fields besides `columns_definition` and `case_attributes` that can be included in the request body.

The purpose of these fields is explained below.

Typically, when uploading an XES file as an event log, PrCore assumes that it conforms to the [Standard lifecycle transition model](https://www.tf-pm.org/resources/xes-standard/about-xes/standard-extensions/lifecycle/standard).

As PrCore requires identification of a timestamp for each event, it will utilize transition and timestamp information to extract it.

## Identify the timestamp for each event

Initially, PrCore will check if all rows in the event log lack a `start_transition`. If they do not contain a `start_transition`, PrCore will use the timestamp of the row that has a `complete_transition` as the timestamp for each event. Alternatively, if there is no `complete_transition` present in the event log, PrCore will use the `start_transition` to identify the timestamp for each event.

If both `start_transition` and `complete_transition` are absent in the event log, PrCore will preserve the timestamp of the row as is, and therefore, all rows will remain unmerged.

## If fast_mode is true

If both `start_transition` and `complete_transition` are present in the event log, PrCore will utilize the `complete_transition` and `abort_transition` to identify the timestamp for each event.

This mode is enabled by default, and it is recommended to use this mode if you are uncertain which mode to utilize.

## If fast_mode is false

If both `start_transition` and `complete_transition` are present in the event log, PrCore will use the `start_transition` to identify the start timestamp for each event, and use the `complete_transition` to identify the end timestamp for each event. As such, two timestamps will be obtained for each event.

It is important to note that the non-fast mode may take a long time to process based on the size of the event log. If the event log is too large, PrCore may not allow you to set the `fast_mode` to `false`. In this instance, it is recommended to preprocess the event log to obtain the timestamp for each event and convert the file to CSV before the uploading, or, simply use the fast mode.

## Redefine the transition

However, there are instances where the XES file does not comply with the lifecycle standard, or your business domain has specific requirements. In such cases, you can redefine the `start_transition`, `complete_transition`, and `abort_transition` to suit your needs.

Supported values are:

- `ASSIGN`
- `ATE_ABORT`
- `AUTOSKIP`
- `COMPLETE`
- `MANUALSKIP`
- `PI_ABORT`
- `REASSIGN`
- `RESUME`
- `SCHEDULE`
- `START`
- `SUSPEND`
- `UNKNOWN`
- `WITHDRAW`
- `IGNORE`: Ignore this transition and do not utilize it to identify the timestamp for each event.

So, if you prefer not to use `abort_transition` in fast mode, you can set the `abort_transition` to `IGNORE`.
