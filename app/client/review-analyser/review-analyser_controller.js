/**
 * Created by aml on 01/10/2016.
 */
'use strict';

angular.module('review-analyser_controller', [])
    .controller('AnalyserController', function ($scope, $http) {

        const keywordAnalysisUrl = 'http://127.0.0.1:5000/ask_keyword/';
        const usernameAnalysisUrl = 'http://127.0.0.1:5000/ask_username/';

        const buildUrlWithQuery = (url, query, isKeyWordAnalysis) => {

            return isKeyWordAnalysis ? url + '?keyword=' + query : url + '?username=' + query;
        };

        const readKeywordAnalysis = query => {

            const url = 'http://127.0.0.1:5000/ask_keyword/';

            const config = {
                method: 'GET',
                url: url,
                params: {keyword: query}
            };

            $http(config).then(function successCallback(response) {
                console.log('intra pe succes');
                $scope.keywordAnalysisResult = response.data;
                $scope.averagePolarity = $scope.keywordAnalysisResult['AveragePolarity'];
                $scope.mostUsedAdjectives = $scope.keywordAnalysisResult['Data'];
                $scope.loadingAnalysisResult = false;
            }, function errorCallback(response) {
                console.log('intra pe error');
                $scope.keywordAnalysisResult = response.data;
                $scope.loadingAnalysisResult = false;
            });
        };

        const readUsernameAnalysis = query => {

            $http.get(buildUrlWithQuery(usernameAnalysisUrl, query, false)).then(response => {
                return response.data;
            });
        };

        $scope.loadingAnalysisResult = false;

        $scope.performKeywordAnalysis = () => {
            $scope.loadingAnalysisResult = true;
            readKeywordAnalysis($scope.keyword);
        };
    });