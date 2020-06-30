import boto3
import random
New = random.randint(150000, 999999)
Message = f'Verification Code for Assignment Project is = {New}'
client = boto3.client('sns', 'ap-south-1')
client.publish(PhoneNumber='+91**********', Message=Message)
