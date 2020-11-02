from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

influxcfg = {
    'url': 'http://localhost:8086',
    'bucket': 'cbtdata',
    'token': 'M-F2VyIHlZ_f5NiHQXK1CdvPwXGR5BDVrB32HRGuBqBGMTh-n0ibQthO0r5c2LgB6z0_OsAXlnaRTv_Z1wu1zw==',
    'org': 'trevor'
}

influx = InfluxDBClient(url=influxcfg['url'], token=influxcfg['token'])

writer = influx.write_api(write_options=SYNCHRONOUS)

writer.write(influxcfg['bucket'], influxcfg['org'], 'bacon strips=50')