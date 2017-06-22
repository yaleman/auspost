try:
    from collections import namedtuple
    import mechanicalsoup
except ImportError as e:
    exit(e)

AusPostData = namedtuple('AusPostData', ['postcode', 'suburb', 'state'])

def search_postcode(searchterm : str):
    """ this does a search against the Australia Post site to 
    grab postcode/suburb/state data and returns a namedtuple 
    AusPostData(postcode=int, suburb=str, state=str)
    """
    browser = mechanicalsoup.StatefulBrowser(soup_config={'features': 'lxml'})
    # Uncomment for a more verbose output:
    # browser.set_verbose(2)

    # build the URL for search
    searchurl = "http://auspost.com.au/postcode/{}".format(searchterm.replace(' ', '%20'))

    # grab the page
    try:
        browser.open(searchurl)
    except:
        raise RuntimeError("Failed to open the url '{}'".format(searchurl))
    # get the page contents
    page = browser.get_current_page()

    # find the ol
    ols = page.find_all('ol')
    # find the lis within the ol
    lis = ols[0].find_all('li')
    # pull out the data
    for li in lis:
        # this is in the li tag
        if 'id="result' in str(li):
            # this is the data found in June 2017
            #<span class="suburb-map-postcode">POSTCODE</span>
            #<h2>SUBURB, STATE</h2>
            postcode = li.find_all('span')
            if postcode:
                postcode = postcode[0].contents[0]
                secondfield = li.find_all('h2')
                if secondfield:
                    suburb, state = secondfield[0].contents[0].split(",")
                    suburb, state = suburb.strip(), state.strip()
                    if postcode and state and suburb:
                        yield AusPostData(postcode=int(postcode), state=state, suburb=suburb)
                
if __name__ == '__name__':
    for data in search_postcode("Sydney"):
        print(data.state, data.postcode, data.suburb)