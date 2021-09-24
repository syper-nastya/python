action = input("Введите действие: ")
while action != "Выход":
    if action == "Сказка":
        fairytale = print('''Жил был мальчик. Учился он програмировать.
Он вырос и стало у него много денег!''')
    elif action == "Погаворка":
        proverb = print("Люби кататся, люби и саночки возить.")
    elif action == "Как дела":
        good = print("У меня всё отлично!!!")
    elif action == "Как тебя зовут":
        name = print("""У меня нет имени,
но ты можешь меня звать супер бот:))""")
    elif action == "Рифмы":
        popit = input("Скажи любое слово: ")
        print ("поп ито" + popit)
    action = input("Введите действие: ")
print ("Пока")     
        
    
        
    
    
