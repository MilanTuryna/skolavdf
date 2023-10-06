koleje = 2
from math import ceil

class Cypher():
    def __init__(self, amount):
        self.amount = amount
        self.__open_text = None
        self.encoded = False

    # 1,2,3,4 kolejnice 5 kolejnic 
    def __declension(item_types, number):
        if(number < 1): 
            return item_types[0]
        elif(number < 5):
            return item_types[1]
        return item_types[2]

    def __build_rails(self, length):
        rails = []
        for x in range(self.amount):
            rails.append([""]*length)
        return rails

    def __transcript(self, open_text):
        return open_text
                    
    def encrypt(self, open_text, setter = True):
        self.encoded = True
        self.__open_text = self.__transcript(open_text)
        length = len(open_text)
        rails =  self.__build_rails(length)
        chars = [*open_text]
        i = 0
        krok = 1
        for count, letter in enumerate(chars):
            rails[i][count] = letter
            if i == self.amount-1:
                krok = -1
            elif i == 0:
                krok = 1
            i += krok
        result = ""
        for count, x in enumerate(rails):
            line = "".join(x)
            result += line.strip()
        if(setter): self.__cypher_text = result
        return result
    
    def decrypt(self, cipher_text):
        self.__cypher_text = self.__transcript(cipher_text)
        rails = self.__build_rails(len(self.__cypher_text))
        letters = [*self.__cypher_text]
        i = 0
        krok = 1
        for count, letter in enumerate(letters):
            rails[i][count] = "*"
            if i == self.amount-1:
                krok = -1
            elif i == 0:
                krok = 1
            i += krok
        fronta = 0
        result = [""]*10
        for line_count, line in enumerate(rails):
            for position, character in enumerate(line):
                if character == "*":
                    result[position] = letters[fronta]
                    fronta += 1
        self.__open_text = "".join(result)

        
    def get_open_text(self):
        return self.__open_text
    
    def get_cypher_text(self):
        return self.__cypher_text
    
    def __str__(self):
        if(self.encoded):
            amount_of_rails = self.amount + " " + self.__declension(["kolejnic", "kolejnice", "kolejnic"], self.amount)
            return f"Váš zašifrovaný text pro {self.__declension()} ({amount_of_rails})"
        else:
            return "Žádný text nebyl ještě zakódován!"
    

# zkouška
textinput = "TESTYRESTY"
print(f"Vstup: {textinput}")

test = Cypher(3)
test.encrypt(textinput)
cypher_text = test.get_cypher_text()
print(f"Zašifrovaný text: {cypher_text}")

test.decrypt("TYTETRSYSE")
print(f"Dešifrovaný text: {test.get_open_text()}")