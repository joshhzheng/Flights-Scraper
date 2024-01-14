# import json
# import boto3

# def lambda_handler(event, context):
#     client = boto3.client("ses")
#     subject = "test subject"
#     body = "test body" 
#     message = {"Subject": {"Data" : subject}, "Body": {"Html": {"Data" : body}}}
#     response = client.send_email(Source = "joshzheng99@outlook.com", 
#                                  Destination = {"ToAddresses" : ["joshzheng99@outlook.com"]}, Message = message)
#     return response


import json
import boto3
import pandas as pd
from main import *

def format_dataframe_to_text(df):
    # Format the DataFrame to a readable text
    formatted_text = df.to_string(index=False)
    return formatted_text

def lambda_handler(event, context):
    main()
    df_sorted = main.df_sorted

    formatted_text = format_dataframe_to_text(df_sorted)

    client = boto3.client("ses")
    subject = "Flight Data"
    body = formatted_text

    message = {
        "Subject": {"Data": subject},
        "Body": {"Text": {"Data": body}}
    }

    response = client.send_email(
        Source="joshzheng99@outlook.com",
        Destination={"ToAddresses": ["teemoing99@gmail.com"]},
        Message=message
    )

    return response
