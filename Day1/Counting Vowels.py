word=str(input("Please enter a word: "))     #get input form user
l=word.lower()                               #convert input to lowecase

vc={}                                        #set up dictionary variable to hold vowle count

for vowel in "aeiou":                        # start for loop to compare each letter to vowels
    count=l.count(vowel)
                                            #count each vowel in the input
    vc[vowel] =count

counts=vc.values()                          #set up variable for adding up the number of variables

tv=sum(counts)                              #add up the number of vowles

print("the total number of vowels is: "+(str(tv)))     #print the number of vowels
