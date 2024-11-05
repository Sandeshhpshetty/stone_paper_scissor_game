import random

class Games:
    def computer(self):
        a=["stone","paper","scisser"]
        self.computers=random.choice(a)

    def person(self):
        a=["stone","paper","scisser"]
        self.persons=random.choice(a)

game=Games()
game.computer()
game.person()

print(f"computer choice : {game.computers} and",f"players choice :{game.persons}")

if game.computers==game.persons:
    print("match draw")


elif (game.computer=='stone' and game.persons=='paper') or\
  (game.computers=='paper' and game.persons=='scissor') or\
    (game.computers=='scissor' and game.persons=='stone'):
    print("palyer win")

else:
    print("computer win")