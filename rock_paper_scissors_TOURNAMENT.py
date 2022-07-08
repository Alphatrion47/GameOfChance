import random
print('****GAME START****')
def Game(comp, you):
    if you == comp:
        return print('draw')
    if you == 'x' and comp == 'p':
        return True
    if you == 's' and comp == 'x':
        return True
    if you == 'p' and comp == 's':
        return True
    if you == 's' and comp == 'p':
        return False
    if you == 'p' and comp == 'x':
        return False
    if you == 'x' and comp == 's':
        return False
    else:
        return print('invalid entry')

randno = random.randint(1,3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'p'
elif randno == 3:
    comp = 'x'

upoint = 0
compoint = 0

dict = {
    's' : 'Stone',
    'p' : 'Paper',
    'x' : 'Scissor'
}

while upoint < 5 and compoint < 5:
    randno = random.randint(1,3)
    if randno == 1:
        comp = 's'
    elif randno == 2:
        comp = 'p'
    elif randno == 3:
        comp = 'x'
    
 
    you = input("your turn, choose - stone(s), paper(p) or scissors(x)")

    b = Game(comp, you)

    if you in dict:
        print("you chose => ", dict[you])
        print("computer chose => ", dict[comp])
    else: print("Try again")

    if b == True:
        upoint += 1
        print(f"you win. \nScore is you - {upoint} vs comp - {compoint}")

    elif b == False:
        compoint += 1
        print(f"you lose. \nScore is you - {upoint} vs comp - {compoint}")

   

if upoint ==5:
    print('******Congrats you won the game!!******')
elif compoint ==5:
    print('******Oops you lost the game!!******')
