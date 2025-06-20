# Word Finder

A multilingual Python tool that finds the longest word you can make from a given set of letters.

## Description

Word Finder downloads comprehensive word lists for different languages and determines the longest possible word that can be formed using only the letters you provide. This is perfect for word games like Scrabble, Words with Friends, or any anagram-based puzzle. Currently supports English and Hungarian languages.

## Features

- Multi-language support: Currently supports English and Hungarian
- Configurable language settings: Easy configuration through JSON files
- Downloads word list from online source automatically
- Finds the longest possible word from your letters
- Case-insensitive matching

## Requirements

- Python 3.6 or higher
- Configuration files: config.json and language files in lang/ directory

## Installation

1. Clone the repository
2. Set up the required configuration files:

## Directory Structure

```
word_finder/
├── word_finder.py
├── config.json
└── lang/
    ├── en.json
    └── hu.json
```

## Configuration Setup

1. Create a `config.json` file:
```json
{
  "language": "en",
  "word_list_url": {
    "en": "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt",
    "hu": "https://raw.githubusercontent.com/your-repo/hungarian-words/master/words.txt"
  }
}
```
2. Create language files in the `lang/` directory:

**lang/en.json:**
```json
{
  "downloading": "Checking for cached word list...",
  "downloaded": "Word list loaded successfully.",
  "download_error": "Could not proceed without a word list.",
  "input_letters": "Enter the letters you have: ",
  "result": "The longest word you can make is: {result}",
  "no_word": "No word could be made from the letters provided."
}
```

## Usage

1. Make sure your configuration files are set up correctly
2. Run the script:
```bash
python word_finder.py
```
2. Wait for the word list to download (this happens once per run)
3. Enter your available letters when prompted:
```en
Enter the letters you have:
```
4. Get your result

## Changing Languages

Edit the `config.json` file and change the `"language"` value:

- `"en"` for English
- `"hu"` for Hungarian

## Examples

### English Mode:

```
Enter the letters you have: hello
The longest word you can make is: hello

Enter the letters you have: python
The longest word you can make is: typhon

Enter the letters you have: abcdef
The longest word you can make is: faced
```

## How It Works

1. **Configuration Loading**: Reads language preferences and word list URLs from `config.json`
2. **Language Setup**: Loads localized strings from the appropriate language file
3. **Download**: Fetches a comprehensive English word list from GitHub
4. **Count**: Creates a frequency count of your available letters
5. **Match**: For each word in the dictionary, checks if it can be formed using your letters. Only considers words longer than the current best match
6. **Return**: Returns the longest valid word found

## Configuration Files

### config.json

Main configuration file containing:

- Current language setting
- Word list URLs for each supported language

### Language Files (lang/*.json)

Individual JSON files for each language containing:

- User interface strings
- Error messages
- Prompts and responses

All text strings are localized and loaded dynamically based on the selected language.

## Word List Source

The script uses the words_alpha.txt file from the dwyl/english-words repository, which contains over 370,000 English words.