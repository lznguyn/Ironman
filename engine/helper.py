import re

def extract_search_term(command):

    # Extract the search term from the query
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None   

def remove_words(input_string, words_to_move):
    words = input_string.split()

    filltered_words = [word for word in words if word.lower() not in words_to_move]
    result_string = ' '.join(filltered_words)
    return result_string

input_string = "make a phone call to lâm"
words_to_remove = ["make", "a", "to", "phone", "call", "send", "message", "whatsapp", ""]
result = remove_words(input_string, words_to_remove)
print(result)  # Output: "lâm"
