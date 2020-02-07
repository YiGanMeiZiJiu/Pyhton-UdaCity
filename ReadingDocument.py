def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    with open(filename) as document:
        for line in document:
            cast_list.append(line.split(',',1)[0])

    return cast_list

# Use an import statement at the top 

import random
import math
#随机密码生成器
word_file = "words.txt"
word_list = []
#fill up the word_list
# with open(word_file,'r') as words:
# 	for line in words:
# 		# remove white space and make everything lowercase
# 		word = line.strip().lower()
# 		# don't include words that are too long or too short
# 		if 3 < len(word) < 8:
# 			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    password = ''
    for _ in range(3):
        password += random.choice(word_list)
    return password

# test your function
# print(generate_password())
