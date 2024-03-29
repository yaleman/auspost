# Australia Post data grabber

A quick module for searching and pulling suburb data from the Australia Post website.

# Usage

Example below, it's pretty simple and yields namedtuples:

    import auspost
    for data in auspost.search_postcode("Sydney"):
         print(data)
    AusPostData(postcode='2055', suburb='NORTH SYDNEY', state='NSW')
    AusPostData(postcode='2059', suburb='NORTH SYDNEY', state='NSW')
    AusPostData(postcode='2060', suburb='NORTH SYDNEY', state='NSW')
    AusPostData(postcode='2060', suburb='NORTH SYDNEY SHOPPINGWORLD', state='NSW')
    AusPostData(postcode='2001', suburb='SYDNEY', state='NSW')
    AusPostData(postcode='2000', suburb='SYDNEY', state='NSW')
    AusPostData(postcode='2020', suburb='SYDNEY DOMESTIC AIRPORT', state='NSW')
    AusPostData(postcode='2020', suburb='SYDNEY INTERNATIONAL AIRPORT', state='NSW')
    AusPostData(postcode='2129', suburb='SYDNEY MARKETS', state='NSW')
    AusPostData(postcode='2127', suburb='SYDNEY OLYMPIC PARK', state='NSW')
    AusPostData(postcode='1235', suburb='SYDNEY SOUTH', state='NSW')
    AusPostData(postcode='2000', suburb='SYDNEY SOUTH', state='NSW')
    AusPostData(postcode='2006', suburb='SYDNEY UNIVERSITY', state='NSW')
    AusPostData(postcode='2006', suburb='THE UNIVERSITY OF SYDNEY', state='NSW')
    AusPostData(postcode='1466', suburb='UNSW SYDNEY', state='NSW')

# Errors

It'll raise a RunTimeError if something goes wrong with fetching the data

# Changelog

* 2019-11-16 - Changed from a namedtuple response to a dict because... I don't even know why I was returning them at the time.
* 2021-01-23 - Fixed example code typo
* 2022-03-28 - Adding typing, bumped to 0.0.10
* 2022-06-04 - v0.0.11 - Added more typing, more testing.