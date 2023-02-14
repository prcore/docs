---
title: "Workflow Example"
weight: 50
---

Here you can find a Python script that automatically handles the uploading of data, defining the project, triggering the simulation, and getting the results.

## Prerequisites

Before you start, make sure you have the following packages installed:

```bash
python3 -m venv venv
./venv/bin/pip install requests sseclient
```

## Example script

You can also download the script from [here](/download/workflow-example.py).

According to the script, uploaded event log should be [this one](/download/bpic2012-CSV.zip), unless you manually modify the columns definition, etc.

Please change the `EVENT_LOG_FILE` to get the correct path to your local event log file.

{{< include file="/static/download/workflow-example.py" language="python" >}}

## Example output

Here is an snippet of the output of the script:

```
Staring the client...

Uploading the event log file...
Event log 17 has been uploaded!

Setting the columns definition...
The columns definition has been set!

Creating the project...
Project 16 has been created!

Getting the project status...
Now the project status is PREPROCESSING. Waiting for 5 seconds...
Now the project status is PREPROCESSING. Waiting for 5 seconds...
Now the project status is PREPROCESSING. Waiting for 5 seconds...
Now the project status is PREPROCESSING. Waiting for 5 seconds...
Now the project status is PREPROCESSING. It's plugins have status PREPROCESSING, PREPROCESSING, TRAINED. Waiting for 5 seconds...
Now the project status is PREPROCESSING. It's plugins have status PREPROCESSING, PREPROCESSING, TRAINED. Waiting for 5 seconds...
Now the project status is PREPROCESSING. It's plugins have status PREPROCESSING, TRAINED, TRAINED. Waiting for 5 seconds...
Now the project status is PREPROCESSING. It's plugins have status PREPROCESSING, TRAINED, TRAINED. Waiting for 5 seconds...
Now the project status is TRAINING. It's plugins have status TRAINING, TRAINED, TRAINED. Waiting for 5 seconds...
Now the project status is TRAINING. It's plugins have status TRAINING, TRAINED, TRAINED. Waiting for 5 seconds...
The project has been trained!

Starting the simulation...
The simulation has been started!

Now we are going to get the streaming response...
Waiting for events...
Received message: NEW_RESULT
ID: 365
[{'date': '2023-02-14T10:03:25.053610',
  'output': 'W_Completeren aanvraag',
  'plugin': {'accuracy': 0.5669,
             'f1_score': 0.5115,
             'model': 3,
             'name': 'KNN next activity prediction',
             'precision': 0.936,
             'recall': 0.5669},
  'type': 'NEXT_ACTIVITY'},
 {'date': '2023-02-14T10:03:25.064882',
  'output': 0.6355,
  'plugin': {'accuracy': 0.6527,
             'f1_score': 0.5155,
             'model': 3,
             'name': 'Random forest negative outcome probability',
             'precision': 0.7733,
             'recall': 0.6527},
  'type': 'ALARM'},
 {'date': '2023-02-14T10:03:25.682665',
  'output': {'cate': 0.6872,
             'proba_if_treated': 0.6873,
             'proba_if_untreated': 0.0001,
             'treatment': [[{'column': 'Activity', 'operator': 'EQUAL', 'value': 'O_SENT_BACK'}]]},
  'plugin': {'model': 3, 'name': 'CasualLift treatment effect'},
  'type': 'TREATMENT_EFFECT'}]
------------------------
Received message: NEW_RESULT
ID: 371
[{'date': '2023-02-14T10:03:55.610696',
  'output': 'W_Afhandelen leads',
  'plugin': {'accuracy': 0.5669,
             'f1_score': 0.5115,
             'model': 3,
             'name': 'KNN next activity prediction',
             'precision': 0.936,
             'recall': 0.5669},
  'type': 'NEXT_ACTIVITY'},
 {'date': '2023-02-14T10:03:55.622616',
  'output': 0.6406,
  'plugin': {'accuracy': 0.6527,
             'f1_score': 0.5155,
             'model': 3,
             'name': 'Random forest negative outcome probability',
             'precision': 0.7733,
             'recall': 0.6527},
  'type': 'ALARM'},
 {'date': '2023-02-14T10:03:56.230732',
  'output': {'cate': 0.6828,
             'proba_if_treated': 0.6829,
             'proba_if_untreated': 0.0001,
             'treatment': [[{'column': 'Activity', 'operator': 'EQUAL', 'value': 'O_SENT_BACK'}]]},
  'plugin': {'model': 3, 'name': 'CasualLift treatment effect'},
  'type': 'TREATMENT_EFFECT'}]
------------------------
Received message: NEW_RESULT
ID: 372
[{'date': '2023-02-14T10:04:00.686650',
  'output': 'W_Completeren aanvraag',
  'plugin': {'accuracy': 0.6769,
             'f1_score': 0.555,
             'model': 4,
             'name': 'KNN next activity prediction',
             'precision': 0.782,
             'recall': 0.6769},
  'type': 'NEXT_ACTIVITY'},
 {'date': '2023-02-14T10:04:00.700571',
  'output': 0.6455,
  'plugin': {'accuracy': 0.6468,
             'f1_score': 0.5081,
             'model': 4,
             'name': 'Random forest negative outcome probability',
             'precision': 0.7716,
             'recall': 0.6468},
  'type': 'ALARM'},
 {'date': '2023-02-14T10:04:01.397980',
  'output': {'cate': 0.679,
             'proba_if_treated': 0.6791,
             'proba_if_untreated': 0.0001,
             'treatment': [[{'column': 'Activity', 'operator': 'EQUAL', 'value': 'O_SENT_BACK'}]]},
  'plugin': {'model': 4, 'name': 'CasualLift treatment effect'},
  'type': 'TREATMENT_EFFECT'}]
------------------------
Received message: NEW_RESULT
ID: 373
[{'date': '2023-02-14T10:04:05.760306',
  'output': 'W_Completeren aanvraag',
  'plugin': {'accuracy': 0.6769,
             'f1_score': 0.555,
             'model': 4,
             'name': 'KNN next activity prediction',
             'precision': 0.782,
             'recall': 0.6769},
  'type': 'NEXT_ACTIVITY'},
 {'date': '2023-02-14T10:04:05.771450',
  'output': 0.63,
  'plugin': {'accuracy': 0.6468,
             'f1_score': 0.5081,
             'model': 4,
             'name': 'Random forest negative outcome probability',
             'precision': 0.7716,
             'recall': 0.6468},
  'type': 'ALARM'},
 {'date': '2023-02-14T10:04:06.475218',
  'output': {'cate': 0.6873,
             'proba_if_treated': 0.6874,
             'proba_if_untreated': 0.0001,
             'treatment': [[{'column': 'Activity', 'operator': 'EQUAL', 'value': 'O_SENT_BACK'}]]},
  'plugin': {'model': 4, 'name': 'CasualLift treatment effect'},
  'type': 'TREATMENT_EFFECT'}]
------------------------
Interrupted by user

Done!
```
