import random
with open('data.txt', 'r') as file:
    data = file.read().rstrip()
    data_txt = str(data)
    data_list = data_txt.split()
i = random.randrange(3, 35)
i = i - 4
word = data_list[i]
def split(word):
     return [char for char in word]
word = split(word)
user1 = input("Enter the first character of your idea: ")
user2 = input("Enter the second character of your idea: ")
user3 = input("Enter the third character of your idea: ")
user4 = input("Enter the forth character of your idea: ")
if user1 == word[0]:
    print("the firt character is in right place")
else:
    print("the first character is not right")
if user2 == word[1]:
    print("the second character is in right place")
else:
    print("the second character is not right")
if user3 == word[2]:
    print("the third character is in right place")
else:
    print("the third character is not right")
if user4 == word[3]:
    print("the forth character is in right place")
else:
    print("the forth character is not right")
