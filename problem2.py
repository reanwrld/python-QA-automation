"""
Title: Text Stats & ASCII Report
Author: Reyan Heyar
Date: 02-18-2026
Purpose: Analyzes user provided text for ASCII values.
Analysis: Processes multi-line text input to generate character-level and word-level statistics.
Design: Uses a dictionary for frequency tracking and string methods for character classification.
Algorithm: Collect lines -> Parse characters for ASCII/Type -> Split/Clean words -> Sort and Display.
"""
print("Enter your text (type a single '.' on a new line to finish): ")
lines = []

# Checks lines until "." entered 
while True:
    userInput = input()
    if userInput == ".":
        break
    lines.append(userInput)

# Initializes counters and data structures 
seenChars = []
wordCount = {}
letterCount = 0
digitCount = 0
totalChars = 0
totalWords = 0
longestLine = 0

print("\n------- ASCII TABLE (first 25 unique chars) -------")
print("-" *50)
print("%-20s %-20s" % ("CHARACTER", "ASCII"))
print("-" *30)
for text in lines:

    # Tracks the length of the longest line
    if len(text) > longestLine:
        longestLine = len(text)
    words = text.split()
    for w in words:
        totalWords +=1
        cleanW = w.lower().strip(".,!?:;")

        # Dictionary frequencey counter for words 
        if cleanW in wordCount:
            wordCount[cleanW] += 1
        else:
            wordCount[cleanW] = 1

    for char in text:
        totalChars +=1

        # Catagorizes characters using string methods
        if char.isdigit():
            digitCount +=1

        if char.isalpha():
            letterCount +=1

        # Tracks unique characters for ASCII report   
        if char not in seenChars and len(seenChars) < 25:
            seenChars.append(char)
            ascii = ord(char)
            print("%-20s %-20d" % (char, ascii))

letterFreq = letterCount / totalChars * 100
wordList = list(wordCount.items())
wordList.sort(key=lambda x: (-x[1], x[0]))

print("\n------- TOP 10 WORDS -------")
print("%-20s %-20s" % ("WORD", "FREQUENCY"))
print("-" *30)

# Displays the top 10 most frequent words
for word, count in wordList[:10]:
    print("%-20s %-20d" % (word, count))

print("")
print("-"*10, "SUMMARY", "-"*10) 
print("%-20s %6d" % ("Total Characters:", totalChars))
print("%-20s %6d" % ("Total Words:", totalWords))
print("%-20s %6d" % ("Total Lines:", len(lines)))
print("%-20s %6d" % ("Longest Line Length:", longestLine))
print("%-20s %6.2f%%" % ("Letter Frequency:", letterFreq))
print("%-20s %6d" % ("Digits in text:", digitCount))





