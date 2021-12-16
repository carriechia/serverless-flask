import boto3
import json
from config import Config
import uuid


# def push_sqs(data):
#     deduplicationId = str(uuid.uuid1())
#     sqs_client = boto3.client("sqs", region_name="us-east-1")

#     response = sqs_client.send_message(
#         MessageGroupId=str(1),
#         QueueUrl="https://sqs.us-east-1.amazonaws.com/088232242632/TestQueue.fifo",
#         MessageBody=json.dumps(data),
#         MessageDeduplicationId=deduplicationId
#     )
#     # print(response)
#     return response


# def create_queue():
#     sqs_client = boto3.client("sqs", region_name="us-east-1")
#     response = sqs_client.create_queue(
#         QueueName="TestQueue.fifo",
#         Attributes={
#             "DelaySeconds": "0",
#             "VisibilityTimeout": "60",  # 60 seconds
#         }
#     )
#     print(response)




def push_sqs(data, is_retry=False):
    config = Config()
    deduplication_id = str(uuid.uuid1())
    session = boto3.session.Session(aws_access_key_id=config.AWS_ACCESS_KEY,
                                    aws_secret_access_key=config.AWS_SECRET_KEY,
                                    aws_session_token=config.AWS_SESSION_TOKEN,
                                    region_name=config.AWS_REGION)
    sqs = session.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName=config.CRON_JOB_QUEUE_NAME,
                                  QueueOwnerAWSAccountId=config.QUEUE_OWNER_ACCOUNT_ID)


    # if is_retry:
    #     if 'retry' not in data:
    #         data.update({'retry': 0})
    #     data['retry'] += 1
    #     deduplication_id = "{}-{}".format(deduplication_id, data['retry'])
    r = queue.send_message(MessageBody=json.dumps(data),
                           MessageGroupId=str(1),
                           MessageDeduplicationId=deduplication_id)
    print("{} push_type:{} is_retry:{} \n data:{} \n response:{}".format("[SQS LOG]", push_type, is_retry, data, r))