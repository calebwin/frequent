import frequent

def main():
    personal_website_frequencies = frequent.word_frequencies("https://www.github.com", 100)
    top_word = personal_website_frequencies.most_common(1)
    print(top_word)

if __name__ == '__main__':
    main()
