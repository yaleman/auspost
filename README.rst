Australia Post data grabber
===========================

A quick module for searching and pulling suburb data from the Australia Post website.

Usage
-----

Example below, it's pretty simple and yields namedtuples:

    import austpost
    for data in austpost.search_postcode("Sydney"):
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

Errors
------

It'll raise a RunTimeError if something goes wrong with fetching the data