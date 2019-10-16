#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import boto3


dynamodb = boto3.resource('dynamodb', region_name='us-east-2')


def create_properties_table():
    table = dynamodb.create_table(
        TableName='properties',
        KeySchema=[
            {
                'AttributeName': 'item_num',
                'KeyType': 'HASH'  #Partition key
            },
            {
                'AttributeName': 'amount_due',
                'KeyType': 'RANGE'  #Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'item_num',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'amount_due',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10 
        }
    )

    print("Table status:", table.table_status)


if __name__ == '__main__':
    create_properties_table()
