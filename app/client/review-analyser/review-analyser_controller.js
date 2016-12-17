/**
 * Created by aml on 01/10/2016.
 */
'use strict';

angular.module('review-analyser_controller', ['angular-shared/services/review-analyser-endpoint_service'])
    .controller('AnalyserController', function ($scope, analyserService) {

        const readKeywordAnalysis = query => {

            analyserService.readAnalysis(query, true).then(result => {

                $scope.keywordAnalysisResult = result;
                $scope.averagePolarity = $scope.keywordAnalysisResult['AveragePolarity'];
                $scope.mostUsedAdjectives = $scope.keywordAnalysisResult['Data'];
                $scope.loadingAnalysisResult = false;
            }, () => {

                $scope.keywordAnalysisNotAvailable = true;
                $scope.loadingAnalysisResult = false;
            });
        };

        // TODO: Read username analysis

        const resetBeforeSearch = () => {

            $scope.keywordAnalysisResult = undefined;
            $scope.keywordAnalysisNotAvailable = undefined;
            $scope.averagePolarity = undefined;
            $scope.mostUsedAdjectives = undefined;
        };

        // ################################################################################ //

        $scope.loadingAnalysisResult = false;

        $scope.performKeywordAnalysis = () => {
            $scope.keywordToBeShown = $scope.keyword;
            $scope.loadingAnalysisResult = true;
            resetBeforeSearch();
            readKeywordAnalysis($scope.keyword);
        };
    });