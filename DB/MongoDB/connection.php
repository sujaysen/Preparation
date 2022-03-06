<?php
// PHP-Mongo connection
//$m = new MongoDB\Driver\Manager("mongodb://localhost:27017");
$m = new MongoClient();
echo "Connection to database successfully\n";
$db = $m->test;
echo "Database mydb selected\n";
$col = $db->createCollection("sujay");
echo "Collection created succsessfully\n";

?>
