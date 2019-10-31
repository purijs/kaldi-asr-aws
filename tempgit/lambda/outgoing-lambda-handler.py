import json
import boto3
from boto3.dynamodb.conditions import Key

client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('audioAnalytics')
s3 = boto3.client("s3")

def lambda_handler(event, context):
    
    if event:
        
        file_obj = event["Records"][0]
        bucketname = str(file_obj['s3']['bucket']['name'])
        filename = str(file_obj['s3']['object']['key'])
        
        fileObj = s3.get_object(Bucket=bucketname, Key=filename)
        file_content = fileObj["Body"].read().decode('utf-8')
        
        file_content=file_content.replace('utterance-id1','')
        
        customer_key = filename.split('/')[1]
        
        table.update_item(
                Key={
                    "customer_key": customer_key
                },
                UpdateExpression="SET transcript = :t",
                ExpressionAttributeValues={
                    ':t': file_content
                }
            
            )
    
    return True