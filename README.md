## What this is
frequent is a utility for crawling websites and building word frequency list. Mainly made because I wanted to be able to find top n most common words on different websites, but I imagine there might be more useful applications. Or not. 😉

## How to use it
```
import frequent

def main():
    website_word_frequencies = frequent.word_frequencies("https://www.w3schools.com", 25)
    top_words = website_word_frequencies.most_common(500)
    print(top_words)
```
