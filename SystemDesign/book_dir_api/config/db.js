// write db connection here
const mongoose = require('mongoose');

var url ='mongodb://localhost:27017/booksDB';

const connection = mongoose.createConnection(url);

module.exports = connection;
