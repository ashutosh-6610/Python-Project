questions=("how many elemnets are in periodic table?","which is the national aniaml of india?",
          "how many bones are in human body?","what is our planet name?","what is your name?","what is your age?")

options=(("A.116 ","B.117 ","C.118 ","D.119 "),
         ("A.tiger ","B.lion ","C.cat ","D.dog "),
         ("A.109 ","B.108 ","C.102 ","D.103 "),
         ("A.mars ","B.jupitar ","C.earth ","D.pluto "),
         ("A.ashu ","B.pnkj ","C.sonu ","D.kalu "),
         ("A.21 ","B.22 ","C.24 ","D.25"))

answer=("c","A","B","c","A","D")
guesses=[]
score=0
question_num=0
for question in questions:
    print("-------------------------------------------------")
    print(f"{question_num+1}.{question}")
    for option in options[question_num]:
       print(option)
       
       
    guess=input("enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess==answer[question_num]:
        score=score+1
    else:
        print("INCORRECT ANSWER!")
        print(f"The correct answer is {answer[question_num]}")
    question_num=question_num+1
print("-------------------------------------------------")
print(f"\nYour score is {score}")
    




    
    
