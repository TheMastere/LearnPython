def main():
    age = int(input('Введите числовое обозначение возраста человека: '))  # задаем значение возраста
    if age < 3:
        print('Вы новорожденный годовасик')
    if age >= 3 and age <= 5: # проводим проверку на возраст
        print('Вы ходите в детский сад') # выводим сообщение
    if age >= 6 and age <= 17:
        print('Вы ученик школы')
    if age >= 18 and age <= 23:
        print('Вы студент вуза')
    if age >= 24 and age <= 60:
        print('Вы работник года в макдональдс/работаете работу')
    if age >= 61 and age <= 65:
        print('Вы женщина - пенсионер')
    if age >= 66:
        print('Вы мужчина или женщина - пенсионер')
if __name__ == '__main__':
    main()