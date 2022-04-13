index_body = {
	"settings": {
		"analysis": {
			"analyzer" : {
				"startwith_analyzer": {
					"tokenizer":"keyword",
					"filter":[]
				}
			}
		}
	},
	"mappings": {
		"_doc": {
			"properties": {
				"cs":{
					"type": "text",
					"fields": {
						"startwith": {
							"type": "text",
							"analyzer": "startwith_analyzer",
							"search_analyzer": "startwith_analyzer"
						}
					}
				}
			}
		}
	}
}

query_body = {
	"query": {
		"bool": {
			"should": [
				"match": {
					"cs.startwith":search_term
				}
			],
			"must_not": [
				"ids": {
					"values":list_of_ids
			]
		}
	},
	"from": 0,
	"size": 10,
	"sort": ["pop":{"order":"desc"}],
	"aggs": {}
}











