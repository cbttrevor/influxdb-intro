## Learning Objective

It's easy to deploy InfluxDB as a standalone Docker container for development and small-medium scale usage.

### Helpful Tools

* [Docker Desktop](https://www.docker.com/products/docker-desktop)
* [Microsoft Visual Studio Code](https://code.visualstudio.com)

```
docker run --interactive --tty --publish 8086:8086 quay.io/influxdb/influxdb:2.0.0-rc
```

If this container image tag changes, be sure to reference the [InfluxDB documentation](https://docs.influxdata.com/influxdb/v2.0/get-started/) for the current version.

Once you have InfluxDB running in a container, you'll need to ingest some data.
The **Client Libraries** section shows you the supported integrations with programming languages.
The **Telegraf Plugins** section displays the supported integrations with other software products and cloud services, such as Amazon Elastic Container Service (ECS) or Elasticsearch.

You can also "install" InfluxDB by downloading the pre-built binaries from the [GitHub releases page]().