---
title: "Add New Plugin"
geekdocCollapseSection: true
weight: 10
---

The process of adding a new plugin to the PrCore system is straightforward and highly customizable. The system is designed to be extensible, allowing users to easily integrate new plugins to enhance its functionality.

Here are the steps to add a new plugin to the PrCore system:

1. Create a new folder for the plugin in the `plugins` directory.
2. Create nessary files for the plugin.
3. Modify the algorithm file, implement the `preprocess`, `train`, `predict`, and `predict_df` functions.
4. Add service section in the `docker-compose-custom.yml` file.
5. Rebuild the docker container.

That's it! You've successfully added a new plugin to the PrCore system.

You can find more details about each step below.

{{< toc-tree >}}
