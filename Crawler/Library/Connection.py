import urllib.request

'''
            # This holds our URL so other methods in this
            have access to this string to manipulate
            # http://www.google.com
        '''
URL_Link = str()

'''
    # This will hold the html code
    #
'''
HTML = str()

'''
    # This user agent will trick the server into thinking that we are a real visitors
    # Remember that this program is considered a bot, or self propagated program.
'''
USER_AGENT = str(
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")

'''
            # This data will be decoded from utf-8 
'''
DECODED_HTML = str()

'''
    # This method goes to websites and 
    # Returns the decoded html form
    # WARNING -> This method is confusing 
'''


def VisitWebPage():
    try:
        # This allows for modification of outer scope variables
        global HTML, URL_Link, DECODED_HTML
        """
            # This is raw data.
            #
        """
        response = urllib.request.Request(URL_Link, headers={'User-Agent': USER_AGENT})

        '''
            # This data will be read
        '''
        HTML_RAW = urllib.request.urlopen(response)

        '''
            # This will contains something like text/html; charset=utf-8
        '''
        charset = HTML_RAW.info().get_content_charset()

        try:
            DECODED_HTML = HTML_RAW.read().decode(charset)
        except:
            try:
                charset = "utf-8"
                DECODED_HTML = HTML_RAW.read().decode(charset)
            except Exception as e:
                DECODED_HTML = ""

        # This is the decoded html that a user can read
        HTML = DECODED_HTML
    except Exception as e:
        DECODED_HTML = ""


def URL(url):
    global URL_Link, HTML

    URL_Link = url
    VisitWebPage()

    return getHTML()


def getHTML():
    global HTML

    return HTML
