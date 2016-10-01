from flask import Flask, request
from flask_restful import Resource, Api
import urllib, json
from pprint import pprint
from siteanalyst import SiteAnalyst

app = Flask(__name__)
api = Api(app)

# user_url = ""
class ReviewAnalyser(Resource):
    def get(self):
        pass

    def post(self):
        user_url = request.form['url']
        #print "This is the url %s" %(user_url)
        composed_url = "https://api.majestic.com/api/json?app_api_key=108B1C29B3B01657B66D2236CDEF1798&cmd=GetBackLinkData&item=%s&Count=15&datasource=fresh" %(user_url)
        #print composed_url
        response = urllib.urlopen(composed_url)
        data = json.loads(response.read())
        #print pprint(data)
        links = []
        for link in data['DataTables']['BackLinks']['Data']:
            links.append(link['SourceURL'])

        return SiteAnalyst.analysis(links)



api.add_resource(ReviewAnalyser, '/')

if __name__ == '__main__':
    app.run(debug=True)
