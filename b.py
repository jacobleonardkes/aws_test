import boto3
client = boto3.client('sqs','us-east-1')
client.list_queues()
url = client.get_queue_url(QueueName='test1')['QueueUrl']
messages = client.receive_message(QueueUrl=url)
message = messages['Messages'][0]
message['Body']
message.delete()
