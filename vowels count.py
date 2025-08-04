def vowels_count(string):
    vowels_list = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in string.lower():
        if char in vowels_list:
            count += 1
    return count
    
message = input('Type a word that includes vowels: ')

result = vowels_count(message)
print(f'This word has {result} vowels')



