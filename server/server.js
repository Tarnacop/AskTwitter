/**
 * Created by aml on 01/10/2016.
 */

const express = require('express')
const app = express()

app.get('/', function (req, res) {
    res.send('Hello World')
});

app.listen(5000);