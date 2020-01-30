#!/usr/bin/env python3

from auspost import search_postcode

#import pytest 

def test_search_sydney_suburb():
    #for data in search_postcode("Sydney"):
    #    print(data.get('state'), data.get('postcode'), data.get('suburb'))
    assert "SYDNEY" in [data.get('suburb') for data in search_postcode("Sydney")]

def test_search_sydney_postcode():
    assert 2000 in [data.get('postcode') for data in search_postcode("Sydney")]
