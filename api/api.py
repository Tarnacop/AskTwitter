from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import urllib, json
from twitterutils import TwitterUtils
import requests

app = Flask(__name__)
api = Api(app)

class AskKeyword(Resource):

    @app.after_request
    def add_cors_headers(response):
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5000')
        return response

    def get(self):
        """Resolves the get request"""
        keyword = request.args.get('keyword')

        twitter_results = TwitterUtils.getTweets(keyword)
        dictionaries_list = []
        count = 0
        for twitter_result in twitter_results:

            tweet_url = "http://twitter.com/%s/status/%s" %(twitter_result['user']['screen_name'], twitter_result['id'])
            majestic_url = "https://api.majestic.com/api/json?app_api_key=108B1C29B3B01657B66D2236CDEF1798&cmd=GetBackLinkData&item=%s&Count=0&datasource=fresh"%(tweet_url)
            majestic_response = urllib.urlopen(majestic_url)
            majestic_results = json.loads(majestic_response.read())
            dictionary_result = {}
            dictionary_result['TweetText'] = twitter_result['text']
            dictionary_result['TotalBackLinks'] = majestic_results['DataTables']['BackLinks']['Headers']['TotalBackLinks']
            dictionaries_list.append(dictionary_result)
            count = count + 1
            if count==50:
                break

        print len(dictionaries_list) #To be delted
        dictionaries_list = sorted(dictionaries_list, key=lambda dictionary: dictionary['TotalBackLinks'], reverse = True)

        polarity_sum = 0.0
        polarity_num = len(dictionaries_list)
        magnitude_sum = 0.0

        adjs = {}

        count = 0
        for dictionary in dictionaries_list:

            google_url = "https://language.googleapis.com/v1beta1/documents:annotateText?key=AIzaSyBD_FPfn7HQ1y2iIcnC2j4u6hHts_MRhWs"
            google_json = {"document": {"content": "%s"%(dictionary['TweetText']), "type": "PLAIN_TEXT"}, "features": {"extractDocumentSentiment": "true", "extractEntities": "false", "extractSyntax": "true"}}
            r = requests.post(google_url, data = json.dumps(google_json))
            google_data = r.json()
            if not 'error' in google_data:
                polarity_sum = polarity_sum + google_data['documentSentiment']['polarity']
                magnitude_sum = magnitude_sum + google_data['documentSentiment']['magnitude']
                for token in google_data['tokens']:
                    if token['partOfSpeech']['tag'] == 'ADJ':
                        if token['text']['content'] in adjs:
                            adjs[token['text']['content']] = adjs[token['text']['content']] + 1
                        else:
                            adjs[token['text']['content']] = 1
            else:
                polarity_num = polarity_num - 1

            count = count + 1
            if count==25:
                break

        average_polarity = polarity_sum / polarity_num
        average_polarity = (average_polarity + 1) / 2 * 100

        print average_polarity #To be deleted
        print magnitude_sum #To be deleted

        adjs_list = []

        for adj in adjs:
            adjs_list.append({'number': adjs[adj], 'adjective': adj})

        adjs_list = sorted(adjs_list, key = lambda adj: adj['number'], reverse = True)

        #To be deleted
        for adj in adjs_list:
            print str(adj['number']) + ' ' + adj['adjective']

        final_dictionary = {}
        final_dictionary['AveragePolarity'] = average_polarity
        final_dictionary['Magnitude'] = magnitude_sum
        aux_dictionary = {}

        count = 0;
        for adj in adjs_list:
            aux_dictionary[adj['adjective']] = adj['number']
            count = count + 1
            if count == 10:
                break

        final_dictionary['Data'] = aux_dictionary
        return jsonify(final_dictionary)

class AskUsername(Resource):
    def get(self):
        """Resolves the get request"""
        username = request.args.get('username')

        tweet_url = "http://twitter.com/%s" %(username)

        majestic_url = "https://api.majestic.com/api/json?app_api_key=108B1C29B3B01657B66D2236CDEF1798&cmd=GetBackLinkData&item=%s&Count=0&datasource=fresh"%(tweet_url)
        majestic_response = urllib.urlopen(majestic_url)
        majestic_results = json.loads(majestic_response.read())
        majestic_total_back_links = majestic_results['DataTables']['BackLinks']['Headers']['TotalBackLinks']

        twitter_results = TwitterUtils.getUserTimeline(username)

        dictionaries_list = []
        count = 0
        for twitter_result in twitter_results:
            dictionaries_list.append(twitter_result['text'])
            count = count + 1
            if count==100:
                break

        polarity_sum = 0.0
        polarity_num = len(dictionaries_list)
        magnitude_sum = 0.0

        adjs = {}

        count = 0
        for dictionary in dictionaries_list:

            google_url = "https://language.googleapis.com/v1beta1/documents:annotateText?key=AIzaSyBD_FPfn7HQ1y2iIcnC2j4u6hHts_MRhWs"
            google_json = {"document": {"content": "%s"%(dictionary), "type": "PLAIN_TEXT"}, "features": {"extractDocumentSentiment": "true", "extractEntities": "false", "extractSyntax": "true"}}
            r = requests.post(google_url, data = json.dumps(google_json))
            google_data = r.json()
            if not 'error' in google_data:
                polarity_sum = polarity_sum + google_data['documentSentiment']['polarity']
                magnitude_sum = magnitude_sum + google_data['documentSentiment']['magnitude']
                for token in google_data['tokens']:
                    if token['partOfSpeech']['tag'] == 'ADJ':
                        if token['text']['content'] in adjs:
                            adjs[token['text']['content']] = adjs[token['text']['content']] + 1
                        else:
                            adjs[token['text']['content']] = 1
            else:
                polarity_num = polarity_num - 1

        average_polarity = polarity_sum / polarity_num
        average_polarity = (average_polarity + 1) / 2 * 100

        adjs_list = []

        for adj in adjs:
            adjs_list.append({'number': adjs[adj], 'adjective': adj})

        adjs_list = sorted(adjs_list, key = lambda adj: adj['number'], reverse = True)

        final_dictionary = {}
        final_dictionary['TotalBackLinks'] = majestic_total_back_links
        final_dictionary['AveragePolarity'] = average_polarity
        final_dictionary['Magnitude'] = magnitude_sum
        aux_dictionary = {}

        count = 0;
        for adj in adjs_list:
            aux_dictionary[adj['adjective']] = adj['number']
            count = count + 1
            if count == 9:
                break

        final_dictionary['Data'] = aux_dictionary
        return final_dictionary

api.add_resource(AskKeyword, '/ask_keyword/')
api.add_resource(AskUsername, '/ask_username/')
if __name__ == '__main__':
    app.run(debug=True)
