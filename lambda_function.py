import json
import boto3
import pandas as pd
from main import *

def format_dataframe_to_text(df):
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
        Destination={"ToAddresses": ["joshzheng99@outlook.com"]},
        Message=message
    )

    return response