 # NESNE TABANLI PROGRAMLAMA

#CLASS =>person (name, surname , birthday, calculateAge())
# instance(object)

# liste= [1, 2, 3]
# liste2= [1,2,3,4]



# result = type(liste)
# print(result)


############################################

#class

# class Person:
#     pass

#     # class attributes
#     address = 'no information'

#     # constructor ( yapıcı metod)
#     def __init__(self, name, year):

#         # object attributes
#         self.name = name
#         self.year = year
        

#     # instance methods
#     def intro(self):
#         print('hello there. I am ' + self.name)
#     # instance methods
#     def calculateAge(self):
#         return 2023 - self.year



# #object (instance)
# p1 = Person(name='ali',year= 1990)
# p2 = Person(name='yağmur',year= 1995)

# p1.intro()
# p2.intro()

# print(f'adım: {p1.name} ve yaşım: {p1.calculateAge()}')
# print(f'adım: {p2.name} ve yaşım: {p2.calculateAge()}')



# class Circle:
#     #class object attribute
#     pi = 3.14

#     def __init__(self, yaricap=1):
#         self.yaricap = yaricap


#         #methods
#     def cevre_hesapla(self):
#         return 2*self.pi * self.yaricap
        
#     def alan_hesapla(self):
#         return self.pi * (self.yaricap**2)
        
        
# c1 = Circle() 
# c2 = Circle(5)
    


# print(f"c1: alan = {c1.alan_hesapla} çevre = {c1.cevre_hesapla()}")
# print(f"c1: alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}")

#####################################

# İNHERİTANCE (KALITIM): MİRAS ALMA

#Person => name, lastname, age, eat(), run(), drink()
#Student(Person), Teacher(Person)

#Animal => Dog(Animal), Cat(Animal)

# class Person():
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#         print('Person Created')

#     def who_am_i(self):
#         print('I am a person') 

#     def eat(self):
#         print('I am a eating')   

# class Student(Person):
#     def __init__(self, fname, lname, number):
#         Person.__init__(self, fname, lname)
#         self.studentNumber = number
#         print('student created')
#     #override (aynı isimdeki metodun temel sınıfdakini ezmesi)
#     def who_am_i(self):
#         print('I am a student')

#     def sayHello(self):
#         print('Hello I am a student')


# class Teacher(Person):
#     def __init__(self, fname, lname, branch):
#         super().__init__(fname, lname,)
#         self.branch = branch

#     def who_am_i(self):
#         print(f'I am a {self.branch} teacher')


# p1 = Person("ali","yılmaz")
# s1= Student("çınar","turan", 1453)
# t1= Teacher('Serkan', 'Yılmaz', 'Math')



# print(p1.firstname + ' '+ p1.lastname )
# print(s1.firstname + ' '+ s1.lastname + ' ' + str(s1.studentNumber)  )

# p1.who_am_i()
# s1.who_am_i()

# p1.eat()
# s1.eat()

# s1.sayHello()
# t1.who_am_i()

##########################################################
# myList = [1,2,3]


# class Movie():
#     def __init__(self, title, director, duration):
#         self.title = title
#         self.director = director
#         self.duration = duration
#         print('movie objesi oluşturuldu')

#     def __str__(self):
#         return f"{self.title} by {self.director}"
    
#     def __len__(self):
#         return self.duration
    
#     def __del__(self):
#         print('film objesi silindi')

# m = Movie('film adı', 'yönetmen adı', 120)

# # print(str(myList))
# print(str(m))
# # print(len(myList))
# # print(len(m))

##########################################################

# QUESTİON

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer



# QUİZ

class Quiz:
    def __init__(self, question):
        self.questions = question
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-' + q)

        answer = input('cevap:  ')
        self.guess(answer)
        self.loadQuestions
    

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score+= 1
        self.questionIndex+= 1

        

    def loadQuestions(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()

    def showScore(self):
        pass


q1 = Question('en iyi programlama dili hangisidir', ['C#', 'PYTHON', 'JAVASCRİPT', 'JAVA'], 'PYTHON')
q2 = Question('en populer programlama dili hangisidir', ['C#', 'PYTHON', 'JAVASCRİPT', 'JAVA'], 'PYTHON')
q3 = Question('en çok kazandıran programlama dili hangisidir', ['C#', 'PYTHON', 'JAVASCRİPT', 'JAVA'], 'PYTHON')
questions = [q1,q2,q3]

quiz = Quiz(questions)

quiz.displayQuestion()






























