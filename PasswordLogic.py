import random

class PasswordLogic:
    LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    NUMBERS = ['1','2','3','4','5','6','7','8','9','0']
    SYMBOLS = ['!','@','#','$','%','&','*','?','^',',','<','>','.','/','-','~']

    @staticmethod #- allows to call back to PasswordLogic without needing instantate an object of the class
    def generate(length=12, includeNumbers=True, includeSymbols=True):
        password = ""
        dictionary = PasswordLogic.LETTERS + [x.upper() for x in PasswordLogic.LETTERS]
        if includeNumbers == True:
            dictionary += PasswordLogic.NUMBERS
        elif includeNumbers == False:
            pass
        if includeSymbols == True:
            dictionary += PasswordLogic.SYMBOLS
        elif includeSymbols == False:
            pass
        
        for x in range(length):
            password += random.choice(dictionary)
        
        return password

def main():
    length = int(input("Enter the length of the password: "))
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    
    generated_password = PasswordLogic.generate(length, include_numbers, include_symbols)
    print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()
