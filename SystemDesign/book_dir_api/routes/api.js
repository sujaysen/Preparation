// write api here
const router = require('express').Router();
const bookModel = require('../model/book_model');

// Get all book list
router.get('/books', async function (req, res) {
   const bookList = await bookModel.find();
   console.log(bookList);
   res.send(bookList);
});

// Get a particular book
router.get('/books/:id', async function (req, res) {
    const { id } = req.params;
    const book = await bookModel.findOne({isbn : id});
    if(!book) return res.send("Book Not Found");
    res.send(book);
});

// Just for test
router.post('/login', async function (req, res) {
    user = req.body.username;
    pass = req.body.password;
    userExist = await userModel.findOne({user : user});
    if (!userExist) return res.send('User does not exist');
    res.send('successfully logged in');
});
router.post('/register', async function (req, res) {
    const user= req.body.username;
    const pass = req.body.password;
    const userExist = await userModel.findOne({username : user});
  
    if (!userExist) return res.send('User already exist');

    var data = await userModel.create({user,pass});
    data.save();

    res.send("User Registered");
});

// Insert a book
router.post('/books', async function (req, res) {
    const title= req.body.title;
    const isbn = req.body.isbn;
    const author = req.body.author;
    const bookExist = await bookModel.findOne({isbn : isbn});
  
    if (bookExist) return res.send('Book already exist');

    var data = await bookModel.create({title,isbn,author});
    data.save();

    res.send("Book Uploaded");
});

// Update a book
router.put('/books/:id', async function (req, res) {
    const { id } = req.params;
    const {
        title,
        authors,
    } = req.body;

    const bookExist = await bookModel.findOne({isbn : id});
    if (!bookExist) return res.send('Book Do Not exist');


    const updateField = (val, prev) => !val ? prev : val;

    const updatedBook = {
        ...bookExist ,
        title: updateField(title, bookExist.title),
        authors: updateField(authors, bookExist.authors),
        
    };

    await bookModel.updateOne({isbn: id},{$set :{title : updatedBook.title, author: updatedBook.authors}})
    
    res.status(200).send("Book Updated");
});

router.delete('/books/:id', async function (req, res) {
    const { id } = req.params;

    const bookExist = await bookModel.findOne({isbn : id});
    if (!bookExist) return res.send('Book Do Not exist');

   await bookModel.deleteOne({ isbn: id }).then(function(){
        console.log("Data deleted"); // Success
        res.send("Book Record Deleted Successfully")
    }).catch(function(error){
        console.log(error); // Failure
    });
});

module.exports = router;
