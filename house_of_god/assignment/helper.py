import time

import tablib

from . import serializers


def upload_csv():
    with open('/Users/sagar/assignment-sampleinput.csv', encoding="utf8", errors="ignore") as f:
        tdata = tablib.Dataset().load(f.read(), 'csv')

    for i, item in enumerate(tdata.dict, start=1):
        post_id = int(item['Post ID'])
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(item[' Timestamp'])))
        print(timestamp)
        data = {'post_id': post_id, 'timestamp': timestamp}
        serializer = serializers.PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
        else:
            print('saga', serializer.errors)
