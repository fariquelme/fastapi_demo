from celery import Celery
import time
import os
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
import settings


redis_password = os.getenv('REDIS_PASSWORD')

CELERY_BROKER_URL=f'redis://:{redis_password}@localhost:6379/0'
CELERY_BACKEND_URL=f'redis://:{redis_password}@localhost:6379/1'

app = Celery('celery_conf', broker=CELERY_BROKER_URL, backend=CELERY_BACKEND_URL)

app.conf.broker_transport_options = {"queue_order_strategy": "sorted"}
app.control.enable_events(reply=True)
#import pdb;pdb.set_trace()
#app.conf.timezone

#app.conf.update(
#                enable_utc=True,
#                timezone='Europe/London',
#                )

app.autodiscover_tasks(['detect', 'api'])

@app.task
def add(x, y):
    time.sleep(2)
    return x + y

if __name__ == '__main__':
    result = add.delay(4, 4)
    print( result.get() )

