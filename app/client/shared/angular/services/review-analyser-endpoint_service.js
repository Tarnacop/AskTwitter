/**
 * Created by aml on 01/10/2016.
 */
'use strict';

angular.module('angular-shared/services/review-analyser-endpoint_service', [])
    .factory('analyserService', ($http, $q) => {

        const keywordAnalysisUrl = 'http://127.0.0.1:5000/ask_keyword/';
        const usernameAnalysisUrl = 'http://127.0.0.1:5000/ask_username/';

        const config = (query, isKeywordAnalysis) => {

            return {
                method: 'GET',
                url: isKeywordAnalysis ? keywordAnalysisUrl : usernameAnalysisUrl,
                params: isKeywordAnalysis ? {keyword: query} : {username: query}
            };
        };

        const read = (query, isKeywordAnalysis) => {

            const deferred = $q.defer();

            $http(config(query, isKeywordAnalysis)).then(
                successResponse => {

                    deferred.resolve(successResponse.data);
                },
                errorResponse => {

                    deferred.reject();
                }
            );

            return deferred.promise;
        };

        return {
            readAnalysis: read
        };
    });

