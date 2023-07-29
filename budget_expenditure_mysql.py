'''
Technologies Used:
1. Python3
2. Mysql
3. AWS

1. Establish mysql connection.
2. Here we have 3 function which allows users to insert/update/delete records into/from mysql table.
3. For all 3 functions, user is initially asked whether he/she wants to provide inputs.
if Yes, user is asked for particular and amount to be entered.
after providing inputs, user is again asked whether he wants to continue giving inputs. If Yes, programe continues. If No, programe terminates.
4. Finally all data given by user is stored into Mysql database table in bulk and uploaded to AWS S3 bucket.
Here we are directly appending all data to file that is already present in AWS S3.
5. Lastly we are downloading file from AWS S3 bucket in our local machine in specified folder.

Note: This script demonstrates how to insert/update/delete records in bulk.

This programme is intended to keep expenditure records like amount spent for which items. 
This will help user to keep track of payment done for any item during particular month.
At the end of the month, user will get to know how much money was spent in total in entire month for particulars used.

'''

from datetime import datetime
import mysql
from mysql import connector
import myconfig as Config
import io
import boto3
import logging


#DB config for master
config_master = {
'user': Config.DATABASE_CONFIG['user'],
'password': Config.DATABASE_CONFIG['password'],
'host': Config.DATABASE_CONFIG['host'],
'database': Config.DATABASE_CONFIG['database'],
}

ACCESS_KEY = Config.S3_ACCESS['access_key']
SECRET_ACCESS_KEY = Config.S3_ACCESS['secret_access_key']
s3_bucket_name = Config.S3_ACCESS['bucket_name']
File = Config.S3_ACCESS['sql_file']
filename = Config.S3_ACCESS['sql_filename']

# Function to connect Database with DB configuration
def connect_db( dbname, **config):
    try:
        cnx = mysql.connector.connect(**config)
        cur = cnx.cursor(dictionary=True)
        cnx.autocommit = True
        print('{} Database Connected Successfully'.format(dbname))
        logger.info('{} Database Connected Successfully'.format(dbname))
    except mysql.connector.Error as err:
        print('Database Connection Error: {}'.format(err))
        logger.error('Database Connection Error: {}'.format(err))
        raise Exception
    return (cnx, cur)

# Function to close Database
def close_db( dbname, master_slave):
    (cnx, cur) = master_slave
    cur.close()
    cnx.close()
    print('{} Database Connection Closed Successfully'.format(dbname))
    logger.info('{} Database Connection Closed Successfully'.format(dbname))

def connect_s3(logger):
    # print('Uploading log file to s3')
    # logger.info('Uploading log file to s3')
    client = boto3.client('s3', aws_access_key_id = ACCESS_KEY, aws_secret_access_key = SECRET_ACCESS_KEY)
    s3_resource = boto3.resource('s3', aws_access_key_id = ACCESS_KEY, aws_secret_access_key = SECRET_ACCESS_KEY)
    return s3_resource, client

def sum_of_amount():
    # calculating sum of Amount column
    some = "select sum(Amount) as Total from Expenditure_July" 
    cur.execute(some)
    get_query = cur.fetchone()

    # Access the total value
    total_value = get_query['Total']

    # Updating total value in table
    update_query = '''UPDATE Expenditure_July SET Total_Amount = %s'''
    cur.execute(update_query, (total_value,))

    return total_value

def insert_query():
    insert_input = input("Do you want to insert any records in table? Yes or No \n").capitalize()
    if insert_input == "Yes":
        insert_entries = []
        response = True
        while response:
            particulars = input(("Enter Particulars\n")).capitalize()
            amount = float(input("Enter amount\n"))
            date = datetime.now()
            insert_entries.append((particulars, amount, date))

            logger.info("User input Entered are: Particulars: '{}', Amount: '{}' ".format(particulars, amount))

            user_input = input("Do you want to continue giving inputs?? Yes or No \n").capitalize()
            response = True if user_input == 'Yes' else False
            if user_input == 'Yes':
                logger.info(" ")

        print('Insert_entries: ', insert_entries)
        # get table name from database
        tab = '''SELECT Table_name from information_schema. tables where table_schema = "Development" '''
        cur.execute(tab)
        table = cur.fetchall()[1]['TABLE_NAME']

        # Insert user inputs into table
        query = ''' INSERT INTO `Expenditure_July` (`Particulars`, `Amount`, `Date`) VALUES (%s, %s, %s) '''
        cur.executemany(query, insert_entries)
        print(f"Data inserted successfully into Table: '{table}' ")
        logger.info(f"Data inserted successfully into Table: '{table}', Database: '{Config.DATABASE_CONFIG['database']}' ")

        sum_total = sum_of_amount()
        print(f'Amount spent till now: {sum_total}')
        logger.info(f'Amount spent till now: {sum_total}')

    else:
        print("Thank you for the response!")
        logger.info("User do not want to insert records in 'Expenditure_July' table")

    return insert_input

def update_query():
    update_input = input("Do you want to update any records in table? Yes or No \n").capitalize()
    if update_input == "Yes":
        update_entries = []

        response = True
        while response:
            up_sl_no = int(input("Please provide Sl_No for which you want to update values! \n"))
            up_particulars = input(("Enter Particular \n")).capitalize()
            up_amount = float(input("Enter amount \n"))
            update_entries.append((up_particulars, up_amount, up_sl_no))

            logger.info("User inputs Entered to update the records are: Particulars: '{}', Amount: '{}' ".format(up_particulars, up_amount))

            user_up_input = input("Do you want to make any further changes?? Yes or No \n").capitalize()
            response = True if user_up_input == "Yes" else False
            if user_up_input == 'Yes':
                logger.info(" ")

        print('update_entries: ', update_entries)
        up_query = "update Expenditure_July set Particulars = %s, Amount = %s where Sl_No = %s"
        cur.executemany(up_query, update_entries)
        print(f"Updated values for Particular: '{up_particulars}', Amount: '{up_amount}' corresponding to Sl_No: {up_sl_no} in table Expenditure_July")
        logger.info(f"Updated values for Particular: '{up_particulars}', Amount: '{up_amount}' corresponding to Sl_No: {up_sl_no} in table Expenditure_July")

        sum_total = sum_of_amount()
        print(f'Total amount spent after updating the record is: {sum_total}')
        logger.info(f'Total amount spent after updating the record is: {sum_total}')

    else:
        print("Thank you for the response!")
        logger.info("User do not want to update records in 'Expenditure_July' table")

    return update_input

def delete_values():
    delete_input = input("Do you want to delete any records in table? Yes or No \n").capitalize()
    if delete_input == "Yes":
        delete_entries = []

        select_query = "select Sl_No, Particulars, Amount from Expenditure_July"
        cur.execute(select_query)
        show = cur.fetchall()
        
        for records in show:
            print(records)
            print()

        response = True
        while response:
            del_particulars = int(input("Enter Sl_No you want to delete from above list\n"))
            delete_entries.append((del_particulars,))

            logger.info(f"User input Entered to delete the record from table Expenditure_July is: Particulars: '{del_particulars}' ")
            
            user_udel_input = input("Do you want to delete any more records from table?? Yes or No \n").capitalize()
            response = True if user_udel_input == "Yes" else False
            if user_udel_input == 'Yes':
                logger.info(" ")

        print('delete_entries: ', delete_entries)
        del_query = "delete from Expenditure_July where Sl_No = %s"
        cur.executemany(del_query, delete_entries)
        print("Record deleted successfully from Expenditure_July table")
        logger.info(f"Sl_No: {del_particulars} deleted successfully from Expenditure_July table")

        sum_total = sum_of_amount()
        print(f'Total amount spent after deleting the record is: {sum_total}')
        logger.info(f'Total amount spent after deleting the record is: {sum_total}')

    else:
        print("Thank you for the response!")
        logger.info("User do not want to delete any records from 'Expenditure_July' table")

    return delete_input

def logger_creator(log_stringio_obj):
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.INFO)
    #create stream handler and initialise it with string io buffer
    string_io_log_handler = logging.StreamHandler(log_stringio_obj)
    string_io_log_handler.setFormatter(formatter)
	#add stream handler to logger
    logger.addHandler(string_io_log_handler)
    return logger

# Function to upload log files to s3 bucket
def uploading_log_s3(logger):
    # Connecting to s3
    s3_resource, client = connect_s3(logger)
    # Read the existing object's contents from S3
    response = client.get_object(Bucket = s3_bucket_name, Key = File)
    existing_data = response['Body'].read().decode('utf-8')
    log_contents = log_stringio_obj.getvalue()
    # Append the log_data to the existing file
    combined_data = existing_data + '\n' + log_contents
    # Encode the combined data as UTF-8
    combined_data_bytes = combined_data.encode('utf-8')
    # Uploading combined_log_data back to the same file
    client.put_object(Body = combined_data_bytes, Bucket = s3_bucket_name, Key = File)


def download_file_s3(logger):
    if insert_input == "No" and  update_input == "No" and delete_input == "No":
        print("Thank you for your response! No file downloded from S3 Bucket to folder")
        logger.info("User did not insert, update and delete any records. So file from S3 Bucket was not downloaded!")
    else:
        try:
            obj = boto3.client("s3")
            obj.download_file(Filename = filename, Bucket = s3_bucket_name, Key = File)
            print(f"Downloaded file from S3 bucket to folder..")
        except Exception as e:
            logger.error('AWS s3 Bucket Download Error: {}'.format(e))
            print('AWS s3 Bucket Download Error: {}'.format(e))

if __name__ == '__main__':
    
    #create string i/o object as string buffer
    log_stringio_obj = io.StringIO()
    logger = logger_creator(log_stringio_obj)

    (cnx, cur) = connect_db('test', **config_master)

    insert_input = insert_query()

    update_input = update_query()

    delete_input = delete_values()

    close_db('test', (cnx, cur))

    logger.info(f"Downloaded file '{File}' from S3 bucket to '{filename}' folder.")

    uploading_log_s3(logger)

    download_file_s3(logger)