// write api here
const router = require('express').Router();
const elasticsearch = require('elasticsearch');
elasticserver = 'http://192.168.24.132:9200';

const esClient = elasticsearch.Client({
    host: 'http://192.168.24.132:9200',
})

router.get('/typos/:search_text', async function (req, res) {
    search_text = req.params.search_text;
    console.log(search_text)
    var body = {};
    var bool = {};
    bool = {
       "fuzzy":{
	   "string_variation.exact" : {
		   "value":search_text
	   }
        }
    }
    body = {"_source":["string"],"from": 0,"size" : 1,"query":bool,"sort":[{"pop":"desc"}]}
    esClient.search({
        index: "typos",
	type: "_doc",
        body:body
    })
    .then(resp => {
	var hits = resp.hits.hits.map(hit => hit._source.string);
	var count = resp.hits.total;
	if(count){
	   var response = {result: hits['0'],error:0};
	}else{
		var response = {result: hits,error:1};
	}
        return res.json(response)
    })
    .catch(err => {
        return res.status(500).json({"message": "Error"})
    })
    

});


module.exports = router;
