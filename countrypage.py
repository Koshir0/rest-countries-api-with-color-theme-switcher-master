from traceback import print_tb
from unittest import result
import requests 
import json 

response_API = requests.get("https://restcountries.com/v3.1/all")
# print(res.status_code)
data = response_API.text
parse_json = json.loads(data)

# result = parse_json["name"]
# print("country Name:", result)
# print(parse_json[0])



# keys:
# postalCode
# name
# tld
# cca2
# ccn3
# cca3
# independent
# status
# unMember
# currencies
# idd
# capital
# altSpellings
# region
# subregion
# languages
# translations
# latlng
# landlocked
# borders
# area
# demonyms
# flag
# maps
# population
# car
# timezones
# continents
# flags
# coatOfArms
# startOfWeek
# capitalInfo



# print all list of the countries
# for i in parse_json:
#     print("Flag: " + i["flag"])
#     print( i["name"]["common"].capitalize() )
#     print("Population: " + str(i["population"]))
#     print("Region: " + i["region"])
#     print("Capital: " + i["capital"][0])
#     print("#####################")
   


for i in parse_json:
    print("Flag: " + i["flag"])
    print( i["name"]["common"].capitalize() )
    print( i["name"]["nativeName"] )
    print("Population: " + str(i["population"]))
    print("Region: " + i["region"])
    print("sub region: " + i["subregion"])
    print("Capital: " + i["capital"][0])
    print("currencies: " +str( i["currencies"]))
    print("languages: " + str(i["languages"]))
    print("border countries: " +str( i["borders"])) 
    print("Top level Domain: " +str( i["tld"]))
    print("#####################")