## Learning Objective

There are a couple of major versions of InfluxDB right now. There's the 1.x branch and the 2.x release candidate.

In order to effectively work with InfluxDB, there are a few basic concepts to understand.

## Buckets

First of all, data in InfluxDB is categorized into "buckets."
Buckets can have separate retention policies assigned to them.

## Data Fields

Metrics are known as field keys and field values, and are stored with a timestamp.
Metrics can also have tags (key-value pairs) associated with them.

## InfluxDB Line Protocol

InfluxDB uses a ["line protocol"](https://docs.influxdata.com/influxdb/v2.0/reference/syntax/line-protocol/) to write data into the storage engine.
The line protocol includes a few important items:

* Measurement / metric value
* Field set
* Metric tags (_optional_)
* Timestamp (_optional_)

