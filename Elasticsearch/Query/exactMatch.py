index_body = {
	"settings": {
		"analysis": {
			"analyzer" : {
				"exact_analyzer": {
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
						"exact": {
							"type": "text",
							"analyzer": "exact_analyzer",
							"search_analyzer": "exact_analyzer"
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
					"cs.exact":search_term
				}
			],
			"must_not": [
				"ids": {
					"values":[]
			]
		}
	},
	"from": 0,
	"size": 10,
	"sort": ["pop":{"order":"desc"}],
	"aggs": {}
}
