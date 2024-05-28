#!/usr/bin/env python
# coding: utf-8

# # String Based Assignment Problem

# In[214]:


# 1.reverse a string
s = "Hello, world! This is a sample string. String sample."
reversed_string = s[::-1]
print("Reversed string:", reversed_string)


# In[2]:


#2.Check if a string is a palindrome
s = "racecar"
is_palindrome = s == s[::-1]
print("Is palindrome:", is_palindrome)


# In[3]:


#3.Convert a string to uppercase
s = "Hello, world!"
uppercase_string = s.upper()
print("Uppercase:", uppercase_string)


# In[4]:


#4.Convert a string to lowercase
s = "Hello, world!"
lowercase_string = s.lower()
print("Lowercase:", lowercase_string)


# In[5]:


#5.Count the number of vowels in a string
s = "Hello, world!"
vowels = 'aeiouAEIOU'
vowel_count = sum(1 for char in s if char in vowels)
print("Vowel count:", vowel_count)


# In[7]:


#6.Count the number of consonants in a string
s = "Hello, world!"
vowels = 'aeiouAEIOU'
consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
print("Consonant count:", consonant_count)


# In[8]:


#7.Remove all whitespaces from a string
s = "Hello, world!"
no_whitespaces = s.replace(" ", "")
print("Without whitespaces:", no_whitespaces)


# In[9]:


#8.Find the length of a string without using the len
s = "Hello, world!"
length = 0
for char in s:
    length += 1
print("Length:", length)


# In[10]:


#9.Check if a string contains a specific word
s = "Hello, world! This is a sample string."
word_to_find = 'sample'
contains_word = word_to_find in s
print("Contains 'sample':", contains_word)


# In[11]:


#10.Replace a word in a string with another word
s = "This is a sample string."
old_word = 'sample'
new_word = 'example'
replaced_string = s.replace(old_word, new_word)
print("Replace 'sample' with 'example':", replaced_string)


# In[12]:


#11.Count the occurrences of a word in a string
s = "This is a sample string. Sample string."
word_to_find = 'sample'
word_occurrences = s.lower().split().count(word_to_find.lower())
print("Count 'sample':", word_occurrences)


# In[13]:


#12.Find the first occurrence of a word in a string
s = "This is a sample string. Sample string."
word_to_find = 'sample'
first_occurrence = s.lower().find(word_to_find.lower())
print("First occurrence of 'sample':", first_occurrence)


# In[14]:


#13.Find the last occurrence of a word in a string
s = "This is a sample string. Sample string."
word_to_find = 'sample'
last_occurrence = s.lower().rfind(word_to_find.lower())
print("Last occurrence of 'sample':", last_occurrence)


# In[15]:


#14.Split a string into a list of words
s = "This is a sample string."
words_list = s.split()
print("Split into words:", words_list)


# In[16]:


#15.Join a list of words into a string
words_list = ["This", "is", "a", "sample", "string."]
joined_string = " ".join(words_list)
print("Join words:", joined_string)


# In[17]:


#16.Convert a string where words are separated by spaces to one where words are separated by underscores
s = "This is a sample string."
underscored_string = s.replace(" ", "_")
print("Underscored string:", underscored_string)


# In[18]:


#17.Check if a string starts with a specific word or phrase
s = "Hello, world!"
start_word = "Hello"
starts_with = s.startswith(start_word)
print(f"Starts with '{start_word}':", starts_with)


# In[19]:


# 18. Check if a string ends with a specific word or phrase.
string = "hello world"
phrase = "world"
ends_with_phrase = string.endswith(phrase)
print(ends_with_phrase)


# In[20]:


# 19. Convert a string to title case (e.g., "hello world" to "Hello World").
string = "hello world"
title_case_string = string.title()
print(title_case_string)


# In[21]:


# 20. Find the longest word in a string.
string = "hello world and universe"
longest_word = max(string.split(), key=len)
print(longest_word)


# In[22]:


# 21. Find the shortest word in a string.
string = "hello world and universe"
shortest_word = min(string.split(), key=len)
print(shortest_word)


# In[23]:


# 22. Reverse the order of words in a string.
string = "hello world and universe"
reversed_string = ' '.join(reversed(string.split()))
print(reversed_string)


# In[24]:


# 23. Check if a string is alphanumeric.
string = "hello123"
is_alphanumeric = string.isalnum()
print(is_alphanumeric)


# In[25]:


# 24. Extract all digits from a string.
string = "hello123world456"
digits = ''.join(filter(str.isdigit, string))
print(digits)


# In[26]:


# 25. Extract all alphabets from a string.
string = "hello123world456"
alphabets = ''.join(filter(str.isalpha, string))
print(alphabets)


# In[27]:


# 26. Count the number of uppercase letters in a string.
string = "Hello World"
uppercase_count = sum(1 for c in string if c.isupper())
print(uppercase_count)


# In[28]:


# 27. Count the number of lowercase letters in a string.
string = "Hello World"
lowercase_count = sum(1 for c in string if c.islower())
print(lowercase_count)


# In[29]:


# 28. Swap the case of each character in a string.
string = "Hello World"
swapped_string = string.swapcase()
print(swapped_string)


# In[30]:


# 29. Remove a specific word from a string.
string = "hello world and universe"
word_to_remove = "world"
string_without_word = ' '.join(w for w in string.split() if w != word_to_remove)
print(string_without_word)


# In[31]:


# 30. Check if a string is a valid email address.
import re

email = "example@example.com"
regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
is_valid_email = re.match(regex, email) is not None
print(is_valid_email)


# In[32]:


#31.Extract the username from an email address string.
email = "user@example.com"
username = email.split('@')[0]
print(username)  


# In[33]:


#32.Extract the domain name from an email address string.
email = "user@example.com"
domain = email.split('@')[1]
print(domain)  


# In[34]:


#33. Replace multiple spaces in a string with a single space.
text = "This  is   an example    string."
cleaned_text = ' '.join(text.split())
print(cleaned_text)  


# In[35]:


#34. Check if a string is a valid URL.
import re

url = "https://www.example.com"
regex = re.compile(
    r'^(?:http|https)://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
is_url_valid = re.match(regex, url) is not None
print(is_url_valid)  


# In[36]:


#35. Extract the protocol (http or https) from a URL string.
url = "https://www.example.com"
protocol = url.split('://')[0]
print(protocol)  


# In[37]:


#36. Find the frequency of each character in a string.
from collections import Counter

string = "example"
frequency = dict(Counter(string))
print(frequency) 


# In[38]:


#37. Remove all punctuation from a string.
import string

text = "Hello, world! This is an example string."
cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
print(cleaned_text)  


# In[39]:


#38. Check if a string contains only digits.
text = "123456"
is_only_digits = text.isdigit()
print(is_only_digits)  


# In[40]:


#39. Check if a string contains only alphabets.
text = "example"
is_only_alphabets = text.isalpha()
print(is_only_alphabets) 


# In[41]:


#40. Convert a string to a list of characters
text = "example"
char_list = list(text)
print(char_list)  


# In[42]:


#41. Check if two strings are anagrams.
from collections import Counter

str1 = "listen"
str2 = "silent"
are_anagrams = Counter(str1) == Counter(str2)
print(are_anagrams)  


# In[43]:


#42. Encode a string using a Caesar cipher.
text = "example"
shift = 3
encoded_text = ''.join(chr((ord(char) - 97 + shift) % 26 + 97) for char in text)
print(encoded_text)  


# In[44]:


#43. Decode a Caesar cipher encoded string.
encoded_text = "hadpsoh"
shift = 3
decoded_text = ''.join(chr((ord(char) - 97 - shift) % 26 + 97) for char in encoded_text)
print(decoded_text)  


# In[45]:


#44. Find the most frequent word in a string.
from collections import Counter
import re

text = "This is a test. This test is only a test."
words = re.findall(r'\w+', text.lower())
most_common_word = Counter(words).most_common(1)[0]
print(most_common_word)  


# In[46]:


#45. Find all unique words in a string.
import re

text = "This is a test. This test is only a test."
words = re.findall(r'\w+', text.lower())
unique_words = set(words)
print(unique_words) 


# In[47]:


#46. Count the number of syllables in a string.
import re

text = "This is a simple example."

def count_syllables(word):
    word = word.lower()
    vowels = "aeiou"
    syllables = 0
    if word[0] in vowels:
        syllables += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            syllables += 1
    if word.endswith("e"):
        syllables -= 1
    if word.endswith("le") and len(word) > 2 and word[-3] not in vowels:
        syllables += 1
    if syllables == 0:
        syllables += 1
    return syllables

words = re.findall(r'\w+', text)
total_syllables = sum(count_syllables(word) for word in words)
print(total_syllables)  


# In[48]:


#47. Check if a string contains any special characters.
import re

text = "Hello, world!"
contains_special_characters = bool(re.search(r'[^a-zA-Z0-9\s]', text))
print(contains_special_characters)  


# In[49]:


#48. Remove the nth word from a string.
text = "This is an example string."
n = 2
words = text.split()
if 0 <= n < len(words):
    del words[n]
result = ' '.join(words)
print(result)


# In[50]:


#49. Insert a word at the nth position in a string.
text = "This is an example string."
word_to_insert = "new"
n = 2
words = text.split()
if 0 <= n <= len(words):
    words.insert(n, word_to_insert)
result = ' '.join(words)
print(result) 


# In[51]:


#50. Convert a CSV string to a list of lists.
import csv
import io

csv_string = "name,age,city\nAlice,30,New York\nBob,25,Los Angeles"
f = io.StringIO(csv_string)
reader = csv.reader(f)
csv_list = list(reader)
print(csv_list)  


# # List Based Practice Problem :

# In[52]:


# 1. Create a list with integers from 1 to 10
my_list = list(range(1, 11))
print(my_list)


# In[53]:


# 2. Find the length of a list without using the len() function
my_list = list(range(1, 11))
length = 0
for _ in my_list:
    length += 1
print(length)


# In[54]:


# 3. Append an element to the end of a list
my_list = list(range(1, 11))
my_list.append(11)
print(my_list)


# In[55]:


# 4. Insert an element at a specific index in a list
my_list = list(range(1, 11))
my_list.insert(5, 15)  # Insert 15 at index 5
print(my_list)


# In[56]:


# 5. Remove an element from a list by its value
my_list = list(range(1, 11))
my_list.append(15)
print("Before removing:", my_list)
my_list.remove(15)
print("After removing:", my_list)


# In[59]:


# 6. Remove an element from a list by its index
my_list = list(range(1, 11))
del my_list[9]  # Remove element at index 10
print(my_list)


# In[60]:


# 7. Check if an element exists in a list
my_list = list(range(1, 11))
exists = 5 in my_list
print(exists)


# In[61]:


# 8. Find the index of the first occurrence of an element in a list
my_list = list(range(1, 11))
index = my_list.index(5)
print(index)


# In[62]:


# 9. Count the occurrences of an element in a list
my_list = list(range(1, 11))
count = my_list.count(5)
print(count)


# In[63]:


# 10. Reverse the order of elements in a list
my_list = list(range(1, 11))
my_list.reverse()
print(my_list)


# In[64]:


# 11. Sort a list in ascending order
my_list = [5, 3, 8, 1, 9, 2, 6, 7, 4, 10]
my_list.sort()
print(my_list)


# In[65]:


# 12. Sort a list in descending order
my_list = [5, 3, 8, 1, 9, 2, 6, 7, 4, 10]
my_list.sort(reverse=True)
print(my_list)


# In[66]:


# 13. Create a list of even numbers from 1 to 20
even_list = [x for x in range(1, 21) if x % 2 == 0]
print(even_list)


# In[67]:


# 14. Create a list of odd numbers from 1 to 20
odd_list = [x for x in range(1, 21) if x % 2 != 0]
print(odd_list)


# In[68]:


# 15. Find the sum of all elements in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum = sum(my_list)
print(total_sum)


# In[69]:


# 16. Find the maximum value in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_value = max(my_list)
print(max_value)


# In[70]:


# 17. Find the minimum value in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_value = min(my_list)
print(min_value)


# In[71]:


# 18. Create a list of squares of numbers from 1 to 10
squares_list = [x**2 for x in range(1, 11)]
print(squares_list)


# In[72]:


# 19. Create a list of random numbers
import random
random_list = [random.randint(1, 100) for _ in range(10)]
print(random_list)


# In[73]:


# 20. Remove duplicates from a list
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)


# In[74]:


# 21. Find the common elements between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = list(set(list1) & set(list2))
print(common_elements)


# In[75]:


# 22. Find the difference between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
difference = list(set(list1) - set(list2))
print(difference)


# In[76]:


# 23. Merge two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)


# In[77]:


# 24. Multiply all elements in a list by 2
my_list = [1, 2, 3, 4, 5]
multiplied_list = [x * 2 for x in my_list]
print(multiplied_list)


# In[78]:


# 25. Filter out all even numbers from a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = [x for x in my_list if x % 2 != 0]
print(filtered_list)


# In[79]:


# 26. Convert a list of strings to a list of integers
str_list = ["1", "2", "3", "4", "5"]
int_list = [int(x) for x in str_list]
print(int_list)


# In[80]:


# 27. Convert a list of integers to a list of strings
int_list = [1, 2, 3, 4, 5]
str_list = [str(x) for x in int_list]
print(str_list)


# In[81]:


# 28. Flatten a nested list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)


# In[83]:


# 29. Create a list of the first 10 Fibonacci numbers
fib_list = [0, 1]
for _ in range(8):
    fib_list.append(fib_list[-1] + fib_list[-2])
print(fib_list)


# In[84]:


# 30. Check if a list is sorted
my_list = [1, 2, 3, 4, 5]
is_sorted = my_list == sorted(my_list)
print(is_sorted)


# In[85]:


# 31. Rotate a list to the left by n positions
my_list = [1, 2, 3, 4, 5]
n = 2
rotated_list = my_list[n:] + my_list[:n]
print(rotated_list)


# In[86]:


# 32. Rotate a list to the right by n positions
my_list = [1, 2, 3, 4, 5]
n = 2
rotated_list = my_list[-n:] + my_list[:-n]
print(rotated_list)


# In[87]:


# 33. Create a list of prime numbers up to 50
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_list = [x for x in range(2, 51) if is_prime(x)]
print(prime_list)


# In[88]:


# 34. Split a list into chunks of size n
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
chunks = [my_list[i:i + n] for i in range(0, len(my_list), n)]
print(chunks)


# In[89]:


# 35. Find the second largest number in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
unique_list = list(set(my_list))
unique_list.sort()
second_largest = unique_list[-2]
print(second_largest)


# In[90]:


# 36. Replace every element in a list with its square
my_list = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in my_list]
print(squared_list)


# In[91]:


# 37. Convert a list to a dictionary where list elements become keys and their indices become values
my_list = ['a', 'b', 'c', 'd']
dict_from_list = {my_list[i]: i for i in range(len(my_list))}
print(dict_from_list)


# In[92]:


# 38. Shuffle the elements of a list randomly
import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)


# In[93]:


# 39. Create a list of the first 10 factorial numbers
import math
factorial_list = [math.factorial(x) for x in range(1, 11)]
print(factorial_list)


# In[94]:


# 40. Check if two lists have at least one element in common
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
common_element = any(elem in list1 for elem in list2)
print(common_element)


# In[95]:


# 41. Remove all elements from a list
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)


# In[96]:


# 42. Replace negative numbers in a list with 0
my_list = [1, -2, 3, -4, 5]
replaced_list = [x if x >= 0 else 0 for x in my_list]
print(replaced_list)


# In[97]:


# 43. Convert a string into a list of words
my_string = "Convert this string into a list of words"
word_list = my_string.split()
print(word_list)


# In[98]:


# 44. Convert a list of words into a string
word_list = ["Convert", "this", "list", "into", "a", "string"]
my_string = " ".join(word_list)
print(my_string)


# In[99]:


# 45. Create a list of the first n powers of 2
n = 10
powers_of_2 = [2**x for x in range(n)]
print(powers_of_2)


# In[100]:


# 46. Find the longest string in a list of strings
str_list = ["apple", "banana", "cherry", "date"]
longest_string = max(str_list, key=len)
print(longest_string)


# In[101]:


# 47. Find the shortest string in a list of strings
str_list = ["apple", "banana", "cherry", "date"]
shortest_string = min(str_list, key=len)
print(shortest_string)


# In[102]:


# 48. Create a list of the first n triangular numbers
n = 10
triangular_numbers = [(x * (x + 1)) // 2 for x in range(1, n + 1)]
print(triangular_numbers)


# In[103]:


# 49. Check if a list contains another list as a subsequence
def is_subsequence(main_list, sub_list):
    it = iter(main_list)
    return all(elem in it for elem in sub_list)

main_list = [1, 2, 3, 4, 5]
sub_list = [2, 4]
result = is_subsequence(main_list, sub_list)
print(result)


# In[104]:


# 50. Swap two elements in a list by their indices
my_list = [1, 2, 3, 4, 5]
i, j = 1, 3  
my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)


# # Tuple Based Practice Problem :

# In[105]:


# 1. Create a tuple with integers from 1 to 5
my_tuple = tuple(range(1, 6))
print(my_tuple)


# In[106]:


# 2. Access the third element of a tuple
my_tuple = (1, 2, 3, 4, 5)
third_element = my_tuple[2]  # Indexing starts from 0
print(third_element)


# In[107]:


# 3. Find the length of a tuple without using the len() function
my_tuple = (1, 2, 3, 4, 5)
length = 0
for _ in my_tuple:
    length += 1
print(length)


# In[108]:


# 4. Count the occurrences of an element in a tuple
my_tuple = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5)
element_count = my_tuple.count(3)
print(element_count)


# In[109]:


# 5. Find the index of the first occurrence of an element in a tuple
my_tuple = (1, 2, 3, 4, 3, 5)
index = my_tuple.index(3)
print(index)


# In[110]:


# 6. Check if an element exists in a tuple
my_tuple = (1, 2, 3, 4, 5)
exists = 5 in my_tuple
print(exists)


# In[111]:


# 7. Convert a tuple to a list
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)


# In[112]:


# 8. Convert a list to a tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)


# In[113]:


# 9. Unpack the elements of a tuple into variables
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c)


# In[114]:


# 10. Create a tuple of even numbers from 1 to 10
even_tuple = tuple(range(2, 11, 2))
print(even_tuple)


# In[115]:


# 11. Create a tuple of odd numbers from 1 to 10
odd_tuple = tuple(range(1, 11, 2))
print(odd_tuple)


# In[116]:


# 12. Concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)


# In[117]:


# 13. Repeat a tuple three times
my_tuple = (1, 2, 3)
repeated_tuple = my_tuple * 3
print(repeated_tuple)


# In[118]:


# 14. Check if a tuple is empty
empty_tuple = ()
is_empty = not empty_tuple
print(is_empty)


# In[119]:


# 15. Create a nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)


# In[120]:


# 16. Access the first element of a nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
first_element = nested_tuple[0]
print(first_element)


# In[121]:


# 17. Create a tuple with a single element
single_element_tuple = (5,)
print(single_element_tuple)


# In[122]:


# 18. Compare two tuples
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
are_equal = tuple1 == tuple2
print(are_equal)


# In[182]:


# 19. Delete a tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)


# In[127]:


# 20. Slice a tuple
my_tuple = (1, 2, 3, 4, 5)
sliced_tuple = my_tuple[1:4]  # Elements from index 1 to 3
print(sliced_tuple)


# In[183]:


# 21. Find the maximum value in a tuple
my_tuple = (3, 7, 2, 9, 5)
max_value = max(my_tuple)
print(max_value)


# In[184]:


# 22. Find the minimum value in a tuple
my_tuple = (3, 7, 2, 9, 5)
min_value = min(my_tuple)
print(min_value)


# In[185]:


# 23. Convert a string to a tuple of characters
my_string = "hello"
char_tuple = tuple(my_string)
print(char_tuple)


# In[186]:


# 24. Convert a tuple of characters to a string
char_tuple = ('h', 'e', 'l', 'l', 'o')
my_string = ''.join(char_tuple)
print(my_string)


# In[187]:


# 25. Create a tuple from multiple data types
mixed_tuple = (1, 'hello', 3.14, True)
print(mixed_tuple)


# In[188]:


# 26. Check if two tuples are identical
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
are_identical = tuple1 == tuple2
print(are_identical)


# In[189]:


# 27. Sort the elements of a tuple
my_tuple = (3, 1, 4, 1, 5, 9, 2)
sorted_tuple = tuple(sorted(my_tuple))
print(sorted_tuple)


# In[190]:


# 28. Convert a tuple of integers to a tuple of strings
int_tuple = (1, 2, 3, 4, 5)
str_tuple = tuple(str(x) for x in int_tuple)
print(str_tuple)


# In[191]:


# 29. Convert a tuple of strings to a tuple of integers
str_tuple = ('1', '2', '3', '4', '5')
int_tuple = tuple(int(x) for x in str_tuple)
print(int_tuple)


# In[192]:


# 30. Merge two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)


# In[193]:


# 31. Flatten a nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
flattened_tuple = tuple(item for sublist in nested_tuple for item in sublist)
print(flattened_tuple)


# In[194]:


# 32. Create a tuple of the first 5 prime numbers
prime_tuple = (2, 3, 5, 7, 11)
print(prime_tuple)


# In[195]:


# 33. Check if a tuple is a palindrome
my_tuple = (1, 2, 3, 2, 1)
is_palindrome = my_tuple == my_tuple[::-1]
print(is_palindrome)


# In[196]:


# 34. Create a tuple of squares of numbers from 1 to 5
squares_tuple = tuple(x ** 2 for x in range(1, 6))
print(squares_tuple)


# In[197]:


# 35. Filter out all even numbers from a tuple
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
filtered_tuple = tuple(x for x in my_tuple if x % 2 != 0)
print(filtered_tuple)


# In[198]:


# 36. Multiply all elements in a tuple by 2
my_tuple = (1, 2, 3, 4, 5)
multiplied_tuple = tuple(x * 2 for x in my_tuple)
print(multiplied_tuple)


# In[199]:


# 37. Create a tuple of random numbers
import random
random_tuple = tuple(random.randint(1, 100) for _ in range(5))
print(random_tuple)


# In[200]:


# 38. Check if a tuple is sorted
my_tuple = (1, 2, 3, 4, 5)
is_sorted = my_tuple == tuple(sorted(my_tuple))
print(is_sorted)


# In[201]:


# 39. Rotate a tuple to the left by n positions
def rotate_left_tuple(tuple, n):
    return tuple[n % len(tuple):] + tuple[:n % len(tuple)]

my_tuple = (1, 2, 3, 4, 5)
rotated_tuple = rotate_left_tuple(my_tuple, 2)
print(rotated_tuple)


# In[202]:


# 40. Rotate a tuple to the right by n positions
def rotate_right_tuple(tuple, n):
    return tuple[-n % len(tuple):] + tuple[:-n % len(tuple)]

my_tuple = (1, 2, 3, 4, 5)
rotated_tuple = rotate_right_tuple(my_tuple, 2)
print(rotated_tuple)


# In[203]:


# 41. Create a tuple of the first 5 Fibonacci numbers
def fibonacci(n):
    a, b = 0, 1
    fib = []
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return tuple(fib)

fibonacci_tuple = fibonacci(5)
print(fibonacci_tuple)


# In[204]:


# 42. Create a tuple from user input
user_input = input("Enter elements separated by space: ")
user_tuple = tuple(user_input.split())
print(user_tuple)


# In[213]:


# 43. Swap two elements in a tuple
test_list = [(3, 4), (6, 5), (7, 8)]
print("The original list is : " + str(test_list))
res = [(sub[1], sub[0]) for sub in test_list]
print("The swapped tuple list is : " + str(res))


# In[206]:


# 44. Reverse the elements of a tuple
my_tuple = (1, 2, 3, 4, 5)
reversed_tuple = my_tuple[::-1]
print(reversed_tuple)


# In[207]:


# 45. Create a tuple of the first n powers of 2
n = 5
powers_of_2_tuple = tuple(2 ** i for i in range(1, n + 1))
print(powers_of_2_tuple)


# In[208]:


# 46. Find the longest string in a tuple of strings
my_tuple = ("apple", "banana", "orange", "kiwi")
longest_string = max(my_tuple, key=len)
print(longest_string)


# In[209]:


# 47. Find the shortest string in a tuple of strings
my_tuple = ("apple", "banana", "orange", "kiwi")
shortest_string = min(my_tuple, key=len)
print(shortest_string)


# In[210]:


# 48. Create a tuple of the first n triangular numbers
def triangular_number(n):
    return n * (n + 1) // 2

n = 5
triangular_numbers_tuple = tuple(triangular_number(i) for i in range(1, n + 1))
print(triangular_numbers_tuple)


# In[211]:


# 49. Check if a tuple contains another tuple as a subsequence
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (2, 3)
is_subsequence = any(tuple2 == tuple1[i:i + len(tuple2)] for i in range(len(tuple1) - len(tuple2) + 1))
print(is_subsequence)


# In[212]:


# 50. Create a tuple of alternating 1s and 0s of length n
n = 10
alternating_tuple = tuple(1 if i % 2 == 0 else 0 for i in range(n))
print(alternating_tuple)


# # Set Based Practice Problem :

# In[166]:


# 1. Create a set with integers from 1 to 5
my_set = {1, 2, 3, 4, 5}
print(my_set)


# In[167]:


# 2. Add an element to a set
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)


# In[168]:


# 3. Remove an element from a set
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)


# In[169]:


# 4. Check if an element exists in a set
my_set = {1, 2, 3, 4, 5}
exists = 5 in my_set
print(exists)


# In[170]:


# 5. Find the length of a set without using the len() function
my_set = {1, 2, 3, 4, 5}
length = sum(1 for _ in my_set)
print(length)


# In[171]:


# 6. Clear all elements from a set
my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set)


# In[172]:


# 7. Create a set of even numbers from 1 to 10
even_set = {x for x in range(1, 11) if x % 2 == 0}
print(even_set)


# In[173]:


# 8. Create a set of odd numbers from 1 to 10
odd_set = {x for x in range(1, 11) if x % 2 != 0}
print(odd_set)


# In[174]:


# 9. Find the union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)


# In[175]:


# 10. Find the intersection of two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection_set = set1.intersection(set2)
print(intersection_set)


# In[176]:


# 11. Find the difference between two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference_set = set1.difference(set2)
print(difference_set)


# In[177]:


# 12. Check if a set is a subset of another set
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_subset = set1.issubset(set2)
print(is_subset)


# In[178]:


# 13. Check if a set is a superset of another set
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
is_superset = set1.issuperset(set2)
print(is_superset)


# In[179]:


# 14. Create a set from a list
my_list = [1, 2, 3, 4, 5]
set_from_list = set(my_list)
print(set_from_list)


# In[180]:


# 15. Convert a set to a list
my_set = {1, 2, 3, 4, 5}
list_from_set = list(my_set)
print(list_from_set)


# In[128]:


# 16. Remove a random element from a set
import random
my_set = {1, 2, 3, 4, 5}
random_element = random.choice(list(my_set))
my_set.remove(random_element)
print(my_set)


# In[129]:


# 17. Pop an element from a set
my_set = {1, 2, 3, 4, 5}
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("Updated set:", my_set)


# In[130]:


# 18. Check if two sets have no elements in common
set1 = {1, 2, 3}
set2 = {4, 5, 6}
no_common_elements = set1.isdisjoint(set2)
print(no_common_elements)


# In[131]:


# 19. Find the symmetric difference between two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)


# In[132]:


# 20. Update a set with elements from another set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)


# In[133]:


# 21. Create a set of the first 5 prime numbers
prime_set = {2, 3, 5, 7, 11}
print(prime_set)


# In[134]:


# 22. Check if two sets are identical
set1 = {1, 2, 3}
set2 = {3, 2, 1}
are_identical = set1 == set2
print(are_identical)


# In[135]:


# 23. Create a frozen set
my_frozen_set = frozenset({1, 2, 3, 4, 5})
print(my_frozen_set)


# In[136]:


# 24. Check if a set is disjoint with another set
set1 = {1, 2, 3}
set2 = {4, 5, 6}
is_disjoint = set1.isdisjoint(set2)
print(is_disjoint)


# In[137]:


# 25. Create a set of squares of numbers from 1 to 5
squares_set = {x**2 for x in range(1, 6)}
print(squares_set)


# In[138]:


# 26. Filter out all even numbers from a set
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
filtered_set = {x for x in my_set if x % 2 != 0}
print(filtered_set)


# In[139]:


# 27. Multiply all elements in a set by 2
my_set = {1, 2, 3, 4, 5}
multiplied_set = {x * 2 for x in my_set}
print(multiplied_set)


# In[140]:


# 28. Create a set of random numbers
import random
random_set = {random.randint(1, 100) for _ in range(10)}
print(random_set)


# In[141]:


# 29. Check if a set is empty
my_set = set()
is_empty = not my_set
print(is_empty)


# In[142]:


# 30. Create a nested set (hint: use frozenset)
nested_set = {frozenset({1, 2}), frozenset({3, 4})}
print(nested_set)


# In[143]:


# 31. Remove an element from a set using the discard method
my_set = {1, 2, 3, 4, 5}
my_set.discard(3)
print(my_set)


# In[144]:


# 32. Compare two sets
set1 = {1, 2, 3}
set2 = {3, 2, 1}
are_equal = set1 == set2
print(are_equal)


# In[145]:


# 33. Create a set from a string
my_string = "hello"
string_set = set(my_string)
print(string_set)


# In[146]:


# 34. Convert a set of strings to a set of integers
string_set = {"1", "2", "3", "4", "5"}
int_set = {int(x) for x in string_set}
print(int_set)


# In[147]:


# 35. Convert a set of integers to a set of strings
int_set = {1, 2, 3, 4, 5}
string_set = {str(x) for x in int_set}
print(string_set)


# In[148]:


# 36. Create a set from a tuple
my_tuple = (1, 2, 3, 4, 5)
tuple_set = set(my_tuple)
print(tuple_set)


# In[149]:


# 37. Convert a set to a tuple
my_set = {1, 2, 3, 4, 5}
tuple_from_set = tuple(my_set)
print(tuple_from_set)


# In[150]:


# 38. Find the maximum value in a set
my_set = {3, 7, 2, 9, 5}
max_value = max(my_set)
print(max_value)


# In[151]:


# 39. Find the minimum value in a set
my_set = {3, 7, 2, 9, 5}
min_value = min(my_set)
print(min_value)


# In[152]:


# 40. Create a set from user input
user_input = input("Enter elements separated by space: ")
user_set = set(user_input.split())
print(user_set)


# In[153]:


# 41. Check if the intersection of two sets is empty
set1 = {1, 2, 3}
set2 = {4, 5, 6}
is_empty_intersection = set1.isdisjoint(set2)
print(is_empty_intersection)


# In[154]:


# 42. Create a set of the first 5 Fibonacci numbers
fibonacci_set = {0, 1, 1, 2, 3}
print(fibonacci_set)


# In[155]:


# 43. Remove duplicates from a list using sets
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)


# In[156]:


# 44. Check if two sets have the same elements, regardless of their count
set1 = {1, 2, 3, 3}
set2 = {1, 1, 2, 3}
same_elements = set1 == set2
print(same_elements)


# In[157]:


# 45. Create a set of the first n powers of 2
n = 5
powers_of_2_set = {2 ** x for x in range(n)}
print(powers_of_2_set)


# In[158]:


# 46. Find the common elements between a set and a list
set1 = {1, 2, 3, 4, 5}
list1 = [4, 5, 6, 7, 8]
common_elements = set1.intersection(list1)
print(common_elements)


# In[162]:


# 47. Create a set of the first n triangular numbers
def triangular_series( n ):
    j = 1
    k = 1
    for i in range(1, n + 1):
        print(k, end = ' ')
        j = j + 1 
        k = k + j 
         
n = 5
triangular_series(n)


# In[163]:


# 48. Check if a set contains another set as a subset
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3}
is_subset = set2.issubset(set1)
print(is_subset)


# In[164]:


# 49. Create a set of alternating 1s and 0s of length n
n = 10
alternating_set = {1 if i % 2 == 0 else 0 for i in range(n)}
print(alternating_set)


# In[165]:


# 50. Merge multiple sets into one
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}
merged_set = set1.union(set2, set3)
print(merged_set)


# In[ ]:




