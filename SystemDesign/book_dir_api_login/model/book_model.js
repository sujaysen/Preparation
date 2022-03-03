// write schema for mongo
const mongoose = require('mongoose');
const db = require('../config/db');

const userSchema = new mongoose.Schema({
    username:{
        type:String,
        default:"----"
    },
    password:{
        type:String,
        default:"----"
    }
});

const usermodel = db.model('users',userSchema);
module.exports = usermodel;
