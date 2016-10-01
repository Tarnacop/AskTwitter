import urllib2

class SiteAnalyst():

    @staticmethod
    def analysis(urls):
        for url in urls:
            if SiteAnalyst.isReview(url):
                SiteAnalyst.processReview(url)
                #TODO
        return True

    @staticmethod
    def isReview(url):
        if url == "http://www.androidauthority.com/best-android-games-316202/":
            return True

    @staticmethod
    def processReview(url):
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}
        req = urllib2.Request(url, headers = hdr)
        try:
            response = urllib2.urlopen(req)
            the_page = response.read()
            print the_page
        except urllib2.HTTPError, e:
            print e.fp.read()
        # return "Very good app"
