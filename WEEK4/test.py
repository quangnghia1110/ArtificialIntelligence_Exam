Morse_Sample = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
                   'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
                   '0': '-----'}
def word_to_morse(text):
    char_morse = ''
    for char in text:
        if char.upper() in Morse_Sample:
            char_morse = char_morse + Morse_Sample[char.upper()] + ' '
        elif char == ' ':
            char_morse = char_morse + ' '
    return char_morse.strip()
text = input("Nhập chuỗi cần mã hóa: ")
print(word_to_morse(text))
