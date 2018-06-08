from elasticsearch import Elasticsearch


es = Elasticsearch()


## Alternate way
elasticseaerch.helpers.scan(
    es,
    query = {
		# your query
	    },
    index = index,
    doc_type = dtype,
)

## Initialize parameters
iname = ""
dtype = ""

# Initialize the scroll
page = es.search(
    index = iname,
    doc_type = "",
    scroll = '2m',
    search_type = 'scan',
    size = 1000,
    body = { # your query's body}
    )

sid = page['_scroll_id']
scroll_size = page['hits']['total']

# start scrolling

while (scroll_size > 0):
    print "scrolling.."
    page = es.scroll(scroll_id = sid, scroll = '2m')
    # update the scroll ID
    sid = page['_scroll_id']
    # Get the number of results that we returned in the last scroll
    scroll_size = len(page['hits']['hits'])
    print "scroll size: " + str(scroll_size)
    # Do something with the obtained page

    # clear scroll
    es.clear_scroll(body={'scroll_id': [sid]}, ignore=(404, ))
