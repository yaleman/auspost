from auspost import search_postcode

for data in search_postcode("Sydney"):
    print(data.state, data.postcode, data.suburb)