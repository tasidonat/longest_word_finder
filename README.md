# Word Finder

A Python tool that finds the longest word you can make from a given set of letters.

## Description

Word Finder downloads a comprehensive English word list and determines the longest possible word that can be formed using only the letters you provide. This is perfect for word games like Scrabble, Words with Friends, or any anagram-based puzzle.

## Features

- Downloads word list from online source automatically
- Finds the longest possible word from your letters
- Case-insensitive matching

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository

No additional packages required! The script uses only Python standard library modules:

- collections
- urllib.request

## Usage

1. Run the script:
```bash
python word_finder.py
```
2. Wait for the word list to download (this happens once per run)
3. Enter your available letters when prompted:
```
Enter the letters you have:
```
4. Get your result

## Examples

```
Enter the letters you have: hello
The longest word you can make is: hello

Enter the letters you have: python
The longest word you can make is: typhon

Enter the letters you have: abcdef
The longest word you can make is: faced
```

## How It Works

1. **Download**: Fetches a comprehensive English word list from GitHub
2. **Count**: Creates a frequency count of your available letters
3. **Match**: For each word in the dictionary, checks if it can be formed using your letters. Only considers words longer than the current best match
4. **Return**: Returns the longest valid word found

## Word List Source

The script uses the words_alpha.txt file from the dwyl/english-words repository, which contains over 370,000 English words.