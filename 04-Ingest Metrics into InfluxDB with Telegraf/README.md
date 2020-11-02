## Learning Objective

Let's set up Telegraf to collect metrics from a device.
You'll need to install the Telegraf agent and then perform some additional configuration to connect the agent to your InfluxDB service.
There are several different types of plugins supported by Telegraf: input, output, aggregator, and processor.
For now, we'll just use an input plugin to gather system metrics, and the `outputs.influxdb_v2` output plugin to write to InfluxDB v2.

### Installation of Telegraf

* Visit the [InfluxDB downloads page](https://portal.influxdata.com/downloads/)
* Run the download / extract / install command for your operating system
* There are two files in the Windows ZIP file: the executable and the config file
* Let's enable the InfluxDB v2 output plugin and explore the default input plugins
  * Create a new bucket in InfluxDB
  * Create an authentication token in InfluxDB
  * Configure the appropriate settings (bucket, organization, and InfluxDB URL)
* When you run Telegraf, you must specify the path to the configuration
  * Let's define the `TELEGRAF_CONFIG_PATH` environment variable

### Common Plugins for Telegraf

* CPU / disk / memory
* NVIDIA Systems Management Interface (SMI)
* Windows Performance Counters
* HTTP endpoints (think Prometheus exporter)
* HTTP response times (poller)