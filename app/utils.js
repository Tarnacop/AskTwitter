/**
 * Created by aml on 01/10/2016.
 */

'use strict';

const path = require('path');
const clientPath = path.join(__dirname, 'client');

module.exports = {

    joinPathWithClient: givenPath => {
        return path.join(clientPath, givenPath);
    },
    getClientPath: () => {
        return clientPath;
    }
};