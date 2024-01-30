def alphabet_occurrence(input_string):
    char_count = {}
    for char in input_string:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    maximum_character = max(char_count, key=char_count.get)
    maximum_occurrence = char_count[maximum_character]
 
    return maximum_character, maximum_occurrence
 
input_string = "hippopotamus"
result_character, result_occurrence = alphabet_occurrence(input_string)
print(f"The highest occurring character is '{result_character}' with occurrence count {result_occurrence}.")
