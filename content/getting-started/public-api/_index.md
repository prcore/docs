---
title: "Public API"
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