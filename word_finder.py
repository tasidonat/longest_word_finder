import collections
import urllib.request
import json
import os

def load_config():
    try:
        with open("config.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading config: {e}")
        return {"language": "en"}
    
def load_lang_strings(language):
    lang_path = os.path.join("lang", f"{language}.json")
    with open(lang_path, "r", encoding="utf-8") as file:
        return json.load(file)

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
    config = load_config()
    language = config.get("language", "en")
    word_list_url = config.get("word_list_url", {}).get(language)

    if not word_list_url:
        print(lang_strings["bad_url_link"].format(language=language))
        return

    lang_strings = load_lang_strings(language)

    print(lang_strings["downloading"])
    word_list = download_word_list(word_list_url)

    if not word_list:
        print(lang_strings["download_error"])
        return

    print(lang_strings["downloaded"])
    input_letters = input(lang_strings["input_letters"])

    result = find_longest_word(input_letters, word_list)

    if result:
        print(lang_strings["result"].format(result=result))
    else:
        print(lang_strings["no_word"])

if __name__ == "__main__":
    main()
