---
title: "Files"
weight: 10
---

The basic file structure of PrCore's code is as follows: 

```
prcore/
├─ core/
├─ plugins/
│  ├─ common/
│  ├─ causallift_treatment_effect/
│  ├─ knn_next_activity/
│  ├─ random_forest_alarm/
├─ simulation/
├─ .env
├─ docker-compose.yml
```

The `plugins` directory contains all the plugins.

To add a new plugin, create a new directory in the `plugins` directory. For example, if you want to add a plugin called `foo_bar`, create a directory called `foo_bar` in the `plugins` directory:

```
plugins/
├─ common/
├─ causallift_treatment_effect/
├─ random_forest_alarm/
├─ foo_bar/
```

Next, create the following files in the `foo_bar` directory:

```
foo_bar/
├─ __init__.py
├─ algorithm.py
├─ config.py
├─ Dockerfile
├─ main.py
├─ requirements.txt
```

## \_\_init\_\_.py

Just create an empty file called `__init__.py` in the `foo_bar` directory.

## algorithm.py

This file contains the algorithm that the plugin will use to make predictions. For example, we can create an algorithm `FooBarAlgorithm` as follows:

{{< include file="/static/plugin/algorithm.py" language="python" >}}

The input and expected output  of these functions are described in the [Algorithm](/development/plugin-system/add-new-plugin/algorithm) section.

## config.py

This file contains the configuration of the plugin. For example, we can create a configuration file as follows:

{{< include file="/static/plugin/config.py" language="python" >}}

Here you can change the name of the plugin, the description, the prescription type, and the parameters that the plugin will use. The prescription type can be any string.

The `needed_columns` variable is a list of the columns that the plugin needs to make prescriptions. The elements should be selected from the following list:

- `ColumnDefinition.OUTCOME`
- `ColumnDefinition.TREATMENT`
- `ColumnDefinition.TREATMENT_RESOURCE`

If you fill in other values, your plugin may not be generically usable. But you can still use it if your data contains the columns that you specified.

## Dockerfile

It is used to build the Docker image of the plugin. For example, we can create a Dockerfile as follows:

{{< include file="/static/plugin/Dockerfile" language="dockerfile" >}}

## main.py

This is the entry point of the plugin. For example, we can create a main file as follows:

{{< include file="/static/plugin/main.py" language="python" >}}

## requirements.txt

Since each plugin will be run in a Docker container, you need to specify the dependencies of the plugin in the `requirements.txt` file.
