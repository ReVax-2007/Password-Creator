import random

class PasswordLogic:
    LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    NUMBERS = ['1','2','3','4','5','6','7','8','9','0']
    SYMBOLS = ['!','@','#','$','%','&','*','?','^',',','<','>','.','/','-','~']

    def generate(length=12,includeNumbers=True,includeSymbols=True):
        password = ""
        dictionary = PasswordLogic.LETTERS + [x.upper() for x in PasswordLogic.LETTERS]
        if includeNumbers:
            dictionary += PasswordLogic.NUMBERS
        if includeSymbols:
            dictionary += PasswordLogic.SYMBOLS
        
        for x in range(length):
            password =
        
        return password

if __name__ == "__main__":
    print(f"{PasswordLogic.generate()}")
