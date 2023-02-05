---
title: "Example"
toc: true
weight: 30
---

Public API is available for testing and integration, and the base path is https://prcore.chaos.run

You can also use the [Swagger UI](https://prcore.chaos.run/docs) to test the API.

Currently, the server requires authentication, and the API key is required in the header of each request.

If you are using the [Swagger UI](https://prcore.chaos.run/docs), you can click the `Authorize` button on the top right corner, and enter the username and password fields.

| Username | Password |
| -------- | -------- |
| `Compile3667` | `42v@zbT$2jUp!X27` |

If you are using Postman, you can click the `Authorization` tab, select `Bearer Token` as the type, and enter the token in the `Token` field.

| Token |
| ----- |
| `UaJW0QvkMA1cVnOXB89E0NbLf3JRRoHwv2wWmaY5v=QYpaxr1UD9/FupeZ85sa2r` |

And if you are just calling the API, for example, using `curl` or using a frontend framework, you can add the header to the request.

| Header | Value |
| ------ | ----- |
| `Authorization` | `Bearer UaJW0QvkMA1cVnOXB89E0NbLf3JRRoHwv2wWmaY5v=QYpaxr1UD9/FupeZ85sa2r` |

---

Following we will show you how to use the API by using the [Postman](https://www.postman.com/).

## Prerequisites

- [Postman](https://www.postman.com/) installed
- [Download the example collection](/download/postman_collection.json) and import it to Postman
- [Download the example environment](/download/postman_environment.json) and import it to Postman
- [Download the example event log file (CSV)](/download/bpic2012-CSV.zip) and [download the example event log file (XES)](/download/bpic2012-XES.zip), both are from BPI Challenge 2012
- Extract the event log files

## Set the variables

After importing the collection and environment, you need to set the variables.

First, click the `PrCore` collection, and then click the `Variables` tab.

![](images/set-path.png)

Then, set the `server` as `https://prcore.chaos.run`.

## Upload event log

There is a request in the collection called `Upload event log`. This request will upload the event log file to the PrCore server, and the event log ID will be returned.

Navigate to the `Body` tab, select a file from the `file` field, and click `Send`.

![](images/upload-file.png)

## Submit column definitions

Another request in the collection called `Set columns definition`.

Navigate to the `Body` tab, modify the raw JSON data as you wish, and click `Send`.

![](images/columns-definition.png)

## Submit outcome and treatment definitions to create a new project

The last main request in this example is `Create a project`.

Please note that we need to use the event log ID returned from the previous request, so you need to activate the environment `PrCore` you imported before, then the event log ID will be automatically handled in the request, without the need to manually enter it.

![](images/create-project.png)
