/**
 * Created by aml on 01/10/2016.
 */
'use strict';

angular.module('review-analyser-endpoint_service', [])
    .factory('reviewAnalyser', ['$http', $http => {
        const url = '';

        const buildUrlWithQuery = (url, query) => {

            return url + '?query=' + query;
        };

        const readAnalysis = query => {

            $http.get(buildUrlWithQuery(url, query)).then(response => {
                return response.data;
            });
        };

        return {
            readAnalysis: readAnalysis
        };
    }]);

