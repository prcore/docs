---
title: "上传数据集"
weight: 10
---

When the project's status is `TRAINED`, you can upload a new test dataset to the project.

{{< hint type=note icon=gdoc_info_outline >}}
The test dataset should only contain ongoing cases.

If you already uploaded a test dataset together with the historical event log, you can skip this step. Because you will receive a `result_key` when you [created the project](/workflow/upload-event-log/project-creation/).
{{< /hint >}}


## Request

File upload is a `multipart/form-data` request, and the file should be attached to the `file` field.

### General information

| Method | Endpoint | Request body type | Description |
| ------ | -------- | ----------------- | ----------- |
| POST | `/project/{project_id}/result` | `form-data` | Upload event log |

### Request body porperties

{{< propertylist name=new-dataset-request >}}

## Response

The system will validate the dataset. If everything is fine, the response will be:

```json
{
    "message": "Ongoing dataset uploaded successfully",
    "project_id": 20,
    "result_key": "ZJPKGGby"
}
```

Since the processing of the dataset may take a while, the response will not contain the result, but a `result_key`.

The `result_key` will be used in the [Get Dataset Result](/workflow/get-prescriptions/get-dataset-result/) API.
