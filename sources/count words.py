with open('hey.txt') as infile:

    for line in infile:
        words = 0
        characters = 0
        wordslist = line.split()
        words += len(wordslist)
        characters += sum(len(word) for word in wordslist)
        print(line,words,characters)