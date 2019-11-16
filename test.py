from auspost import search_postcode

for data in search_postcode("Sydney"):
    print(data.get('state'), data.get('postcode'), data.get('suburb'))