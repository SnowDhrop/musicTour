import requests
from bs4 import BeautifulSoup
import json

def getAll(artists = null, styles = null, json = null):
    base_url = 'http://everynoise.com/'
    result = {}

    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    styles = soup.find_all('div', {'class': 'genre scanme'})

    for style in styles:
        styleNameRaw = style.text
        styleName = styleNameRaw[:-2]
        print(styleName)

        artistLink = style.find('a')['href']
        artistsUrl = base_url + artistLink

        responseArtists = requests.get(artistsUrl)
        artistsPage = BeautifulSoup(responseArtists.text, 'html.parser')
        artists = artistsPage.find_all('div', {'class': 'genre scanme'})

        result[styleName] = {"artists": []}

        for artist in artists:
            artistNameRaw = artist.text
            artistName = artistNameRaw[:-2]
            # print('Artists:', artist_name)
            result[styleName]["artists"].append(artistName)

        # print(result)
        # print('Style:', style_name)

    print(result)
    with open('all.json', 'w') as fichier:
        json.dump(result, fichier)


