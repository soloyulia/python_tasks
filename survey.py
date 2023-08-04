class AnonymousSurvey():
    """сбор анонимных ответов на вопросы"""
    def __init__(self,question):
        self.question = question
        self.responses = []
    def show_question(self):
        """выводит вопрос"""
        print(self.question)
    def store_response(self,new_response):
        self.responses.append(new_response)
    def show_rezult(self):
        """выводит все полученные ответы"""
        print('Survey result: ')
        for response in self.responses:
            print(response)