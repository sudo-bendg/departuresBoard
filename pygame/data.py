import requests
import json

import config

def getDeparturesData(stationCode):
    #import requests

    headers = {
        'x-apikey': f'{config.config["API_KEY"]}',
        'Accept': '*/*',
        'User-Agent': 'curl/7.88.1',
    }

    response = requests.get(
        f'https://api1.raildata.org.uk/1010-live-departure-board-dep1_2/LDBWS/api/20220120/GetDepartureBoard/{stationCode}',
        headers=headers,
    )

    #print(response.text)
    responseDict = json.loads(response.text)

    print(responseDict['trainServices'])
    return responseDict['trainServices']