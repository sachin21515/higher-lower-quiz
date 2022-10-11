
from game_data import data
import random
import os

def check_followers():
  game_should_continue = True
  current_score = [0]
  while game_should_continue:
    num1 = random.randint(0, len(data)-1)
    
    num2 = [0]
    
    def num():
      num2[0]=(random.randint(0, len(data)-1))
      if num1==num2[0]:
        num()
    num()  
  
    option_a = f"Compare A: {data[num1]['name']}, a {data[num1]['description']}, from {data[num1]['country']}"
    print(option_a)
    
    option_b = f"Compare B: {data[num2[0]]['name']}, a {data[num2[0]]['description']}, from {data[num2[0]]['country']} "
      
    print(option_b)
    user_input = input("Who has more followers? Type 'A' or 'B': ")
    if user_input.lower() == 'a':
      if data[num1]['follower_count']>data[num2[0]]['follower_count']:
        current_score[0]+=1
        os.system('clear')
        print(f"You are right! Current score: {current_score[0]}")
        
      else:
        os.system('clear')
        print(f"sorry that's wrong Final score: {current_score[0]}")
        game_should_continue = False
    
    else:
      if data[num1]['follower_count']<data[num2[0]]['follower_count']:
        current_score[0]+=1
        os.system('clear')
        print(f"You are right! Current score: {current_score[0]}")
        
      else:
        os.system('clear')
        print(f"sorry that's wrong Final score: {current_score[0]}")
        game_should_continue = False

check_followers()
