FROM python:3.10.6
WORKDIR /code
COPY ./core /code/core
COPY ./plugins /code/plugins
RUN pip install --no-cache-dir -r plugins/foo_bar/requirements.txt
CMD ["python", "-m", "plugins.foo_bar.main"]
