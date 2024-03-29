
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


from typing import Generator, List, TypedDict, Optional
import requests
from mechanicalsoup import StatefulBrowser # type: ignore


class PostcodeResult(TypedDict):
    """typed dict of results from `search_postcode`"""
    postcode: int
    state: str
    suburb: str

def search_postcode(
    searchterm: str,
    session: Optional[requests.Session]=None,
    ) -> Generator[PostcodeResult, None, None]:
    """ this does a search against the Australia Post site to
    grab postcode/suburb/state data

    params.searchterm: the search string
    type.searchterm: str

    :returns: postcode=int, suburb=str, state=str
    :rtype: dict

    """
    if session is None:
        session = requests.Session()

    browser = StatefulBrowser(
        session=session,
        soup_config={'features': 'lxml'},
        )
    # Uncomment for a more verbose output:
    # browser.set_verbose(2)

    # build the URL for search
    searchurl = f"https://auspost.com.au/postcode/{searchterm.replace(' ', '%20')}"
    print(searchurl)
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
        raise ConnectionError from ConnectionError(f"Failed to open the url '{searchurl}'")
