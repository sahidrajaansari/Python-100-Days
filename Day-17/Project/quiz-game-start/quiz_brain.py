from question_model import Question
class QusetionBrain:
    score=0
    def isCorrect(self,question:Question,answer:bool):
        if(question.answer==answer):
            self.score+=1
            return True
        return False
    
    def getInput(self,question:Question):
        print(question.text)
        choice=True
        k=str(input("Input 1 for True and 2 for False :"))
        if(k==2):
            choice=False
        ans=self.isCorrect(question,choice)
        return ans