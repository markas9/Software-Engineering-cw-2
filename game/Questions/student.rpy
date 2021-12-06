label initializeStudent:
    python:
        import random

        #define generic question lists
        genericQuestions = ["genericQ1", "genericQ2", "genericQ3", "genericQ4", "genericQ5"]
        renpy.random.shuffle(genericQuestions)

        
        class Student:
            #Currently question types are [own department, generic]
            #list of probabilities for each question type (sums to 1)
           
            def __init__(self, name, image, probabilities = [0.8,0.2]):
                self.name = name
                self.image = image
                self.probabilities = probabilities

            def getQuestionType(self):
                random.seed()
                rnum = random.random()
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
                else:
                    question = genericQuestions.pop()
                return question
    
    return