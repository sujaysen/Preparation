// Mysql- node js connection
var mysql = require('mysql');
var con = mysql.createConnection({
  host: "localhost",
  user: "justdial",
  password: "justdial",
  database: "sujay"
});

var sql = "CREATE TABLE nodejs (name VARCHAR(255), address VARCHAR(255))";
con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  con.query(sql, function (err, result) {
     if (err) throw err;
     console.log("Table created");
    });
});


