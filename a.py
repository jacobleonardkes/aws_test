import boto3
sqs = boto3.resource('sqs','us-east-1')
q = sqs.create_queue(QueueName='test1')
response = q.send_message(MessageBody='asdf')
