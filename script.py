import requests
from bs4 import BeautifulSoup
import json

def getAll(artists = True, styles = True, output = False):
    base_url = 'http://everynoise.com/'
    result = {}

    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    stylesResult = soup.find_all('div', {'class': 'genre scanme'})

    for style in stylesResult:
        styleNameRaw = style.text
        styleName = styleNameRaw[:-2]
        print(styleName)

        artistLink = style.find('a')['href']
        artistsUrl = base_url + artistLink

        responseArtists = requests.get(artistsUrl)
        artistsPage = BeautifulSoup(responseArtists.text, 'html.parser')
        artistsResult = artistsPage.find_all('div', {'class': 'genre scanme'})

        result[styleName] = {"artists": []}

        for artist in artistsResult:
            artistNameRaw = artist.text
            artistName = artistNameRaw[:-2]
            # print('Artists:', artist_name)
            result[styleName]["artists"].append(artistName)

            # if (artists == true) 

        # print(result)
        # print('Style:', style_name)

    print(result)

    if (output == True):
        name = "all"

        if (artists == True):
            name += "Artists"
        

        if (styles == True): 
            name += "Styles"
        

        with open('allArtistsStyles.json', 'w') as f:
            json.dump(result, f)


getAll(True, True, True)