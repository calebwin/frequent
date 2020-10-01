#for better use read and understand it carefully

# Frequent
frequent is a utility for crawling websites and building word frequency list. Mainly made because I wanted to be able to find top n most common words on different websites, but I imagine there might be more useful applications. Or not. 

```python
import frequent

# get most frequent words from the w3schools website
# limit crawl depth to 25
word_frequencies = frequent.word_frequencies("https://www.w3schools.com", 25)

# get the top 50 words
top_words = website_word_frequencies.most_common(50)

# print the top 50 most frequent words
print(top_words)
```
