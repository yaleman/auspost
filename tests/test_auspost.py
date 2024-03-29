"""test the auspost module"""

from auspost import search_postcode

def test_search_sydney_suburb() -> None:
    """ tests a basic sydney search
        for data in search_postcode("Sydney"):
            print(data.get('state'), data.get('postcode'), data.get('suburb'))
    """
    assert "SYDNEY" in [data.get('suburb') for data in search_postcode("Sydney")]

def test_search_sydney_postcode() -> None:
    """ searching for sydney postcodes """
    assert 2000 in [data.get('postcode') for data in search_postcode("Sydney")]
