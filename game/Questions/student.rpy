init python:
    class Student:
            #Currently question types are [own department, generic]
            #list of probabilities for each question type (sums to 1)
           
            def __init__(self, name, image, probabilities = [0.8,0.2]):
                self.name = name
                self.image = image
                self.probabilities = probabilities

            def getQuestionType(self):
                rnum = renpy.random.random()
                lb = 0
                ub = self.probabilities[0]
                for i in range(len(self.probabilities)):
                    if lb <= rnum and rnum < ub:
                        return i
                    else:
                        lb += ub
                        ub +=self.probabilities[i+1]
                return len(self.probabilities)-1 #just incase

            def getQuestion(self, departmentQuestions):
                index = self.getQuestionType()
                if len(departmentQuestions)!=0 and (index==0 or len(genericQuestions)==0):
                    question = departmentQuestions.pop()
                elif len(genericQuestions)!=0: 
                    question = genericQuestions.pop()
                else:
                    question = "defaultQuestion"
                return question

label defaultQuestion:
    s "Hmm I'm out of questions to ask you... what should I do now?"
    menu:
        "I thought you just said you were out of questions... why are you asking me another!":
            $ ranking_meter -= lower_increase
            s "Sorry... don't get ants in your pants"
        "Please just leave me alone!":
            $ ranking_meter -= lower_increase
            s "I didn't realise you felt that way..."
        "You could go ask another teacher some questions, you do seem to love asking questions!":
            $ ranking_meter -= lower_increase
            s "Okay... Rude..."
        "You should have a splendid day!"
            $ ranking_meter += lower_increase
            s "Thats the nicest thing someone has said to me in a long time..."
    return