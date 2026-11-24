""" test with a connection error """

import pytest
import requests_mock

from auspost import search_postcode


def test_connection_error() -> None:
    """ tests a connection error """

    with pytest.raises(ConnectionError), requests_mock.Mocker() as mocked:
        mocked.get('https://auspost.com.au/postcode/Sydney', exc=ConnectionError)
        result = search_postcode(
            "Sydney",
            )
        for sub in result:
            print(sub)
