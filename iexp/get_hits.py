import os
from elasticsearch import Elasticsearch

es = Elasticsearch()

res = es.search(index="en-sent-summ-index-iexp", body={"query": {"match_all": {}}},request_timeout=30)
print("Got %d Hits:" % res['hits']['total'])

os.system("touch " + str(res['hits']['total']))
