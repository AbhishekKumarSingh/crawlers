import redis
import time

conn = redis.Redis('localhost')

while True:
    time.sleep(3600)
    conn.save()
    #time.sleep(3600)
