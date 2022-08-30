import time
from playsound import playsound

rus_dict = {"а": "*-", "б": "-***", "в": "*--", "г": "--*", "д": "-**", "е": "*",
            "ё": "*", "ж": "***-", "з": "--**", "и": "**", "й": "*---", "к": "-*-", "л": "*-**",
            "м": "--", "н": "-*", "о": "---", "п": "*--*", "р": "*-*", "с": "***", "т": "-",
            "у": "**-", "ф": "**-*", "х": "****", "ц": "-*-*", "ч": "---*", "ш": "----", "щ": "--*-",
            "ъ": "--*--", "ы": "-*--", "ь": "-**-", "э": "**-**", "ю": "**--", "я": "*-*-", " ": "  "}

eng_dict = {"a": "*-", "b": "-***", "w": "*--", "g": "--*", "d": "-**", "e": "*",
            "v": "***-", "z": "--**", "i": "**", "j": "*---", "k": "-*-", "l": "*-**",
            "m": "--", "n": "-*", "o": "---", "p": "*--*", "r": "*-*", "s": "***", "t": "-",
            "u": "**-", "f": "**-*", "h": "****", "c": "-*-*", "ch": "----", "q": "--*-",
            "y": "-*--", "x": "-**-", " ": "  "}

special_characters = {"1": "*−−−−", "2": "**−−−", "3": "***--", "4": "****-", "5": "*****",
                    "6": "-****", "7": "--***", "8": "---**", "9": "----*", "0": "-----",
                      "_": "**--*-", "/": "-**-*", "@": "*--*-*"}


def sound_Translate(text):
    for i in text:
        if i == "-":
            playsound('dash.mp3')
        elif i == "*":
            playsound('pick.mp3')
        elif i == " ":
            time.sleep(0.01)


choice = None

try:
    choice = int(input("Введите 1 - чтобы перевести на азбуку Морзе\n"
                       " Введите 2 - чтобы перевести на русский или английский алфавит: "))
except:
    print("Вы написали не то, что надо, повторите попытку!!!")

if choice == 1:
    strText = str(input("Введите текст, который вы хотите перевести в азбуку Морзе: "))
    strText = strText.lower()

    strResult = ""
    for letter in strText:
        alp = rus_dict
        alp |= eng_dict
        alp |= special_characters
        alp = alp[letter]
        strResult += alp + " "

    print(strResult)
    sound_Translate(strResult)

elif choice == 2:
    choice = int(input("Введите 1 - чтобы перевести на русский язык\n"
                       "Введите 2 - чтобы перевести на английский язык: "))
    strResult = None
    if choice == 1:
        dictionary = rus_dict
        dictionary |= special_characters
        strText = str(input("Введите текст, который вы хотите перевести на русский язык: "))
        sound_Translate(strText)
        strText = strText.split(' ')
        strResult = ""
        rus_dict[""] = " "
        for letter in strText:
            for keys, value in rus_dict.items():
                if value == letter:
                    strResult += keys
        print(strResult)
    elif choice == 2:
        dictionary = eng_dict
        dictionary |= special_characters
        strText = str(input("Введите текст, который вы хотите перевести на английский язык: "))
        sound_Translate(strText)
        strText = strText.split(' ')
        strResult = ""
        eng_dict[""] = " "
        for letter in strText:
            for keys, value in eng_dict.items():
                if value == letter:
                    strResult += keys
        print(strResult)
    else:
        print("Чего ты хочешь сынок?")
else:
    print("Чего ты хочешь сынок?")
