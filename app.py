import json

def handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps("Success! Your containerized microservice is running perfectly on AWS Lambda.")
    }