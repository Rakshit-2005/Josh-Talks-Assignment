import re

hindi_numbers = {
    'शून्य': 0, 'जीरो': 0, 'एक': 1, 'दो': 2, 'तीन': 3, 'चार': 4, 'पांच': 5, 'पाँच': 5,
    'छह': 6, 'सात': 7, 'आठ': 8, 'नौ': 9, 'दस': 10, 'ग्यारह': 11, 'बारह': 12, 'तेरह': 13,
    'चौदह': 14, 'पंद्रह': 15, 'सोलह': 16, 'सत्रह': 17, 'अठारह': 18, 'उन्नाइस': 19, 'उन्नीस': 19,
    'बीस': 20, 'इक्कीस': 21, 'बाईस': 22, 'तेईस': 23, 'चौबीस': 24, 'पच्चीस': 25, 'छब्बीस': 26,
    'सत्ताइस': 27, 'अट्ठाइस': 28, 'उनतीस': 29, 'तीस': 30, 'इकतीस': 31, 'बत्तीस': 32, 'तैंतीस': 33,
    'चौंतीस': 34, 'पैंतीस': 35, 'छत्तीस': 36, 'सैंतीस': 37, 'अड़तीस': 38, 'उनतालीस': 39, 'चालीस': 40,
    'इकतालीस': 41, 'बयालीस': 42, 'तैंतालीस': 43, 'चवालीस': 44, 'पैंतालीस': 45, 'छियालीस': 46,
    'सैंतालीस': 47, 'अड़तालीस': 48, 'उनचास': 49, 'पचास': 50, 'इक्यावन': 51, 'बावन': 52, 'तिरेपन': 53,
    'चौवन': 54, 'पचपन': 55, 'छप्पन': 56, 'सत्तावन': 57, 'अट्ठावन': 58, 'उनसठ': 59, 'साठ': 60,
    'इक्सठ': 61, 'बासठ': 62, 'तिरेसठ': 63, 'चौंसठ': 64, 'पैंसठ': 65, 'छियासठ': 66, 'सड़सठ': 67,
    'अड़सठ': 68, 'उनहत्तर': 69, 'सत्तर': 70, 'इकहत्तर': 71, 'बहत्तर': 72, 'तिहत्तर': 73, 'चौहत्तर': 74,
    'पचहत्तर': 75, 'छिहत्तर': 76, 'सतहत्तर': 77, 'अठहत्तर': 78, 'उनासी': 79, 'अस्सी': 80, 'इक्यासी': 81,
    'बयासी': 82, 'तिरासी': 83, 'चौरासी': 84, 'पचासी': 85, 'छियासी': 86, 'सत्तासी': 87, 'अट्ठासी': 88,
    'नवासी': 89, 'नब्बे': 90, 'इक्यानवे': 91, 'बानवे': 92, 'तिरानवे': 93, 'चौरानवे': 94, 'पचानवे': 95,
    'छियानवे': 96, 'सत्तानवे': 97, 'अट्ठानवे': 98, 'निन्यानवे': 99
}

hindi_multipliers = {
    'सौ': 100, 'साै': 100, 
    'हज़ार': 1000, 'हजार': 1000, 
    'लाख': 100000, 
    'करोड़': 10000000, 'करोड': 10000000
}

def normalize_hindi_numbers(text):
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
        
        if clean_word in hindi_numbers or clean_word in hindi_multipliers:
            current_number_block.append(clean_word)
        else:
            if current_number_block:
                final_digit = process_number_block(current_number_block)
                output.append(final_digit)
                current_number_block = []
            output.append(word)
            
    if current_number_block:
        output.append(process_number_block(current_number_block))
        
    return " ".join(output)

print(normalize_hindi_numbers("मेरे पास दो हैं"))
print(normalize_hindi_numbers("यह पच्चीस और एक हज़ार है"))
print(normalize_hindi_numbers("मेरे पास तीन सौ चौवन रुपये हैं"))
