import random
logo=''' 
                                      .------.
                   .------.           |A .   |
                   |A_  _ |    .------; / \  |
                   |( \/ )|-----. _   |(_,_) |
                   | \  / | /\  |( )  |  I  A|
                   |  \/ A|/  \ |_x_) |------'
                   `-----+'\  / | Y  A|
                         |  \/ A|-----'    hjw
                         `------'
                                                '''
def calculate(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)  


cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def deal_card():
    card=random.choice(cards)
    return card

user_card=[]
computer_card=[]
computer_score=-1
user_score=-1



for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

def play_game(): 
    print(logo) 
    is_game_over=False 
    while not is_game_over:
        user_score=calculate(user_card)
        computer_score=calculate(computer_card)
        print(f"your score={user_score},users csrds={user_card}")
        print(f"computers cards={computer_card[0]}")    


        calculate(cards)


        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            x=input("type y to continue or n for no ")
            if x=="y":
                    user_card.append(deal_card())
                    new_score=calculate(user_card)  
            else:
                is_game_over=True  
    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate(computer_card)            


    def compare(user_score,computer_score):
        if computer_score==user_score:
            return "its a draw"
        elif computer_score==0 or user_score>21:
            return "user loses,computer wins"
        elif user_score==0 or computer_score>21:
            return "computer loses,user wins"
        else:
            if user_score>computer_score:
                return "user wins"
            else :
                return "computer wins"

   
    print(compare(user_score,computer_score))
    print(f"your final score={user_score}, your cards={user_card}")
    print(f"computers final score={computer_score},computers cards={computer_card}")        

while input('type \'y\' for resart/new game or \'n\' for stopping:')=='y':
    print("\n"*20)
    play_game()         