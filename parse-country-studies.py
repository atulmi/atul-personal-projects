# Goal of this program: parse a Country Study book for a given country (published by Library of Congress) into a text file
# As a command-line argument, provide the name of the country as given in the URL for that country, on the website http://countrystudies.us

# Example usage for https://countrystudies.us/germany:
# python3 parse-country-studies.py germany

import requests
import sys
from bs4 import BeautifulSoup

baseUrl = "http://countrystudies.us" # base URL for the Country Studies website
response = requests.get(baseUrl)

countryName = sys.argv[1] # Country whose study we need to parse from website
origResponse = requests.get("https://countrystudies.us/" + countryName + '/')

parsedCountryPage = BeautifulSoup(origResponse.text, 'html.parser')
countryLinks = parsedCountryPage.find_all('a') # Sub-links within a Country's page containing text

# if only 1 link in main Country page, we were likely redirected to a "page not found" page
if len(countryLinks) == 1:
    print("URL doesn't exist, please enter a valid Country name (see the end of the Country's URL in the relevant countrystudies.us page)")
    sys.exit()

finalCountryText = '' # contains full text of the Country Study, saved to a text file at the end

for countryLink in countryLinks:
    print("countryLink here: ", countryLink) # print sub-link of Country Page, to indicate progress (helps us make sure the request isn't frozen)

    if countryLink.get('href') == None:
        continue


    if "#" in countryLink.get('href'):
        continue

    countryResponse = requests.get(countryLink.get('href'))
    responseSoup = BeautifulSoup(countryResponse.content, 'html.parser') # Parsed text from the sub-link in Country page


    # Find all paragraphs in sub-link page's HTML, write to file
    for p_tag in responseSoup.find_all('p'):

        # sometimes, page has a parent <p> tag containing other <p> tags, causing duplication of many paragraphs since we're concatenating text from all <p> tags
        # So, ensure there's no <p> parent to avoid duplication
        if p_tag.name == 'p' and p_tag.parent.name != 'p':
            finalCountryText += p_tag.get_text() + '\n\n'

    countryFile = open(countryName + '.txt', 'wb')
    countryFile.write(finalCountryText.encode())
    countryFile.close()
            
        
