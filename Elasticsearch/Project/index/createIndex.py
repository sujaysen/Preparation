import sys
sys.path.append('../')
from config.conn import es,index

body = {
    "settings":
    {
        "analysis":
        {
            "analyzer":
            {
                "autocomplete":
                {
                    "tokenizer": "autocomplete",
                    "filter": ["lowercase"]
                },
                "autocomplete_search":
                {
                    "tokenizer": "lowercase"
                },
				"startwith_analyzer":{
					"tokenizer":"startwith_analyzer"
				},
				"startwith_search_analyzer":{
					"tokenizer":"keyword"
				}
            },
            "tokenizer":
            {
                "autocomplete":
                {
                    "type": "edge_ngram",
                    "min_gram": 1,
                    "max_gram": 10,
                    "token_chars": ["letter","digit"]
                },
				"startwith_analyzer":{
					"type":"edge_ngram",
					"min_gram": 1,
					"max_gram": 10,
					"token_chars": ["letter","digit"]
				}
            }
        }
    },
    "mappings":
    {
        "_doc":
        {
            "properties":
            {
                "data_field":
                {
                    "type": "keyword"
                },
                "query_field":
                {
                    "type": "text",
                    "fields":
                    {
                        "exact":
                        {
                            "type": "text",
                            "analyzer": "keyword"
                        },
                        "startwith":
                        {
                            "type": "text",
                            "analyzer": "autocomplete",
                            "search_analyzer": "autocomplete"
                        },
                        "all":
                        {
                            "type": "text",
                            "analyzer": "standard"
                        }
                    }
                }
            }
        }
    }
}

if es.indices.exists(index=index):
	es.indices.delete(index=index, ignore=[400, 404])
	print("{} Deleted successfully!".format(index))

try:
	es.indices.create(index = index, body = body)
	print("{} Created successfully!".format(index))
except Exception as e:
	print("Error encountered while creating Index")
	print(e)
