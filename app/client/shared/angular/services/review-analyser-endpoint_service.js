/**
 * Created by aml on 01/10/2016.
 */
'use strict';

angular.module('review-analyser-endpoint_service', [])
    .factory('analyser', ['$http', $http => {
        const keywordAnalysisUrl = 'http://127.0.01:5000/ask_keyword/';
        const usernameAnalysisUrl = 'http://127.0.01:5000/ask_username/?keyword=christmas';

        const buildUrlWithQuery = (url, query, isKeyWordAnalysis) => {

            return isKeyWordAnalysis ? url + '?keyword=' + query : url + '?username=' + query;
        };

        const readKeywordAnalysis = query => {

            $http.get(buildUrlWithQuery(keywordAnalysisUrl, query, true)).then(response => {
                return response.data;
            });
        };

        const readUsernameAnalysis = query => {

            $http.get(buildUrlWithQuery(usernameAnalysisUrl, query, false)).then(response => {
                return response.data;
            });
        };

        return {
            readKeywordAnalysis: readKeywordAnalysis
        };
    }]);

