import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')

def lambda_handler(event, context):
    
    print("Received event:", json.dumps(event, indent=2))
    
    if 'httpMethod' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps(event, indent=2)
        }
    
    if event['httpMethod'] == 'POST':
        # create a new student record
        student = json.loads(event['body'])
        table.put_item(Item=student)
        return {
            'statusCode': 200,
            'body': json.dumps('Student record added successfully')
        }
    
    elif event['httpMethod'] == 'GET':
        # fetch student record by student_id
        student_id = event['queryStringParameters']['student_id']
        response = table.get_item(Key={'student_id': student_id})
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }
