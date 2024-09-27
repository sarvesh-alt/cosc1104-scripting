'''
Week 2 Exercises - Variables, Conditions, Loops
Author: Sarvesh More
Class: COSC1104
'''



#Exercise 1 - Vowel Counter
#Skills: Variables, String MAnipulation , Loops, Conditions

#Takes User input for String
user_string  = input('Enter A random String : ').lower()

#list of vowels
vowels = ['a','e','i','o','u']

#Count the vowels
vowel_counter = [0,0,0,0,0]

#Iterate through each character in the vowel
for each_char in user_string:
    if each_char in vowels:
        #Find the index of the vowel list
        index = vowels.index(each_char)
        #Increment the counter located
        vowel_counter[index] += 1
        
#Display the counter for each vowel
for i in range(len(vowels)):
    print(f'{vowels[i]} - {vowel_counter[i]}')



#Exercise 2 - Sum of Digits
#Skills: Variables, Type Casting, Loops, Conditions