// write api here
const router = require('express').Router();
const userModel = require('../model/book_model');


// Just for test
router.post('/login', async function (req, res) {
    username = req.body.username;
    password = req.body.password;
    userExist = await userModel.findOne({username : username});
    if (!userExist) return res.send('User does not exist');
    let storedPass = await userModel.findOne({username : username});
    if(storedPass.password != password){
	 // return res.send("<div align ='center'><h2>Invalid email or password</h2></div><br><br><div align ='center'><a href='./login.html'>login again</a></div>");
	 return res.send('Incorrect Password');
    }
    //res.send(`<div align ='center'><h2>login successful</h2></div><br><br><br><div align ='center'><h3>Hello ${usrname}</h3></div><br><br><div align='center'><a href='./login.html'>logout</a></div>`);
    res.send('successfully logged in');
});
router.post('/register', async function (req, res) {
    const username= req.body.username;
    const password = req.body.password;
    const userExist = await userModel.findOne({username : username});
  
    if (userExist) return res.send('User already exist');
    var data = await userModel.create({username,password});
    data.save();

    //res.send("<div align ='center'><h2>Registration successful</h2></div><br><br><div align='center'><a href='./login.html'>login</a></div><br><br><div align='center'><a href='./registration.html'>Register another user</a></div>");
    res.send("User Registered");
});

router.post('/forget', async function (req, res) {
    const username= req.body.username;
    const userExist = await userModel.findOne({username : username});
  
    if (!userExist) return res.send('User does not exist');

    res.send({"Password":userExist.password});
});

module.exports = router;
