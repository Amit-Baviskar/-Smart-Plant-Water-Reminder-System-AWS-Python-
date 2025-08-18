import json
import base64
import boto3

sns_client = boto3.client('sns')
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:123456789012:PlantWaterAlert'  # Replace with your SNS ARN

def lambda_handler(event, context):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        data = json.loads(payload)
        
        value = data['value']
        sensor_id = data['sensor_id']

        print(f"Received sensor data: {data}")

        if value == 85:
            message = f"Alert! Plant {sensor_id} needs water. Sensor reading: {value}"
            subject = "Plant Water Reminder: Time to Water the Plant"
            send_email(message, subject)
        
        if value == 0:
            message = f"Critical! Plant {sensor_id} is dying. Sensor reading: {value}"
            subject = "CRITICAL ALERT: Your Plant is Dying!"
            send_email(message, subject)
    
    return {'statusCode': 200}

def send_email(message, subject):
    sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=subject,
        Message=message
    )
