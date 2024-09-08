# Serverless Web Application with AWS Lambda and DynamoDB
This application uses AWS Lambda, DynamoDB, and API Gateway to perform basic CRUD operations (Create, Read, Update, Delete) on the database. The DynamoDB database contains a table called StudentRecords. which holds information about students, such as the student id, name, and courses they are taking. The primary key for the database is the student id. The lambda function takes HTTP requests and performs the corresponding action on the database based on the type of request. API gateway was used to deploy the API and receive requests that would trigger the lambda function. As of now, the function handles creating table entries and reading from the table.

## Testing the application
For testing the application, `curl` was used to send HTTP requests to the deployed API Gateway. For testing the entry creation, the following command was ran: \
`curl -X POST https://<your-api-id>.execute-api.<region>.amazonaws.com/dev/students -H 'Content-Type: application/json' -d '{"student_id": "123", "name": "John Doe", "course": "Enterprise Software"}'` \
When successful, the console should output that the record was added successfully and could be verified when checking the DynamoDB dashboard.
![Screenshot 2024-09-08 at 12 09 10 AM](https://github.com/user-attachments/assets/eedd382d-0354-403c-9704-45336180085b)

For testing table entry retrieval, the following command was ran: \
`curl -X GET https://<your-api-id>.execute-api.<region>.amazonaws.com/dev/students?student_id=123` \
When successful, the console should output the table entry and its components. The following image shows example output of both of these cases:
![Screenshot 2024-09-08 at 12 08 11 AM](https://github.com/user-attachments/assets/e4ccb02f-0f94-4107-b7db-3044de5852d1)
