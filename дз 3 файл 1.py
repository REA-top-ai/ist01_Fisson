import random
name = input('Ваше имя?')
question= input('Задайте свой вопрос')
answer = ''
random_number = random.randint(1,12)
print(random_number)
# генерируется
if random_number == 1:
    answer = "Да, безусловно."
elif random_number == 2:
    answer = "Это решительно так."
elif random_number == 3:
    answer = "Без сомнения."
elif random_number == 4:
    answer = "Ответ туманный, попробуйте еще раз."
elif random_number == 5:
    answer = "Спросите еще раз позже."
elif random_number == 6:
    answer = "Лучше не говорить вам сейчас."
elif random_number == 7:
    answer = "Мои источники говорят «нет»."
elif random_number == 8:
    answer = "Прогноз не очень хороший."
elif random_number == 9:
    answer = "Очень сомнительно."
elif random_number == 10:
    answer = "высокий шанс."
elif random_number == 11:
    answer = "Можешь рассчитывать."
elif random_number == 12:
    answer = "Непонятно."
else:
    answer = "Oшибка."
if question=='':
    print("Если пользователь не задает никаких вопросов, то Magic 8-Ball не может принести удачу, иначе ткань реальности окажется под угрозой!")
else:
    if name!='':
        print(name + " спрашивает: " + question)
        print("Магического шар отвечает : " + answer)
    elif name=='':
        print('Вопрос:'+ question)
        print("Магического шар отвечает : " + answer)