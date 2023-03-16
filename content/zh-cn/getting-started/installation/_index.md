---
title: "本地安装"
weight: 60
---

If you want to install PrCore on your local machine, please make sure you have the following requirements installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

Then, you can follow **three easy steps** to install PrCore:

1. Clone the PrCore repository:
    ```bash
    git clone https://github.com/prcore/prcore.git
    ```
2. Create a `.env` file from the `example.env` file in the root directory of the repository:
    ```bash
    cp example.env .env
    vim .env  # Edit the .env file
    ```
3. Run the following command to install PrCore:
    ```bash
    cd scripts
    bash install.sh
    ```

After the installation is complete, you can access PrCore at `localhost` with the port `API_PORT` you set in the `.env` file.
