""" test with a connection error """

import requests_mock
import pytest

from auspost import search_postcode



def test_connection_error() -> None:
    """ tests a connection error """

    with pytest.raises(ConnectionError):

        with requests_mock.Mocker() as mocked:
            mocked.get('https://auspost.com.au/postcode/Sydney', exc=ConnectionError)
            result = search_postcode(
                "Sydney",
                )
            for sub in result:
                print(sub)
