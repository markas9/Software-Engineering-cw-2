label initializeStudent:
    python:
        import random
        class Student:
            probabilities = [0.8,0.2] #list of probabilities for each question type (sums to 1)
           
            def __init__(self, name, image):
                self.name = name
                self.image = image
                
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

            def getQuestion(self, departmentQuestions):
                index = self.getQuestionType()
                if len(departmentQuestions)!=0 and (index==0 or len(genericQuestions)==0):
                    question = departmentQuestions.pop()
                else:
                    question = genericQuestions.pop()
                return question
    
    return