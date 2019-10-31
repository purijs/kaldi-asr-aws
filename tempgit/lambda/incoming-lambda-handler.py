import json
import boto3
import random
import string

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('audioAnalytics')

def lambda_handler(event, context):
    
    bodyInfo=json.loads(event['body'])
    
    userKey=bodyInfo['customerKey']
    filesList=bodyInfo['files']
    
    for file in filesList:
        
        primaryKey=userKey+'_sep_'+file.split('.')[0]+'.txt'
        table.put_item(Item={'customer_key':primaryKey})
    
    return {
        'statusCode': 200
    }