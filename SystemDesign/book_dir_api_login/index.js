// main file
const express = require('express');
const bodyParser = require('body-parser');
const api = require('./routes/api');
const path = require("path");

const app = express();
const PORT = 3030;

app.use(bodyParser.json());
app.use(express.static(path.join(__dirname,'./public')));
//app.use('/', api);

app.get('/',(req,res) => {
    res.sendFile(path.join(__dirname,'./public/index.html'));
});
app.listen(PORT, () => console.log(`App listening on port ${PORT}`));
