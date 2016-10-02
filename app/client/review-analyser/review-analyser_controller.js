/**
 * Created by aml on 01/10/2016.
 */
'use strict';

angular.module('review-analyser_controller', [])
    .controller('AnalyserController', function ($scope, $http) {

        const keywordAnalysisUrl = 'http://127.0.01:5000/ask_keyword/';
        const usernameAnalysisUrl = 'http://127.0.01:5000/ask_username/?keyword=christmas';

        const buildUrlWithQuery = (url, query, isKeyWordAnalysis) => {

            return isKeyWordAnalysis ? url + '?keyword=' + query : url + '?username=' + query;
        };

        const readKeywordAnalysis = query => {

            let result = 'provizoriu rezultat';
            const url = 'http://127.0.01:5000/ask_keyword/';

            const config = {
                method: 'GET',
                url: url,
                params: {keyword: query}
            };

            $http(config).then(function successCallback(response) {
                console.log('intra pe succes');
                result = response.data;
                console.log('rezultat: ' + result);
            }, function errorCallback(response) {
                console.log('intra pe error');
                result = response;
            });

            return result;
        };

        const readUsernameAnalysis = query => {

            $http.get(buildUrlWithQuery(usernameAnalysisUrl, query, false)).then(response => {
                return response.data;
            });
        };

        $scope.keywordAnalysisResult = 'la inceput e asa raspunsu';
        $scope.keyword = '';

        $scope.performKeywordAnalysis = () => {
            console.log('vine rezultatuuuu');
            console.log('resuuult din main: ' + readKeywordAnalysis($scope.keyword));
        };
    });