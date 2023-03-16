---
title: "下载数据集"
geekdocCollapseSection: true
weight: 20
---

PrCore generates datasets for training, testing, and simulation based on the uploaded file. Once the project has been created or pre-processed, the user can download these datasets. These datasets can also help developers to comprehend the datasets at different stages.

## Original Dataset

After the project has been created, the uploaded file can be downloaded by the user.

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/project/{project_id}/dataset/original` | Download the original file uploaded before |

## Processed Dataset

After the project has been pre-processed, the processed file can be downloaded by the user.

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/project/{project_id}/dataset/processed` | Download the processed file |

## Ongoing Dataset

Upon completion of the pre-processing stage, PrCore can assist the user in generating datasets that solely contain ongoing cases. These cases are derived from the simulation dataset and, therefore, do not include the cases utilized for training purposes. It is important to note that the generated dataset may vary and is produced upon request.

The ongoing dataset can be utilized as new data in order to obtain test results.

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/project/{project_id}/dataset/ongoing` | Download the ongoing dataset |

## Simluation Dataset

After the project has been pre-processed, the simulation dataset can be downloaded by the user.

This simulation dataset will be used to automatically simulate streaming data by PrCore.

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/project/{project_id}/dataset/simulation` | Download the simulation dataset |
