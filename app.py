import requests 
import json 
from flask import Flask , render_template, url_for, request


app = Flask(__name__)


response_API = requests.get("https://restcountries.com/v3.1/all")
# print(res.status_code)
data = response_API.text
parse_json = json.loads(data)




            

@app.route("/")
def index():
    return render_template("index.html", countries = parse_json)


@app.route('/details/<name>')
def details(name):
    country = name
    # print(country)
    # https://restcountries.com/v3.1/name/country
    response_API = requests.get(f"https://restcountries.com/v3.1/name/{country}")
    # print(res.status_code)
    data = response_API.text
    parse_json = json.loads(data)

    # globale variables
    flag="flag"
    name="name"
    nativeName="nativeName"
    population="population"
    region="region"
    subregion="subregion"
    capital="capital"
    currency=[]
    Border=[]
    langs=[]
    tld=[]

    # func to get the code of the country 
    def getCode(code):
        # https://restcountries.com/v3.1/alpha/arg
        response_API = requests.get(f"https://restcountries.com/v3.1/name/{code}")
        data = response_API.text
        parse_json = json.loads(data)
        for i in parse_json:
            Border.append(i["name"]["common"].capitalize()) 


 
    
    # main loop for all variables
    for i in parse_json:
        try:
            # print("Flag: " + i["flags"]["png"])
            flag = i["flags"]["png"]
        except:
            print("Flag: ")
        try:
            # print( "Country:" + i["name"]["common"].capitalize() )
            name = i["name"]["common"].capitalize()
        except:
            print("Country: ")
        try:
            for key in i["name"]["nativeName"]:
                # print("NativeName: " + i["name"]["nativeName"][key]["common"])
                nativeName = i["name"]["nativeName"][key]["common"]
            
        except:
            print("native name: ")
        try:
            # print("Population: " + str(i["population"]))
            population = i["population"]
        except:
            print("Population")
        try:
            # print("Region: " + i["region"])
            region = i["region"]
        except:
            print("Region: ")
        try:
            # print("sub region: " + i["subregion"])
            subregion = i["subregion"]
        except:
            print("sub region")
        try:
            # print("Capital: " + i["capital"][0])
            capital = i["capital"][0]
            
        except:
            print("capital")
        try:
            for key in i["currencies"]:
                # print("currencies: " + str( i["currencies"][key]["name"]))
                currency.append(i["currencies"][key]["name"])
            # print(currency)
        except:
            print("currency")
        try:
            for border in i["borders"]:
                # print("border countries: " + border) 
                getCode(border)  
        except:
            
            print("An exception occurred")
        try:
            for lang in i["languages"]:
                print("languages: " + lang)
                response_API = requests.get(f"https://restcountries.com/v3.1/lang/{lang}")
                data = response_API.text
                parse_json = json.loads(data)
                print(parse_json[0]["languages"].get(lang))
                langs.append(parse_json[0]["languages"].get(lang))
        except:
            print("languages")

        try:
            for i in i["tld"]:
                # print("Top level Domain: " +str( i))
                tld.append( i)
            # print(tld)
        except:
            print("###")
  
    print(langs)
    return render_template("details.html", flag=flag, name=name, nativeName=nativeName, population=population,
                            region=region, subregion=subregion,langs=langs, tld=tld, border=Border, capital=capital,currency=currency)







@app.route("/search", methods=['POST'])
def search():
    region = request.form['region']
    response_API = requests.get(f"https://restcountries.com/v3.1/region/{region}")
    data = response_API.text
    parse_json = json.loads(data)
    # https://restcountries.com/v3.1/region/europe
    return render_template("index.html", countries=parse_json)


@app.route("/searchbyname", methods=['POST'])
def searchbyname():
    search = request.form['search']
    
    response_API = requests.get(f"https://restcountries.com/v3.1/name/{search}")
    data = response_API.text
    parse_json = json.loads(data)
    if search == "israel":
        print(search)
        render_template("nothing.html")
    # https://restcountries.com/v3.1/region/europe
    return render_template("index.html", countries=parse_json)
    




# print all list of the countries
# for i in parse_json:
#     print("Flag: " + i["flag"])
#     print( i["name"]["common"].capitalize() )
#     print("Population: " + str(i["population"]))
#     print("Region: " + i["region"])
#     print("Capital: " + i["capital"][0])
#     print("#####################")





# for i in parse_json:
#     try:
#         print("Flag: " + i["flag"])
#     except:
#         print("Flag: ")
#     try:
#         print( i["name"]["common"].capitalize() )
#     except:
#         print("Country: ")
#     try:
#         print( i["name"]["nativeName"] )
#     except:
#         print("native name: ")
#     try:
#         print("Population: " + str(i["population"]))
#     except:
#         print("Population")
#     try:
#         print("Region: " + i["region"])
#     except:
#         print("Region")
#     try:
#         print("sub region: " + i["subregion"])
#     except:
#         print("sub region")
#     try:
#         print("Capital: " + i["capital"][0])
#     except:
#         print("capital")
#     try:
#         print("currencies: " +str( i["currencies"]))
#     except:
#         print("currency")
#     try:
#         print("border countries: " +str( i["borders"])) 
#     except:
#         print("An exception occurred")
#     try:
#         print("languages: " + str(i["languages"]))
#     except:
#         print("languages")
#     try:
#         print("Top level Domain: " +str( i["tld"]))
#     except:
#         print("#####################")


if __name__ == "__main__":
    app.run()