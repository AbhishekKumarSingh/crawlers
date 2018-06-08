import elasticsearch
import elasticsearch.helpers

# initialize parameters
iname = "en-sent-summ-index-iexp"
dtype = "en_sent_summ_iexp"

es = elasticsearch.Elasticsearch()

scanner = elasticsearch.helpers.scan(es, query = {"query": {"match_all": {}}}, index=iname, doc_type=dtype,
                                     raise_on_error=False, request_timeout=30)

print scanner

count = 0
for item in scanner:
    count =  count + item['hits']['total']

print count
