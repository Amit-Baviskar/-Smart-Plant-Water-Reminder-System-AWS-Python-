import boto3
import json
import time

# AWS setup
kinesis_client = boto3.client('kinesis', region_name='ap-south-1')
stream_name = 'plant-sensor-stream'

sensor_value = 100

while sensor_value >= 0:
    sensor_data = {
        'sensor_id': 'plant-1',
        'timestamp': int(time.time()),
        'value': sensor_value
    }

    print(f"Sending sensor data: {sensor_data}")

    kinesis_client.put_record(
        StreamName=stream_name,
        Data=json.dumps(sensor_data),
        PartitionKey="partition-key"
    )

    sensor_value -= 1
    time.sleep(5)
