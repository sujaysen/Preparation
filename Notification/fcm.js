/////  Tutorial for push notification to client device //////

// Install the fcm-notification using npm
// npm install fcm-notification --save

var fcm = require('fcm-notification');
var FCM = new fcm('path/to/privatekey.json');

// Download privatekey.json from the following link
// https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk

// Send to single token 
var token = "token";

// create message in your own requirment
var message = {
	data : {
		"score" : "100",
		"time" : "2:30" 
	},
	notification : {
		title : "title here",
		body : "body here"
	},
	token : token
};

FCM.send(message , function(err , resp){
	if(err){
		console.log("Error : ",err);
	} else {
		consolr.log("Response : ",resp)
	}
});

// Send to multiple tokens
var Tokens = [ 'token1 here', '....', 'token n here'];
// create message in your own requirment
var message = {
	data : {
		"score" : "100",
		"time" : "2:30" 
	},
	notification : {
		title : "title here",
		body : "body here"
	}
};

FCM.sendToMultipleToken(message , Tokens , function(err , resp){
	if(err){
		console.log("Error : ",err);
	} else {
		consolr.log("Response : ",resp)
	}
});


// send to topic
// To send to a topic first need to subscribe

// subscribe a topic for tokens
var tokens =[ 'token1 here', '....', 'token n here'];
var topic = "topicname"

FCM.subscribeToTopic(tokens , topic , function(err , resp){
	if(err){
		console.log("Error : ",err);
	} else {
		consolr.log("Response : ",resp)
	}
});

// unsubscribe a topic for tokens
var tokens =[ 'token1 here', '....', 'token n here'];
var topic = "topicname"

FCM.unsubscribeFromTopic(tokens , topic , function(err , resp){
	if(err){
		console.log("Error : ",err);
	} else {
		consolr.log("Response : ",resp)
	}
});

// send to topic
topic = "topic name"
// create message in your own requirment
var message = {
	data : {
		score : "250",
		time : "5:20"
	},
	notification : {
		title : "title here",
		body : "body here"
	},
	topic : topic
};

FCM.send(message , function(err , resp){
	if(err){
		console.log("Error : ",err);
	} else {
		consolr.log("Response : ",resp)
	}
});

// send to multiple topics
var Topics = ['Topic one',  '..',  'Topic n'];

// create message in your own requirment
var message = {
	data : {
		"score" : "100",
		"time" : "2:30" 
	},
	notification : {
		title : "title here",
		body : "body here"
	}
};

FCM.sendToMultipleTopic(message , Topics , function(err , resp){
	if(err){
		console.log("Error : ",err);
	} else {
		consolr.log("Response : ",resp)
	}
});


