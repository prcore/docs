---
title: "Ongoing Dataset Example"
weight: 10
---

Here you can find a Python script that automatically handles the uploading of training data and test data files, defining the project, and getting the results.

{{< mermaid class="text-center" >}}
flowchart TB
    upload(Upload the event log file and test log) --> set(Set the columns definition)
    set --> create(Create the project)
    create --> get(Get the result)
{{< /mermaid >}}

## Prerequisites

Before you start, make sure you have the following packages installed:

```bash
python3 -m venv ./venv
./venv/bin/pip install requests
```

## Example script

You can also download the script from [here](/download/workflow-example-dataset.py).

According to the script, uploaded event log should be [this one](/download/bpic2012-CSV.zip), and the test event log should be [this one](/download/bpic2012-ongoing-CSV.zip), unless you manually modify the columns definition, etc. The latter one only contains ongoing cases.

Please change the `EVENT_LOG_FILE` to get the correct path to your local event log file.

{{< hint type=warning icon=gdoc_info_outline >}}
The `outcome` and `treatment` of the project defined in exmaple script is only for demonstration purposes. They don't represent the actual outcome and treatment of the domain, so you can modify them to fit your needs.
{{< /hint >}}

{{< include file="/static/download/workflow-example-dataset.py" language="python" >}}

## Running the script

To run the script, simply execute the following command:

```bash
./venv/bin/python workflow-example.py
```

## Example output

Here is an snippet of the output of the script:

```
Staring the client...

Uploading the event log file...
Event log 34 has been uploaded!

Setting the columns definition...
The columns definition has been set!

Creating the project...
Project 27 has been created!

Getting the project status...

[001] - Now the project status is PREPROCESSING
[002] - Now the project status is PREPROCESSING
[003] - Now the project status is PREPROCESSING
[004] - Now the project status is PREPROCESSING
[005] - Now the project status is PREPROCESSING
[006] - Now the project status is PREPROCESSING
[007] - Now the project status is PREPROCESSING
[008] - Now the project status is PREPROCESSING
[009] - Now the project status is PREPROCESSING
[010] - Now the project status is PREPROCESSING
[011] - Now the project status is PREPROCESSING
[012] - Now the project status is PREPROCESSING
[013] - Now the project status is PREPROCESSING
[014] - Now the project status is PREPROCESSING
[015] - Now the project status is PREPROCESSING
[016] - Now the project status is WAITING
[017] - Now the project status is PREPROCESSING
[018] - Now the project status is PREPROCESSING
[019] - Now the project status is PREPROCESSING
[020] - Now the project status is PREPROCESSING
[021] - Now the project status is PREPROCESSING
[022] - Now the project status is PREPROCESSING
[023] - Now the project status is PREPROCESSING
[024] - Now the project status is PREPROCESSING
[025] - Now the project status is PREPROCESSING
[026] - Now the project status is PREPROCESSING
[027] - Now the project status is PREPROCESSING
[028] - Now the project status is PREPROCESSING
[029] - Now the project status is PREPROCESSING
[030] - Now the project status is PREPROCESSING
[031] - Now the project status is PREPROCESSING
[032] - Now the project status is PREPROCESSING
[033] - Now the project status is PREPROCESSING
[034] - Now the project status is PREPROCESSING
[035] - Now the project status is PREPROCESSING
[036] - Now the project status is TRAINING
[037] - Now the project status is TRAINING
[038] - Now the project status is TRAINING
[039] - Now the project status is TRAINING
[040] - Now the project status is TRAINING
[041] - Now the project status is TRAINING
[042] - Now the project status is TRAINING
[043] - Now the project status is TRAINED
[044] - Now the project status is TRAINED
[045] - Now the project status is TRAINED
[046] - Now the project status is TRAINED
[047] - We have got results from plugin-random-forest-alarm, 
and we are still waiting for plugin-causallift-treatment-effect, plugin-knn-next-activity.
[048] - We have got results from plugin-random-forest-alarm, plugin-knn-next-activity, 
and we are still waiting for plugin-causallift-treatment-effect.

We have got all results!

Here is the first case:

{'events': [['173688',
             '2011-09-30 22:38:44.546',
             '2011-09-30 22:38:44.546',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'A_SUBMITTED',
             '112'],
            ['173688',
             '2011-09-30 22:38:44.880',
             '2011-09-30 22:38:44.880',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'A_PARTLYSUBMITTED',
             '112'],
            ['173688',
             '2011-09-30 22:39:37.906',
             '2011-09-30 22:39:37.906',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'A_PREACCEPTED',
             '112'],
            ['173688',
             '2011-10-01 09:36:46.437',
             '2011-10-01 09:45:13.917',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'W_Completeren aanvraag',
             'nan'],
            ['173688',
             '2011-10-01 09:42:43.308',
             '2011-10-01 09:42:43.308',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'A_ACCEPTED',
             '10862'],
            ['173688',
             '2011-10-01 09:45:09.243',
             '2011-10-01 09:45:09.243',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'O_SELECTED',
             '10862'],
            ['173688',
             '2011-10-01 09:45:09.243',
             '2011-10-01 09:45:09.243',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'A_FINALIZED',
             '10862'],
            ['173688',
             '2011-10-01 09:45:11.197',
             '2011-10-01 09:45:11.197',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'O_CREATED',
             '10862'],
            ['173688',
             '2011-10-01 09:45:11.380',
             '2011-10-01 09:45:11.380',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'O_SENT',
             '10862'],
            ['173688',
             '2011-10-01 10:15:41.290',
             '2011-10-01 10:17:08.924',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'W_Nabellen offertes',
             'nan'],
            ['173688',
             '2011-10-08 14:26:57.720',
             '2011-10-08 14:32:00.886',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'W_Nabellen offertes',
             '10913'],
            ['173688',
             '2011-10-10 09:32:22.495',
             '2011-10-10 09:33:05.791',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'W_Nabellen offertes',
             '11049'],
            ['173688',
             '2011-10-10 09:33:03.668',
             '2011-10-10 09:33:03.668',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'O_SENT_BACK',
             '11049'],
            ['173688',
             '2011-10-13 08:05:26.925',
             '2011-10-13 08:37:37.026',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'W_Valideren aanvraag',
             '10629'],
            ['173688',
             '2011-10-13 08:37:29.226',
             '2011-10-13 08:37:29.226',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'A_REGISTERED',
             '10629'],
            ['173688',
             '2011-10-13 08:37:29.226',
             '2011-10-13 08:37:29.226',
             '20000',
             '2011-09-30T22:38:44.546Z',
             'A_APPROVED',
             '10629']],
 'prescriptions': [{'date': '2023-03-04T17:10:48.137653',
                    'output': 0.5606,
                    'plugin': {'accuracy': 0.5409,
                               'f1_score': 0.5284,
                               'model': 'count-encoding',
                               'name': 'Random forest negative outcome '
                                       'probability',
                               'precision': 0.5241,
                               'recall': 0.5409},
                    'type': 'ALARM'},
                   {'date': '2023-03-04T17:10:48.391516',
                    'output': 'A_ACTIVATED',
                    'plugin': {'accuracy': 0.8495,
                               'f1_score': 0.8461,
                               'model': 'count-encoding',
                               'name': 'KNN next activity prediction',
                               'precision': 0.8534,
                               'recall': 0.8495},
                    'type': 'NEXT_ACTIVITY'},
                   {'date': '2023-03-04T17:10:50.202392',
                    'output': {'cate': 0.6826,
                               'proba_if_treated': 0.6827,
                               'proba_if_untreated': 0.0001,
                               'treatment': [[{'column': 'Activity',
                                               'operator': 'EQUAL',
                                               'value': 'O_SENT_BACK'}]]},
                    'plugin': {'model': 'count-encoding',
                               'name': 'CasualLift treatment effect'},
                    'type': 'TREATMENT_EFFECT'}]}
Done!
```