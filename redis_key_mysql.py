"""
Technologies
1. Python 3
2. Redis
3. Mysql

1. connect to redis.
2. take all keys in a variable for which we want to find matching wildcard (*) records.
3. call copy_keys function with these keys in step2.
4. with help of scan.iter() method, we iterate over matching keys and fetch values of those keys using get() method in redis.
5. Establish mysql connection.
6. loop through fetched values from copy_keys function.
7. breakdown values of keys using split() function so that we can store all individual values into mysql table.
8. we are reducing 1hr from current hour value fetched from matching records.
9. insert all fetched values from matching keys into mysql table. Using ON DUPLICATE KEY, we are updating count to count + 1.
"""

import redis
import mysql.connector
import myconfig as Config

config_mysql = {
    'host': Config.DATABASE_CONFIG['host'],
    'user': Config.DATABASE_CONFIG['user'],
    'password': Config.DATABASE_CONFIG['password'],
    'database': Config.DATABASE_CONFIG['database']
}

# Function to connect Database with DB configuration
def connect_db(dbname, **config_mysql):
    try:
        cnx = mysql.connector.connect(**config_mysql)
        cur = cnx.cursor(dictionary=True)
        cnx.autocommit = True
        print('{} Database Connected Successfully'.format(dbname))
    except mysql.connector.Error as err:
        print('Database Connection Error: {}'.format(err))
        raise Exception
    return (cnx, cur)

# Function to close Database
def close_db(dbname, master_slave):
    (cnx, cur) = master_slave
    cur.close()
    cnx.close()
    print('{} Connection Closed Successfully'.format(dbname))

def copy_keys(redis_client, key_pattern=[]):
    matched_keys = {}

    for matches in key_pattern:
        for key in redis_client.scan_iter(f'{matches}*'):
            value = redis_client.get(key)
            matched_keys[key.decode('utf-8')] = int(value.decode('utf-8'))

    return matched_keys

if __name__ == "__main__":
    redis_con = redis.Redis(host = Config.Redis_Config['host'], port = Config.Redis_Config['port'])
    print("Redis connected\n")

    # pattern for the old key
    prefixes_to_fetch = ['ADS_REQUEST', 'EMPTY_RESPONSE', 'FILLED_RESPONSE']

    # Function to copy the keys
    matched_key_value = copy_keys(redis_con, prefixes_to_fetch)

    if matched_key_value:
        (cnx, cur) = connect_db('[ MASTER ]', **config_mysql)

        data_to_insert = []
        for key, value in sorted(matched_key_value.items()):
            print(f"{key}: {value}")
            parts = key.split('-')
            website_id = int(parts[2])
            ad_response = 0
            empty_response = 0
            ad_request = 0
            created_date = "-".join(parts[4:7])
            current_hour = int(parts[8])
            inventory_type = int(parts[10])

            current_hour = 0 if int(current_hour) == 23 else (int(current_hour) - 1) % 24

            if key.startswith('ADS_REQUEST'):
                ad_response = value
            elif key.startswith('EMPTY_RESPONSE'):
                empty_response = value
            elif key.startswith('FILLED_RESPONSE'):
                ad_request = value

            # Add the data tuple to the list
            data_to_insert.append((website_id, ad_response, empty_response, ad_request, created_date, current_hour, inventory_type))

        # Construct the query
        query = """INSERT INTO tbl_redis_records 
                   (website_id, ad_response, empty_response, ad_request, created_date, current_hour, inventory_type) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s) 
                   ON DUPLICATE KEY UPDATE 
                   ad_response = ad_response + VALUES(ad_response),
                   empty_response = empty_response + VALUES(empty_response),
                   ad_request = ad_request + VALUES(ad_request)"""

        cur.executemany(query, data_to_insert)
        close_db('[ MASTER ]', (cnx, cur))
        print("Data inserted successfully!")