#Hangman python code
from random import randint
#intro
print('Welcome to Hangman!')

#Word Selection
words=['chicken','penguin','pigeon','crow']
selectedword=words[randint(0,3)]
#Word Display
hangman=list(selectedword)
WordDisplay=hangman
WordDisplay = ["_" for e in WordDisplay]
print(WordDisplay)
print('The word has '+ str(len(selectedword))+ ' letters')

#User lives
lives=10

print('YOU HAVE ' + str(lives) +' lives')

#User Guesses
correctnumberletters=0
i=0
listofcorrectindex=[]
while i<lives:
    x=input('Enter a letter:').lower()
    if len(x)>1:
        print("Please enter a single letter!")
    elif x.isalpha()==False:
        print("Wrong input!")
    else:
     #Correct Guess
      if x in hangman:
        print('Correct Guess!!! Lives left '+str(lives-i)+' | Letters left '+ str(len(hangman)-1))
        numberofoccurance=hangman.count(x)
        if numberofoccurance==1:
           positionofcorrectguess=hangman.index(x)
           WordDisplay[positionofcorrectguess]=x
           print(WordDisplay)
        else:
            for i in range(len(hangman)):
                if hangman[i]==x:
                    listofcorrectindex.append(i)

            for i in listofcorrectindex:
                WordDisplay[i]=x
            print(WordDisplay)
    #wrong guess
      else:
        i+=1
        print('Wrong Guess! Lives left ' + str(lives-i)+' | Letters left '+ str(len(hangman)-1))
        print(WordDisplay)
    #game completion
      if ("_" not in WordDisplay):
        print("Game is completed!!!")
        break
