/**
 * Created by aml on 01/10/2016.
 */

const express = require('express');
const path = require('path');

const app = express();
const clientPath = path.join(__dirname, 'client');
console.log(__dirname);

app.use(express.static(clientPath));

app.get('/', function (req, res) {
    res.sendFile(path.join(clientPath, 'index.html'));
});

app.listen(5000);