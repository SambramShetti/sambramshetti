'''
Technologies:
1. Python3
2. Mongodb
3. AWS

Code flow explanation:
1. user gets prompt to choose the number whether he wants to insert/update/delete records to/from collection.
2. Based on number selected by user, he will be asked for updating details.
Like if he wants to insert records into collection, he will be asked to provide particulars and amount. 
Or if user wants to update/delete records, he will be asked to provide 'id' for which we wants to update/delete records
3. Again user is asked whether he wants to insert/update/delete records. This loop continues untill user doesn't want to provide any inputs.
4. Here we are creating log file with help of logger_creator() function which stores all log details.
5. Log file will be created in local machine in specified path but user is asked whether he wants all the details given by him/her to upload to AWS S3 Bucket.
If user input is 'Yes', log file is uploaded to AWS S3 or else file is not updated.

'''

import myconfig as Config
import pymongo
from datetime import datetime
from bson import ObjectId
import boto3
import logging

# AWS Details
ACCESS_KEY = Config.S3_ACCESS['access_key']
SECRET_ACCESS_KEY = Config.S3_ACCESS['secret_access_key']
s3_bucket_name = Config.S3_ACCESS['bucket_name']
File = Config.S3_ACCESS['mongo_file']
filename = Config.S3_ACCESS['mongo_filename']

# Function to insert record(s) into collection
def insert_record():

    insert_response = True

    while insert_response:
        particular = input('Enter particular\n').capitalize()
        amount = float(input('Enter amount\n'))
        date = datetime.now().strftime('%y-%m-%d')

        record = {
            'Particular' : particular,
            'Amount' : amount,
            'Date' : date
        }

        collection.insert_one(record)
        print('Inserted record(s) into collection successfully!')
        logger.info(f'Inserted Particular : {particular}, Amount : {amount}, Date: {date} into collection successfully!')

        continue_insert_input = input("Do you want to continue giving inputs?? Yes or No \n").capitalize()
        insert_response = True if continue_insert_input == 'Yes' else False

    if continue_insert_input == 'No':
        print('Thank you for your response!')

# Function to delete record(s) from collection
def delete_record():

    delete_response = True
    
    while delete_response:

        # Display available records in collection to user
        delete_id = collection.find({})
        for id in delete_id:
            print(id)

        delete_choice = (input('Select an 24 character ObjectId for which you want to delete record \n'))
        collection.delete_one({'_id' : ObjectId(delete_choice)})
        print('Deleted record(s) from collection successfully!')
        logger.info(f'Deleted record for {collection} !')

        continue_delete_input = input("Do you want to delete any other records?? Yes or No \n").capitalize()
        delete_response = True if continue_delete_input == 'Yes' else False

    if continue_delete_input == 'No':
        print('Thank you for your response!')

# Function to update record in collection
def update_record():

    update_response = True
        
    while update_response:

        # Display available records in collection to user
        update_id = collection.find({})
        for id in update_id:
            print(id)

        update_choice = (input('Select an 24 character ObjectId for which you want to update the record \n'))
        update_particular = input('Please enter Particular! \n').capitalize()
        update_amount = float(input('Please enter amount! \n'))

        prev = {'_id' : ObjectId(update_choice)}
        nextt = {'$set': {'Particular': update_particular, 'Amount':update_amount}}

        collection.update_one(prev, nextt)
        print(f'Updated record(s) in collection successfully!')
        logger.info(f'Updated Particular : {update_particular}, Amount : {update_amount} for {prev}')

        continue_update_input = input("Do you want to update any other records?? Yes or No \n").capitalize()
        update_response = True if continue_update_input == 'Yes' else False

    if continue_update_input == 'No':
        print('Thank you for your response!')

# Function to connect to S3
def connect_s3(logger):
    client = boto3.client('s3', aws_access_key_id = ACCESS_KEY, aws_secret_access_key = SECRET_ACCESS_KEY)
    s3_resource = boto3.resource('s3', aws_access_key_id = ACCESS_KEY, aws_secret_access_key = SECRET_ACCESS_KEY)
    return s3_resource, client

# Function to create logger
def logger_creator():
    logger = logging.getLogger('Monthly_expenditure')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.INFO)
    logHandler = logging.FileHandler(filename) # creates the file in local
    logHandler.setLevel(logging.INFO)
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    return logger

# Function to upload log file to AWS S3 bucket
def uploading_log_s3(logger):
    # Connecting to s3
    s3_resource, client = connect_s3(logger)
    print('Uploading file to AWS S3 Bucket!')
    logger.info('Uploading file to AWS S3 Bucket!')
    s3_resource.Object(s3_bucket_name, File).upload_file(filename)

if __name__ == "__main__":

    logger = logger_creator()

    # Mongodb connection to local
    client = pymongo.MongoClient(Config.Mongo_db['connection'])
    # Connection to Mongodb Atlas
    # client = pymongo.MongoClient('mongodb+srv://sambram:<password>@cluster0.ow6xbcb.mongodb.net/') # replace <password> with actual password
    database = client[Config.Mongo_db['database']] # creates database in mongodb
    collection = database[Config.Mongo_db['collection']] # creates collection in database

# while loop that continues to ask user for his inputs/choices untill he wants to exits
    choice = True
    while choice:
        print('Choose your option! ', end = " " )
        user_choice = int(input('''
1. Insert record(s) into collection
2. Update record(s) in collection
3. Delete record(s) from collection
Please enter your desired number
'''))

        if user_choice == 1:
            insert_record()
        elif user_choice == 2:
            update_record()
        elif user_choice == 3:
            delete_record()
        updated_choice = input('Do you want to choose options again? Yes or No \n').capitalize()
        choice = True if updated_choice == 'Yes' else False
    if updated_choice == 'No':
        print('Thank you for your response!')

    # Asking user for uploading file to AWS S3
    s3_input = input('Do you want to log all details to AWS S3 bucket? Yes or No \n').capitalize()
    if s3_input == 'Yes':
        uploading_log_s3(logger)
        print('Success! Logged details to AWS S3.')
    else:
        print('Details not updated to AWS S3!')
