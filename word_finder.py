import collections
import urllib.request

def download_word_list(url):
    try:
        with urllib.request.urlopen(url) as response:
            text = response.read().decode('utf-8')
            return text.splitlines()
    except Exception as e:
        print(f"Error downloading word list: {e}")
        return None
    
def can_form_word(word, letter_counts):
    word_counts = collections.Counter(word)
    return not (word_counts - letter_counts)
    
def find_longest_word(letters, word_list):
    letter_counts = collections.Counter(letters.lower())
    longest_word = ""
    max_length = 0

    for word in word_list:
        word = word.strip().lower()
        word_length = len(word)

        if word_length <= max_length:
            continue

        if can_form_word(word, letter_counts):
            longest_word = word
            max_length = word_length
        
    return longest_word

def main():
    WORD_LIST_URL = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

    print("Downloading word list...")
    word_list = download_word_list(WORD_LIST_URL)

    if not word_list:
        print("Could not proceed without a word list.")
        return

    print("Word list downloaded successfully.")
    input_letters = input("Enter the letters you have: ")

    result = find_longest_word(input_letters, word_list)

    if result:
        print(f"The longest word you can make is: {result}")
    else:
        print("No word could be made from the letters provided.")

if __name__ == "__main__":
    main()
