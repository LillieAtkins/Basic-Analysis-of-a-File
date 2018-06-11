"""
CS101
HW9
Lillie Atkins
Lab X
November 27, 2017
"""

import string

def analyzeFile(filename):
    """
    Reads a file and returns statistics about the contents.
		 Input: filename - a string containing the name of the file to read
		 Output: a tuple containing the longest word, shortest word, most common word and least common word
    """     
    fileData = open(filename, encoding="utf-8") # open the file
    
    counts = {}

    for line in fileData:		          # iterates over every line of the file
        words = line.split()            # turns each line into a list
        for word in words:           #iterates over the words in each line list
            word = word.lower().strip(string.whitespace+string.punctuation)
            if len(word) > 0:       #make sure word is longer than 0 before adding it to the dictionary
                counts[word] = counts.get(word, 0) + 1 #look up if the dictionary has that word and if not then it'll add that word with the value 0 associated with it and then add one to that, if it has seen it it'll add 1 to the value stored in the counts dictionary
                                      #when it gets here for the first line it goes back up to the top and repeats for the 2nd line
        mostCommonWord = [word]
        leastCommonWord = [word]
        shortestWord = [word]
        longestWord = [word]
        
        for item in counts:
            if counts[mostCommonWord[0]] < counts[item]:
                mostCommonWord = [item]
            elif counts[mostCommonWord[0]] == counts[item]:
                mostCommonWord.append(item)
            if counts[leastCommonWord[0]] > counts[item]:
                leastCommonWord = [item]
            elif counts[leastCommonWord[0]] == counts[item]:
                leastCommonWord.append(item)
            if len(shortestWord[0]) > len(item):
                shortestWord = [item] 
            elif len((shortestWord[0])) == len(item):
                shortestWord.append(item)
            if len(longestWord[0]) < len(item):
                longestWord = [item]
            elif len(longestWord[0]) == len(item):
                longestWord.append(item)
        
    return (mostCommonWord, leastCommonWord, shortestWord, longestWord)
    

import urllib.request

def weather(zipcode):
    """
    This takes a string as an input parameter and treats it as a zip code,
    looks up the weather for that zipcode, and returns the current temperature at that zipcode in Fahrenheit.
    """
    
    URL = 'http://api.openweathermap.org/data/2.5/weather?zip=' + zipcode + ',us&appid=' + '7d7a3cf9902ef14f54f49f160fc8a550' + '&units=imperial'
    webpage = urllib.request.urlopen(URL)
    contents = webpage.read()
    contents = contents.decode('ascii')
    weather = eval(contents) #this line turns it from a string into dictionaries and lists
    temperature = weather['main']['temp']
    return temperature
    