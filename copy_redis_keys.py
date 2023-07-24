"""
Technologies:
1. Python3
2. Redis

1. connect to redis.
2. Define variable that stores 'key' which we want to search for matching pattern using wildcard (*) (matches any string).
3. call fetch_values function.
Here we 1st iterate through all matching key "name*" with scan_iter() method.
using smembers() method, we fetch all values for matching pattern.
Then replace existing key with New_key and add/copy the values in it.
"""

import redis
import myconfig as Config

def fetch_values(key_pattern):
    for key in redis_con.scan_iter(key_pattern):
        value = redis_con.smembers(key)
        print(f"Old_key: {key} \tValues: {value}")
        rep_key = key.decode('utf-8').replace('name', 'New_key')
        print(f"New key: {rep_key} \tValue: {value}")
        redis_con.sadd(rep_key, *value)

if __name__ == "__main__":
    redis_con = redis.Redis(host = Config.Redis_Config['host'], port = Config.Redis_Config['port'])
    print('Connected to Redis!')

    key_pattern = "name*" 

    fetch_values(key_pattern)