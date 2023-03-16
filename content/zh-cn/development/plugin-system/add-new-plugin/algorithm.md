---
title: "关于算法文件"
weight: 20
---

We know that the `algorithm.py` file should have the following schema:

{{< include file="/static/plugin/algorithm.py" language="python" >}}

Now we will explain in detail.

## preprocess

The `preprocess` function is used to preprocess the training dataframe. PrCore will call this function when training data is available.

You can use `self.get_df()` to get the original training dataframe. The columns of the dataframe are renamed by PrCore.

The column name can be one of the following:

- `CASE_ID`
- `ACTIVITY`
- `TIMESTAMP`
- `START_TIMESTAMP`
- `END_TIMESTAMP`
- `RESOURCE`
- `DURATION`
- `COST`
- `OUTCOME`
- `TREATMENT`

If the column is not in the above list, but it is marked as case attribute, it will be renamed to `CASE_ATTRIBUTE_<data_type>_<attribute_name>`. For example, if the attribute name is `age`, the column name will be `CASE_ATTRIBUTE_NUMBER_age`.

The data type can be one of the following:

- `TEXT`
- `NUMBER`
- `BOOLEAN`
- `DATETIME`
- `CATEGORICAL`

If the column is not case attribute, it will be renamed to `EVENT_ATTRIBUTE_<data_type>_<attribute_name>`.

Having the above information, you can prepare the training data for your algorithm.

If you need to store any data for persistency, you can use `self.set_data_value(key, value)`. The `key` should be a string, and the `value` can be any type of data, but it should be serializable by `pickle`. The data will be stored after the algorithm is trained.

You can get the data by using `self.get_data()[key]`.

The expected output is a string. An empty string means that the algorithm is ready to be trained. If the string is not empty, PrCore will show the error message to the user.

## train

When `preprocess` is finished, PrCore will call the `train` function to train the algorithm. 

Please store your trained model by utilizing `self.set_data_value(key, value)`. For example, you can store the trained model by using `self.set_data_value("model", model)`.

PrCore will take care of persistency and load the data when needed. Follwing previous example, if you want to fetch the model, you can use `self.get_data()["model"]`.

The expected output is a string. An empty string means that the algorithm is ready to be used. If the string is not empty, PrCore will show the error message to the user.

## predict

When there is a need to predict a prefix, PrCore will call the `predict` function. 

The input is a list of dictionaries. Each dictionary contains the following schema:

```python
{
    "column_name": "value"
}
```

The `column_name` is the name of the attribute. The naming convention is the same as described the `preprocess` function. The list is ordered by the timestamp of the event.

The `predict` function should return a dictionary with the following schema:

```python
{
    "date": datetime.now().isoformat(),
    "type": self.get_basic_info()["prescription_type"],
    "output": "can be any json serializable data, can be null",
    "plugin": {
        "name": self.get_basic_info()["name"],
        "model": "Model name",
        "accuracy": 0.8
    }
}
```

The `date`, `type`, `output`, `plugin`, and `name` is required. You can add other fields to `plugin` if you want. It is recommended to add some metrics fields to `plugin` to help users to understand the performance of the plugin.

It is important to still return a dictionary even if the prediction is not available. In this case, you can set the `output` field to `null`, or you can use the `get_null_output` function to get a null output.

## predict_df

The `predict_df` function is used to predict a dataframe. The input is a dataframe with the same schema as the training dataframe. The output should be a dictionary, which contains the following schema:

```python
{
    "case_id_1": {
        "date": datetime.now().isoformat(),
        "type": self.get_basic_info()["prescription_type"],
        "output": "can be any json serializable data, can be null",
        "plugin": {
            "name": self.get_basic_info()["name"],
            "model": "Model name",
            "accuracy": 0.8
        }
    },
    "case_id_2": {
        "date": datetime.now().isoformat(),
        "type": self.get_basic_info()["prescription_type"],
        "output": "can be any json serializable data, can be null",
        "plugin": {
            "name": self.get_basic_info()["name"],
            "model": "Model name",
            "accuracy": 0.8
        }
    }
}
```

The key of the dictionary is the case id. The value is the same as the `predict` function's output.

It is important to still return a dictionary even if the prediction is not available. In this case, you can set the dictionary value to `{}` as an empty dictionary.
