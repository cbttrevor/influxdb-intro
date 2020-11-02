## Learning Objective

Let's start by discussing why we might want to deploy and use InfluxDB.

### Types of Database Engines

There are database systems that store data in various formats, depending on how the data will be consumed.
Relational databases are excellent for storing large quantities of rows of tabular data, such as customer or product information.
Document databases are useful for storing complete data records that are independently useful.
Graph databases, such as [Neo4j](https://neo4j.com/) or [RedisGraph](https://redislabs.com/blog/new-redisgraph-1-0-achieves-600x-faster-performance-graph-databases/) are useful for data with relationships.
Knox Hutchinson developed a CBT Nuggets skill that discusses the different types of database engines in more depth.

### Why Use a Time-Series Database Engine?

One of the most common examples for IT people includes monitoring systems: CPU, memory, disk, network I/O.
You can also use IoT devices and sensors to track metrics surrounding the physical environment such as temperature, humidity, wind speed, noise and water levels.
I've actually [built an integration with a solar charge controller](https://trevorsullivan.net/2020/10/22/capture-and-analyze-solar-power-generation-metrics-with-influxdb/) to track metrics surrounding solar panel power generation and monitor my battery backup system.

- **Example**: If you work in a factory environment, noise levels might be important to you.
- **Example**: If you're responsible for monitoring conditions inside a mine, you might want to keep track of earthquake activity and air cleanliness.

The more data you have, the more proactive you can be with your decision-making process.

### Related Industry Tools

* Prometheus for metrics storage
* Grafana for visualization
* Google Data Studio for data visualization
* InfluxDB CLI tool - useful, but not recommended

### What You'll Learn

* Basic concepts behind InfluxDB data storage
* Setting up InfluxDB
* Ingesting metrics using the Telegraf agent
* Ingest metrics using Python programming language
* Query data from InfluxDB using the Flux language
* Configure alerts and notifications in InfluxDB
