import random
from pyscript import document
num=random.randint(1,10)
count=0
def check_guess():
    global count
    guess=document.getElementById("guess").value
    result=document.getElementById("result")
    if not guess: #checking if result is empty
        result.innerText="Enter a number!"
        return
    guess=int(guess) #string to int
    count+=1
    if guess==num:
        result.innerText=f"Correct! You took {count} tries!"
    elif guess<num:
        result.innerText="Go Higher!"
    else:
        result.innerText="Go Lower!"
