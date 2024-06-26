from question_model import QuestionList
from quiz_brain import QusetionBrain
questionList=QuestionList()
questionBrain=QusetionBrain()

while(True):
    if(questionList.isQuestionsLeft()):
        question=questionList.getQuestion()
        answeris=questionBrain.getInput(question)
        print(f"Your answer is {answeris} and Current Score is {questionBrain.score}")
    else:
        print(f"You Won your Score is {questionBrain.score}")
        break
    print()