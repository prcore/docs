---
title: "Getting Started"
weight: 10
---

{{< hint type=note icon=gdoc_info_outline >}}
Please note that PrCore is currently in its initial development phase. The API may change in the future.
{{< /hint >}}

## Resources

The [Workflow](../../workflow) section is the primary way to get started with PrCore. It outlines a series of steps you can take to create a project, simulate it, and analyze the results. We also provide a [straightforward example](/workflow/workflow-example/) of how to use PrCore.

For more detailed information on the endpoints, please refer to the [API Reference](https://prcore.chaos.run/docs).

The [Advanced Usage](../../advanced-usage) section provides additional information on the endpoints and how to utilize them.

If you're interested in PrCore's development or would like to expand its functionality, please visit the [Development](../../development) section.

---

## Public API

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

## Postman Collection

Following we will show you how to use the API by using the [Postman](https://www.postman.com/). Before you start, please make sure you have the following resources:

- [Postman](https://www.postman.com/) installed
- [Download the example collection](/download/postman_collection.json) and import it to Postman
- [Download the example environment](/download/postman_environment.json) and import it to Postman
- [Download the example event log file (CSV)](/download/bpic2012-CSV.zip) and [download the example event log file (XES)](/download/bpic2012-XES.zip), both are from BPI Challenge 2012

## Test with Postman

After importing the collection and environment, you need to set the variables.

First, click the `PrCore` collection, and then click the `Variables` tab.

![](images/set-path.png)

Then, set the `server` as `https://prcore.chaos.run`.

{{< toc-tree >}}
