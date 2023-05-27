def pig_latin(text):
    #print(text)
    say = list()
    words = text.split()
    for word in words:
        if str(word[0]) in "aeiou":
            say.append( word + "ay" )
        else:
            say.append( word[1:] + word[0] + "ay"  )

    # Turn the list back into a phrase
    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"