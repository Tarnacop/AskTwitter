/**
 * Created by aml on 01/10/2016.
 */

'use strict';

const express = require('express');
const utils = require('./utils');

const app = express();

app.use("/css", express.static(utils.joinPathWithClient('/shared/css')));
app.use("/images", express.static(utils.joinPathWithClient('/shared/images')));
app.use("/analyser", express.static(utils.joinPathWithClient('/review-analyser')));
app.use("/angular-shared", express.static(utils.joinPathWithClient('/shared/angular')));

app.get('/', (req, res) => {
    res.sendFile(utils.joinPathWithClient('index.html'));
});

app.get('/review-analyser', (req, res) => {
    res.sendFile(utils.joinPathWithClient('review-analyser/review-analyser.html'));
});

app.listen(5000);