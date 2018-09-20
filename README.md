# frequent
A utility for crawling websites and building frequency lists of words

# Usage
```
import frequent

def main():
    personal_website_frequencies = frequent.word_frequencies("https://www.github.com", 100)
    top_word = personal_website_frequencies.most_common(1)
    print(top_word)
```
