from data import question_data
from random import choice
class Question:
    def __init__(self,text:str,answer:bool) -> None:
        self.text=text
        self.answer=answer

class QuestionList:
    listOfQuestions=[]
    def __init__(self):
        for question in question_data:
            temp=Question(question["text"],bool(question["answer"]))
            self.listOfQuestions.append(temp)
    
    def getQuestion(self):
        question=choice(self.listOfQuestions)
        self.listOfQuestions.remove(question)
        return question
    
    def isQuestionsLeft(self):
        if(len(self.listOfQuestions)==0):
            return False
        return True