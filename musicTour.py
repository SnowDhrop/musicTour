import requests
from bs4 import BeautifulSoup
import json

def getAll(styles = True, artists = True, output = False):
    base_url = 'http://everynoise.com/'
    result = {}

    artistsArr = []
    stylesArr = []

    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    stylesResult = soup.find_all('div', {'class': 'genre scanme'})

    def remove_duplicates(lst):
        return list(set(lst))

    def return_result(style, artist, result):
        if (styles == style and artists == artist) :
            return result
        
    def return_json(style, artist, name, newName, result):
            if (styles == style and artists == artist):
                name += newName

                remove_duplicates(result)

                with open(name + ".json", 'w', encoding="utf-8") as f:
                    json.dump(result, f, ensure_ascii=False)
        

    # for styleElement in stylesResult:
    for i, styleElement in enumerate(stylesResult):
        if i == 6:
            break

        styleNameRaw = styleElement.text
        styleName = styleNameRaw[:-2]


        artistLink = styleElement.find('a')['href']
        artistsUrl = base_url + artistLink            


        if (artists == True and styles == True):
            result[styleName] = {"artists": []}


        if (styles == True and artists == False):
            stylesArr.append(styleName)
        

        if (artists == True):
            responseArtists = requests.get(artistsUrl)
            artistsPage = BeautifulSoup(responseArtists.text, 'html.parser')
            artistsResult = artistsPage.find_all('div', {'class': 'genre scanme'}) 

            for artistElement in artistsResult:
                artistNameRaw = artistElement.text
                artistName = artistNameRaw[:-2]

                if (styles == False and artists == True):
                    artistsArr.append(artistName)

                else:
                    result[styleName]["artists"].append(artistName)


        # print(result)
        # print('Style:', style_name)

    # print(result)

    if (output == True):
        name = "all"

        return_json(False, True, name, "Artists", artistsArr)
        return_json(True, False, name, "Styles", stylesArr)
        return_json(True, True, name, "StylesArtists", result)

    else: 
        return_result(False, True, artistsArr)
        return_result(True, False, stylesArr)
        return_result(True, True, result)


getAll(False, True, True)