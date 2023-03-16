---
title: "添加服务"
weight: 30
---

We need to create a new docker compose file called `docker-compose-custom.yml` in the root directory of PrCore. This file will be used to build and run the system.

```bash
cd prcore
cp docker-compose.yml docker-compose-custom.yml
```

Next, we need to add the following lines to the `services` section in `docker-compose-custom.yml` file:

```yaml
  plugin-foo-bar:
    build:
      context: .
      dockerfile: plugins/foo_bar/Dockerfile
    container_name: prcore-plugin-foo-bar
    depends_on:
      - core
    restart: always
    environment:
      APP_ID: "plugin-foo-bar"
      RABBITMQ_HOST: "rabbitmq"
      RABBITMQ_PORT: "5672"
      RABBITMQ_USER: ${RABBITMQ_USER}
      RABBITMQ_PASS: ${RABBITMQ_PASS}
    volumes:
      - ./data/event_logs:/code/data/event_logs
      - ./data/plugins:/code/data/plugins
      - ./data/tmp:/code/data/tmp
    networks:
      - prcore
```

Under the `core` service section, we need to modify the `ENABLED_PLUGINS` environment variable to include the new plugin. For example, if we want to enable the `plugin-foo-bar` plugin, we need to add `plugin-foo-bar` to the `ENABLED_PLUGINS` environment variable:

```
    environment:
      ENABLED_PLUGINS: "plugin-foo-bar || plugin-knn-next-activity || plugin-random-forest-alarm"
```

Please note that the added plugin must be separated by `||` from the other plugins, and the value comes from the `APP_ID` environment variable in the `plugin-foo-bar` service section.

That's it! Now we can build and run the system with the new plugin.
