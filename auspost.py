
"""
Copyright 2017 James Hodgkinson

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
"""

try:
    from mechanicalsoup import StatefulBrowser
except ImportError as error_message:
    IMPORTMESSAGE = "Failure while loading auspost module's dependencies: {}".format(error_message)
    raise ImportError(IMPORTMESSAGE)


def search_postcode(searchterm: str):
    """ this does a search against the Australia Post site to
    grab postcode/suburb/state data

    params.searchterm: the search string
    type.searchterm: str

    :returns: postcode=int, suburb=str, state=str
    :rtype: dict

    """
    browser = StatefulBrowser(soup_config={'features': 'lxml'})
    # Uncomment for a more verbose output:
    # browser.set_verbose(2)

    # build the URL for search
    searchurl = "https://auspost.com.au/postcode/{}".format(searchterm.replace(' ', '%20'))

    # grab the page
    try:
        browser.open(searchurl)
        # get the page contents
        page = browser.get_current_page()
        # find the lis within the ol
        lis = page.find_all('ol')[0].find_all('li')
        # pull out the data
        data_lis = [li for li in lis if 'id="result' in str(li)]
        for list_element in data_lis:
            # this is the data found in June 2017
            #<span class="suburb-map-postcode">POSTCODE</span>
            #<h2>SUBURB, STATE</h2>
            postcode = list_element.find_all('span')
            if postcode:
                postcode = postcode[0].contents[0]
                secondfield = list_element.find_all('h2')
                if secondfield:
                    suburb, state = secondfield[0].contents[0].split(",")
                    if postcode and state.strip() and suburb.strip():
                        yield {
                            'postcode' : int(postcode),
                            'state' : state.strip(),
                            'suburb' : suburb.strip(),
                        }
    except Exception:
        raise ConnectionError("Failed to open the url '{}'".format(searchurl))
