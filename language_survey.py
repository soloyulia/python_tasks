from survey import AnonymousSurvey
question = 'На каком языке вы научились говорить?'
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print('Нажмите для выхода q')
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)
print('Вывод результатов опроса:')
my_survey.show_rezult()