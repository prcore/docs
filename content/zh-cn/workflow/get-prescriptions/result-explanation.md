---
title: "结果解释"
weight: 30
---

PrCore has three default plugins. Here we explain the prescription output schema.

## Fields

The prescription is a JSON object with the following fields:

- `date`: The timestamp of the prescription.
- `type`: The type of the prescription. Can be one of the following:
    - `NEXT_ACTIVITY`: Predicts the next activity of a case.
    - `ALARM`: Provides the probability of a negative outcome.
    - `TREATMENT_EFFECT`: Provides the treatment effect of a case.
    - `RESOURCE_ALLOCATION`: Provides the resource allocation recommendation of a case.
    - Others, depending on the plugins installed.
- `output` field is different for each plugin, and can be `null` if the plugin is not able to make a prediction.
- `plugin` is an object with the following fields:
    - `name`: The name of the plugin.
    - `model`: The name of the model used by the plugin.
    - `accuracy`, `precision`, `recall`, `f1_score`: Some plugins will return the evaluation metrics of the model.
    - Others, depending on the plugins installed.

## NEXT_ACTIVITY

This plugin predicts the next activity of a case. The output is a string, which is the name of the next activity.

```json
{
    "date": "2023-03-04T12:31:53.670496",
    "type": "NEXT_ACTIVITY",
    "output": "A_ACTIVATED",
    "plugin": {
        "name": "KNN next activity prediction",
        "model": "count-encoding",
        "accuracy": 0.8446,
        "precision": 0.8523,
        "recall": 0.8446,
        "f1_score": 0.8414
    }
}
```

## ALARM

The output is the probability of a negative outcome.

```json
{
    "date": "2023-03-04T12:31:53.626402",
    "type": "ALARM",
    "output": 0.364,
    "plugin": {
        "name": "Random forest negative outcome probability",
        "model": "count-encoding",
        "accuracy": 0.5472,
        "precision": 0.5491,
        "recall": 0.5472,
        "f1_score": 0.5481
    }
}
```

## TREATMENT_EFFECT

The output is an object with the following fields:

- `proba_if_treated`: The probability of a positive outcome if the case is treated.
- `proba_if_untreated`: The probability of a positive outcome if the case is not treated.
- `cate`: The Conditional Average Treatment Effect (CATE) score of the case.
- `treatment`: The treatment definition of the case. This is directly from the user's previously inputted treatment definition.

```json
{
    "date": "2023-03-04T12:31:54.638476",
    "type": "TREATMENT_EFFECT",
    "output": {
        "proba_if_treated": 0.6827,
        "proba_if_untreated": 0.0001,
        "cate": 0.6826,
        "treatment": [
            [
                {
                    "value": "O_SENT_BACK",
                    "column": "Activity",
                    "operator": "EQUAL"
                }
            ]
        ]
    },
    "plugin": {
        "name": "CasualLift treatment effect",
        "model": "count-encoding"
    }
}
```

## RESOURCE_ALLOCATION

The output is an object with the following fields:

- `resource`: The allocated resource.
- `allocated_until`: The timestamp until which the resource will be released.

```json
{
    "date": "2023-03-15T12:49:17.742267",
    "type": "RESOURCE_ALLOCATION",
    "output": {
        "cate": 0.6478,
        "resource": "Resource_B",
        "allocated_until": "2023-03-15T13:49:17.742254"
    },
    "plugin": {
        "name": "CasualLift resource allocation",
        "model": "SIMPLE_INDEX-length-3"
    }
}
```
