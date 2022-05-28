from colorama import Fore
from string import ascii_letters, printable


def decryptText(text: str, pad: str) -> str:
    decryptedText = ""

    for textCharacter, padCharacter in zip(text, pad):
        if textCharacter not in ascii_letters:
            decryptedText += textCharacter
            continue

        characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        charactersCopy = characters.copy()
        
        padIndex = characters.index(padCharacter)

        for _ in range(padIndex):
            character = charactersCopy[0]
            charactersCopy.pop(0)
            charactersCopy.append(character)

        textIndex = charactersCopy.index(textCharacter)
        
        decryptedText += characters[textIndex]
    
    return decryptedText

if __name__ == "__main__":
    pad = input(f"{Fore.BLUE} Please enter Encryption Pad: {Fore.RESET}\n ")

    if set(pad).difference(ascii_letters, " "):
        print(f"{Fore.RED} There are no numeric or special characters in the encryption pad allowed. {Fore.RESET}")
        exit()
    
    encryptedText = input(f"{Fore.BLUE} Please enter the Encrypted Text to decrypt: {Fore.RESET}\n ")

    if set(encryptedText).difference(printable):
        print(f"\n{Fore.RED} There are no not printable characters allowed. {Fore.RESET}")
        exit()

    decryptedText = decryptText(encryptedText, pad)
    print(f"{Fore.BLUE} Decrypted Text: {Fore.GREEN} {decryptedText} {Fore.RESET}")
