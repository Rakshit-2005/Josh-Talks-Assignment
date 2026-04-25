import re

hindi_numbers = {
    'शून्य': 0, 'जीरो': 0, 'एक': 1, 'दो': 2, 'तीन': 3, 'चार': 4, 'पांच': 5, 'पाँच': 5,
    'पच्चीस': 25
}

hindi_multipliers = {
    'सौ': 100,
    'हज़ार': 1000
}

text = "यह पच्चीस और एक हज़ार है"
words = text.split()
output = []
current_number_block = []

def process_number_block(block):
    if not block: return ""
    total = 0
    temp = 0
    for w in block:
        if w in hindi_numbers:
            temp += hindi_numbers[w]
        elif w in hindi_multipliers:
            if temp == 0: temp = 1 
            total += temp * hindi_multipliers[w]
            temp = 0
    total += temp
    return str(total)

for word in words:
    clean_word = re.sub(r'[^\w\s]', '', word)
    print(f"Checking word: '{word}' -> clean: '{clean_word}'")
    if clean_word in hindi_numbers or clean_word in hindi_multipliers:
        current_number_block.append(clean_word)
        print("  -> ADDED TO BLOCK:", current_number_block)
    else:
        if current_number_block:
            final_digit = process_number_block(current_number_block)
            output.append(final_digit)
            print("  -> FLUSH BLOCK:", final_digit)
            current_number_block = []
        output.append(word)
