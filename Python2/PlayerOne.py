p1 = input("Player 1, enter rock, paper, or scissors: ").lower()
p2 = input("Player 2, enetr rock, paper, or scissors: ").lower()

if p1 == p2:
    print("tie")
else:
  if p1 == "rock":
    if p2 == "scissors":
      print("player 1 wins")
    else:
      print("Player 2 wins")
     elif p1 == "paper":
        if p2 == "rock":
          print("player 1 wins")
        else:
         print("player 2 wins")
     elif p1 == "scissors":
        if p2 == "paper":
          print("Player 1 wins")
        else:
          print("player 2 wins")
        
