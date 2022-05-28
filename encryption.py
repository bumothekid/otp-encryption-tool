from secrets import choice
from colorama import Fore
from string import ascii_letters, ascii_lowercase, printable

def generatePad(text: str) -> str:
    key =  ""

    for letter in text:
        if letter not in ascii_letters:
            key += letter
            continue

        key += ''.join(choice(ascii_lowercase))
    
    return key

def encryptText(text: str, pad: str) -> str:
    ciphertext = ""

    for textCharacter, padCharacter in zip(text, pad):
        if textCharacter not in ascii_letters:
            ciphertext += textCharacter
            continue

        characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        padIndex = characters.index(padCharacter)
        textIndex = characters.index(textCharacter)

        for _ in range(textIndex):
            character = characters[0]
            characters.pop(0)
            characters.append(character)
        
        ciphertext += characters[padIndex]
    
    return ciphertext

if __name__ == "__main__":
    text = input(f"{Fore.BLUE} Whats the text that you would like to encrypt? {Fore.RESET}\n ")

    if set(text).difference(printable):
        print(f"\n{Fore.RED} There are no not printable characters allowed. {Fore.RESET}")
        exit()
    
    while text[-1] == " ":
        text = text[:-1]

    pad = generatePad(text)
    print(f"{Fore.BLUE} Encryption Pad: {Fore.GREEN} {pad} {Fore.RESET}")

    encryptedText = encryptText(text, pad)
    print(f"{Fore.BLUE} Encrypted Text: {Fore.GREEN} {encryptedText} {Fore.RESET}")