import wikipediaapi
import os
import sys

filename = sys.argv[1]

# Print all Wikipedia links contained in a page except for pages like "Outline of", "Index of", "Glossary of", etc
def print_links(page):
    links = page.links
    for obj in sorted(links.keys()):

        outlines_condition = obj.startswith('Outline of')
        indices_condition = obj.startswith('Index of')
        glossaries_condition = obj.startswith('Glossary of')
        lists_condition = obj.startswith('List of')

        rand_url_condition = obj.startswith('Outline of') == False and obj.startswith('Index of') == False and obj.startswith('Template:') == False and obj.startswith('Category:') == False and obj.startswith('Wikipedia:') == False and obj.startswith('Template talk:') == False and obj.startswith('Portal:') == False and obj.startswith('List of') == False and obj.startswith('Timeline of') == False and obj.startswith('Glossary of') == False and obj.startswith('Talk:') == False and obj.startswith('Help:') == False and obj.startswith('Lists of') == False and obj.startswith('User:') == False

        current_condition = rand_url_condition

        if current_condition == True:
            print(obj)

# page_py = wiki_wiki.page('Wikipedia:Good articles/Agriculture, food and drink')
# print_links(page_py)



with open(filename) as fp:
  for line in fp:

    title = line.split('\n')[0]
    if os.path.exists(title + '.txt'):
      continue
    print(title)

    wiki_wiki = wikipediaapi.Wikipedia(user_agent='User agent', language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)
    wiki_text = wiki_wiki.page(title)
    
    newtext = wiki_text.text
    newfile = open(title + '.txt', 'w')

    newfile.write(newtext + '\n')
    newfile.close()
