---
title: "启用新插件"
weight: 40
---

To enable the plugin, we need to build and run the system with the new plugin.

First, we need to stop the system:

```bash
cd prcore
docker compose down
```

Then, build and run new system:

```bash
docker compose -f docker-compose-custom.yml build
docker compose -f docker-compose-custom.yml up -d
```

Congratulations! Now the system is running with the new plugin. 
