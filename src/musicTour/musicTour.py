# Copyright (c) [année] [titulaire du droit d'auteur]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

        if (styles == True and artists == False):
            name += "Styles"
            remove_duplicates(stylesArr)

            with open(name + ".json", 'w', encoding="utf-8") as f:
                    json.dump(stylesArr, f, ensure_ascii=False)

        elif (styles == False and artists == True):
            name += "Artists"
            remove_duplicates(artistsArr)

            with open(name + ".json", 'w', encoding="utf-8") as f:
                    json.dump(artistsArr, f, ensure_ascii=False)

        elif (styles == True and artists == True):
            name += "StylesArtists"
            remove_duplicates(result)

            with open(name + ".json", 'w', encoding="utf-8") as f:
                    json.dump(result, f, ensure_ascii=False)

    else: 
        if (styles == True and artists == False) :
            return stylesArr        
        
        elif (styles == False and artists == True) :
            return artistsArr    
        
        elif (styles == True and artists == True) :
            return result    

getAll(True, True, True)