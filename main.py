import random
import enchant
import nltk
nltk.download('words')
nltk.download('wordnet')
nltk.download('omw-1.4')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


dictionary = enchant.Dict('en_US')
wordlist = nltk.corpus.words.words()
fiveLetterWords = [word for word in wordlist if len(word) == 5]
fiveLetterWordSet = frozenset(fiveLetterWords)

randomIndex = random.randint(0, len(fiveLetterWords) - 1)
selectedWord = fiveLetterWords[randomIndex]
syns = nltk.corpus.wordnet.synsets(selectedWord)

while len(syns) == 0 or selectedWord[0].isupper():
    randomIndex = random.randint(0, len(fiveLetterWords) - 1)
    selectedWord = fiveLetterWords[randomIndex]
    syns = nltk.corpus.wordnet.synsets(selectedWord)
definition = syns[0].definition()
examples = syns[0].examples()

""" DEBUG
print("Selected word: ", selectedWord)
print("Definition: ", definition)
if len(examples) > 0:
    print("Usage examples: ")
    for ex in examples:
        print(ex)
"""

if __name__ == '__main__':
    guessLayers = ['[ ] [ ] [ ] [ ] [ ]'] * 5
    currentGuess = ''
    selectedWord = selectedWord.upper()
    i = 0
    while i < 5 and currentGuess != selectedWord:
        for guess in guessLayers:
            print(guess)
        currentGuess = input("Input 5-letter word guess: ").lower()
        while len(currentGuess) != 5 or (currentGuess not in fiveLetterWordSet and not dictionary.check(currentGuess) or not currentGuess.isalpha()):
            print("Error: input word invalid.  It must be a real English word with exactly five letters.")
            currentGuess = input("Input 5-letter word guess: ").lower()
        currentGuess = currentGuess.upper()

        guessLayer = ''
        for letterIndex in range(len(currentGuess)):
            if currentGuess[letterIndex] == selectedWord[letterIndex]:
                guessLayer += bcolors.OKGREEN + '[' + currentGuess[letterIndex] + ']' + bcolors.ENDC + ' '
            elif currentGuess[letterIndex] in selectedWord:
                guessLayer += bcolors.OKBLUE + '[' + currentGuess[letterIndex] + ']' + bcolors.ENDC + ' '
            else:
                guessLayer += '[' + currentGuess[letterIndex] + ']' + ' '
        guessLayers[i] = guessLayer
        i += 1

    for guess in guessLayers:
        print(guess)

    if currentGuess == selectedWord:
        print(bcolors.BOLD + bcolors.OKGREEN + "You got it! Congratulations." + bcolors.ENDC)
    else:
        print("Aw, you ran out of guesses!")
    print("Selected word: ", selectedWord)
    print("Definition: ", definition)
    if len(examples) > 0:
        print("Usage examples: ")
        for ex in examples:
            print(ex)