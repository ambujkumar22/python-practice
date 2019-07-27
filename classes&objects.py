class student: #class is created with the keyword class and then name of the class
    def __init__(self, name,phn,rollnum): #then a function is defined in it __init__(necesssary) and self(is like a this pointer and is also necessary)
        self.name = name #correct syntax to start the object details
        self.phn = phn
        self.rollnum = rollnum
    def phonecheck(self): #it is used to check the phone number
        if self.phn == 9958283840:
            return True
        else:
            return False

student1 = student("ambuj",9958283840,"15-CSE") #object is created
student2 = student("rishabh",99999999,"16-CSE") #another object
print(student1.rollnum) #object is accessed and print rollnumber
print(student2.name)
print(student2.phonecheck())
#this class can be imported to another file with the keyword import (file name)

#multiple choice question
paper = [ #list which contains three questions
    "1) What is the colour of an apple?\na) red\nb) yellow\nc) white\n",
    "2) What is the colour of a banana?\na) red\nb) yellow\nc) white\n",
    "1) What is the colour of a pommagrenade?\na) red\nb) yellow\nc) white\n"
]

class question: #question class which has a question parameter and a answer parameter
    def __init__(self,ques,answer):
        self.ques = ques
        self.answer = answer

questions = [
    question(paper[0], "a"), #in this list class is called or objects are created
    question(paper[1], "b"),
    question(paper[2], "a")
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.ques)
        if answer == question.answer:
            score += 1
    print("you got "+ str(score) + "/" + str(len(questions)) + " correct.")

run_test(questions)