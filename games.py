print("welcome to my computer quiz !")
playing =input("Do you want to play game " )
if playing.lower() != "yes":
    quit()
print("okay! let's play :)")
score =0
answer = input("what does CPU stand for ")
if answer =="central processing unit" :
    print('Correct!')
    score +=1
    
else:
    print('Incorrect :(')

answer = input("what does RAM stand for ")
if answer == "random access memory" :
    print('Correct!')
    score +=1
else:
    print('Incorrect :(')
    
answer = input("what does PSU stand for ")
if answer == "power supply unit" :
    print('Correct!')
    score +=1 
else:
    print('Incorrect :(')
    
answer = input("what does GPU stand for ")
if answer == "graphics processing unit" :
    print('Correct!')
    score +=1  
else:
    print('Incorrect :(')
    
    print("you score is " + str(score)+"." )
    print("you score is " + str(score/4 *100)+"." )

