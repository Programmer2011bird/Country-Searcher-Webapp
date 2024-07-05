from typing import Any
import requests
import pandas as pd


def Get_Json(Url_Endpoint: str) -> dict[str, str]:
    # NOTE: The API Being Used Doesn't Require An API Key
    URL: str = f"https://restcountries.com/v3.1/{Url_Endpoint}"
    # Getting The Response From The API
    RESPONSE: requests.Response = requests.get(URL)
    JSON: Any = RESPONSE.json()
    AMOUNT_OF_COUNTRIES: int = int(len(JSON))
    # Place Holder Dictionary
    INFO: dict[str, list] = {
        "common_name": [],
        "official_name": [],
        "capital_city": [],
        "population": [],
        "languages": [],
        "currencies": [],
        "continents": [],
        "timezones": [],
        "is_UN_member": [],
        "driving_side": [],
        "start_of_week": []
    }
    # If There Is A Large Or Bigger Than 0 DataSet ( Zero Because Lists Start At 0 ) It Means We Need To Iterate Through It
    if AMOUNT_OF_COUNTRIES > 0:
        for i in range(AMOUNT_OF_COUNTRIES):
            # This Method Can Look Strange But When We Turn It Into An Pandas DataFrame The Messiness And Confusedness Will Go Away
            NAME_COMMON: str = str(JSON[i]["name"]["common"])
            INFO["common_name"].append(NAME_COMMON)

            NAME_OFFICIAL: str = str(JSON[i]["name"]["official"])
            INFO["official_name"].append(NAME_OFFICIAL)
            
            CAPITAL: str = str(JSON[i]["capital"])
            INFO["capital_city"].append(CAPITAL)
            
            POPULATION: str = str(JSON[i]["population"])
            INFO["population"].append(POPULATION)
            
            LANGUAGES: str = str(JSON[i]["languages"])
            INFO["languages"].append(LANGUAGES)
            
            CURRENCIES: str = str(JSON[i]["currencies"])
            INFO["currencies"].append(CURRENCIES)
            
            CONTINENTS: str = str(JSON[i]["continents"])
            INFO["continents"].append(CONTINENTS)
            
            TIMEZONES: str = str(JSON[i]["timezones"])
            INFO["timezones"].append(TIMEZONES)
            
            UN_MEMBER: str = str(JSON[i]["unMember"])
            INFO["is_UN_member"].append(UN_MEMBER)
            
            DRIVING_SIDE: str = str(JSON[i]["car"]["side"])
            INFO["driving_side"].append(DRIVING_SIDE)
            
            START_OF_WEEK: str = str(JSON[i]["startOfWeek"])
            INFO["start_of_week"].append(START_OF_WEEK)
    # If We Didn't Have A Bigger Than 0 DataSet It Means We Don't Need To Iterate Through It
    else:
        NAME_COMMON: str = str(JSON[0]["name"]["common"])
        INFO["common_name"].append(NAME_COMMON)

        NAME_OFFICIAL: str = str(JSON[0]["name"]["official"])
        INFO["official_name"].append(NAME_OFFICIAL)
        
        CAPITAL: str = str(JSON[0]["capital"])
        INFO["capital_city"].append(CAPITAL)
        
        POPULATION: str = str(JSON[0]["population"])
        INFO["population"].append(POPULATION)
        
        LANGUAGES: str = str(JSON[0]["languages"])
        INFO["languages"].append(LANGUAGES)
        
        CURRENCIES: str = str(JSON[0]["currencies"])
        INFO["currencies"].append(CURRENCIES)
        
        CONTINENTS: str = str(JSON[0]["continents"])
        INFO["continents"].append(CONTINENTS)
        
        TIMEZONES: str = str(JSON[0]["timezones"])
        INFO["timezones"].append(TIMEZONES)
        
        UN_MEMBER: str = str(JSON[0]["unMember"])
        INFO["is_UN_member"].append(UN_MEMBER)
        
        DRIVING_SIDE: str = str(JSON[0]["car"]["side"])
        INFO["driving_side"].append(DRIVING_SIDE)
        
        START_OF_WEEK: str = str(JSON[0]["startOfWeek"])
        INFO["start_of_week"].append(START_OF_WEEK)
        
    # Turning The Dictionary Into A Pandas DataFrame And Then Making It Html-Like And Adding Bootstrap For Better UI
    html_Table: str = pd.DataFrame(INFO).to_html(classes="table table-dark table-bordered table-hover")
    
    return f"""
        <head>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
            integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
        </head>
        <body class="bg-dark text-light">
            <div class="container-fluid p-2">
                {html_Table}
            </div>
        </body>"""
