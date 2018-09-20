import frequent

def main():
    personal_website_frequencies = frequent.word_frequencies("https://www.w3schools.com", 25)
    top_word = personal_website_frequencies.most_common(1000)
    print(top_word)

if __name__ == '__main__':
    main()
