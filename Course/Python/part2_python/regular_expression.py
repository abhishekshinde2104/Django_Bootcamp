"""
Regular Expression allow us to search for patterns in python strings

"""
import re

patterns = ['term1','term2']

text = 'This is a string with term1 and not the other'

#for pattern in patterns:
#    print("Im searching for : "+pattern)

#    if re.search(pattern,text):
#        print("Match")

#    else:
#        print("No Match")

match = re.search('term1',text)
print(type(match))
print(match)
print(match.start()) #tells u where the matching starts

split_term = '@'
email = 'user@gmail.com'

split = re.split(split_term,email)
print(split)

#re.findall() --> gives u all instances of the pattern

f=re.findall('match','Test phrase match in match middle')
print(f)

#Meta character syntax

def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searching for pattern {} ".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

#test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dsssssssss...sddddd'
#test_patterns=['sd*']#this means i want to find s followed by 0 or more d`s
#test_patterns=['sd+']#this means i want to find s followed by 1 or more d
#test_patterns=['sd?']#this means find s followed by d 0 or 1 times
#test_patterns=['sd{3}']#this specfies the that there should be 3 d`s after s
#test_patterns=['sd{2,3}']#this checks for all s followed by 2 or 3 d`s
#test_patterns=['s[sd]+'] #this checks for all s followed by either 1 or more s or d

#test_phrase = 'This is a string ! But it has a punctuation . How can we remove it?'
#test_patterns =['[^!.?]+']#this removes ! . ?  from the phrase
#test_patterns=['[a-z]+']#checks for sequences of lower case character
#test_patterns=['[A-Z]+']

#test_phrase='This is a string with numbers 325452 , 76554 and a symbol #hashtag'
#test_patterns=[r'\d+']#checks for all numbers in python
#o/p:==>['325452', '76554']
#test_patterns=[r'\D'+]#checks for all non-diigts
#test_patterns=[r'\s'+]#white spacess
#test_patterns=[r'\S'+]#non - white spacess
#test_patterns = [r'\w+']#alpha-numeric characters
#test_patterns=[r'\W+']#Non-Alpha-Numeric characters
multi_re_find(test_patterns,test_phrase)
