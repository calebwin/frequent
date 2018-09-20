import re

from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
from collections import Counter

class LinkParser(HTMLParser):

    # adds links to a maintained list
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href' and value.startswith("/") and value.find("css") == -1 and value.find("js") == -1:
                    newUrl = parse.urljoin(self.base_url, value)
                    self.links = self.links + [newUrl]

    # returns links
    def get_links(self, url):
        self.links = []
        self.base_url = url

        response = urlopen(url)
        html_bytes = response.read()
        html_string = html_bytes.decode("utf-8")

        self.feed(html_string)
        return html_string, self.links

def remove_between(document, start_str, end_str):
    while start_str in document and end_str in document:
        start_str_index = document.find(start_str)
        end_str_index = document.find(end_str, start_str_index) + len(end_str) - 1
        document = document[0 : start_str_index] + document[end_str_index + 1 : len(document)]
    return document

def word_frequencies(website_url, max_pages):
    pages_to_visit = [website_url]
    number_visited = 0
    found_words = []

    while number_visited < max_pages and pages_to_visit != []:
        number_visited = number_visited +1

        url = pages_to_visit[0]
        pages_to_visit = pages_to_visit[1:]
        try:
            parser = LinkParser()
            data, links = parser.get_links(url)
            data = remove_between(data, "<script>", "</script>")
            data = remove_between(data, "<style>", "</style>")
            data = remove_between(data, "<", ">")
            words = re.sub("[^\w]", " ",  data).split()
            found_words.extend(words)
            pages_to_visit = pages_to_visit + links
        except:
            print("Failed")

    found_word_frequencies = Counter(found_words)

    return found_word_frequencies
