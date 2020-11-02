import random
from random import randint
import sys,time
import threading




def __Time_To_Live(): # Allowes code to run for specific time
    print('Time has ended. Game over')
timer = threading.Timer(2540, __Time_To_Live)
timer.start()



"""
CLASSESS AREA
"""
class Project_Update_Data:  #Hidden, just for user seeing.
    def __update(self):
        print(time.asctime())
    def __resources(self):
        '''
        :classess:  = "For main activities, except dice/bank"
        :functions: = 'For some main activities/ not to directly return code'
        :modules: = 'threating, sys, time, randint, random'
        '''
    def __game_goal_conditions(self):
        '''
        :Condition 1: Player has 2540 seconds to play, otherwise game over.
        :Condition 2: Game ends once player has 50 gold - see "gold" variable

        '''
    def __To_FIx_stuff(self):
        '''

        Gold indicator - returns false value for "gold" variable at the ShopKeeper interaction.


        '''
class Game_Rules:
    def ruls(self):
        def Rules_For_Main_Game(**rules):
            print(rules)
        Rules_For_Main_Game(howToPlay = 'Input a choice when given',badInput ='If input doesnt match, ignored')
FOO_RULS = Game_Rules()       

global gold
gold = 10
price = 1
inventory = 'Feeling good'
dice_1 = randint(1,6)
dice_2 = randint(1,6)
Shoopkeeper_prices = [10,20,30,40,50]
'''
PLAYER|MOBS
'''
class Player():
    def __init__(self,name, health, damage,gold):
        self.name = name
        self.health = health
        self.damage = damage
        self.gold = gold

class Player_actions(Player):
    def __init__(self,name,health,damage,gold,status):
        super().__init__(name,health,damage,gold)
        self.status = status
Pl = Player_actions('Aa',3,1,gold,inventory)


class Enemy():
    def __init__(self,name,health,damage):
        self.name= name
        self.health = health
        self.damage = damage

class Enemy_Actions(Enemy):
    def __init__(self,name,health,damage,retreat):
        super().__init__(name,health,damage)
        self.retreat = retreat
ENEMY = Enemy_Actions("Lurker",2,1,'cant fight anymore')


class Play_Dice_Start:
    def __init__(self,name,talk):
        self.name = name
        self.talk = talk
    def play_dice_rules(self):
        time.sleep(0.9)
        print('Random number from range 1-6 is chosen')
        time.sleep(0.9)
        print('The grater one wins')
Tav = Play_Dice_Start('name','talk')

'''
NPCs Classess
'''
class Shoopkeeper:
    def __init__(self,name,buy):
        self.name = name
        self.buy = buy
    def __StorePrice(self):
        print(Shoopkeeper_prices)
    @staticmethod
    def Purchase():
        buy_sth = input(f'Want to purchase a bottle of water {random.choice(Shoopkeeper_prices)} gold coins(Yes/No) : ')
        if buy_sth == 'Yes' and Pl.gold >=1:
            gold_takeaway = Pl.gold - price
            print(f' {price} gold have/has been taken. Your gold is {gold_takeaway}')
            print(CITY_MAIN_STREET_MAIN())
        if buy_sth == 'Yes' and Pl.gold <= 0:
            print('You dont have enough gold')
            print(Shoopkeeper.Purchase())
        if buy_sth == 'No':
            print(CITY_MAIN_STREET_MAIN())
        else:
            print(Shoopkeeper.Purchase())
SH = Shoopkeeper('Frogs','good')

global player_GOld
player_GOld = Pl.gold

global cost_gold
cost_gold = 10

class SleepIn:
    def __init__(self,name,talk):
        self.talk = talk
        self.name = name
    def rent(self,player_GOld,cost_gold):
        gold = 10
        player_GOld = gold
        cost_gold = 5
        rent_quest_1 = input('Do you want to rent a room(Yes/No) : ')
        if rent_quest_1 == 'Yes' and player_GOld < cost_gold:
            print('You dont have enough money to rent a room')
        elif rent_quest_1 == 'Yes' and player_GOld >= cost_gold:
            player_GOld - cost_gold
            print('Thank you for your purchase')
        else:
            pass
SleepIN = SleepIn('FrogdIIN','hello')



def Main_Bank():
    def Ban1():
        deposit_value = float(input('How much would you like to store : '))
        if Pl.gold < 1 or deposit_value < 1:
            print('Your deposit value is too small')
            print(Ban1())
        if Pl.gold >= 1 and deposit_value <= Pl.gold:
            after_deposit = Pl.gold - deposit_value
            stored_gold = deposit_value
            print(f'you stored {stored_gold} gold. Gold in deposit {deposit_value}')
        else:
            print('could not store that value')
            print(Ban1())
        def after_Bank():
            quest_13 = input('Do you want to store sth more(Yes/No) : ')
            if quest_13 == 'Yes':
                print(Ban1())
            else:
                print(CITY_MAIN_STREET_MAIN())
        return after_Bank()
    return Ban1()

global result
result = ['Win','Failure']
win = 'You have won! Gold is all yours'


class GameOptions:
    def option_1(self):
        return " 1 configure color"
    def option_2(self):
        return" 2 back"
    @staticmethod
    def after_option_1():
        pass
    @staticmethod
    def after_option_2():
        pass
OptsGame = GameOptions()







""""
FUNCTIONS AREA
"""
def Dice_Tavern(player_1 = dice_1, player_2 = dice_2):
    gold = 10
    question_tav = input('would you like to hear rules : ')
    if question_tav == 'Yes':
        print(Tav.play_dice_rules())
    else:
        pass
    bet = int(input('enter gold: '))
    if Pl.gold < bet:
        print('You cannot bet more gold than you have')
        return Dice_Tavern()
    print(f' you throw equals {player_1}, enemys is {player_2}')
    if player_1 > player_2:
        print(f'{Pl.name} is victorious')
        gold += bet
    if player_1 < player_2:
        gold -= bet
        print(f'{Pl.name} has lost')
    else:
        print('its a draw')
        Pl.gold + 0
    def after_game():
        prom = input('Do you want to play again(Yes/No) : ')
        if prom == 'Yes':
            print( Dice_Tavern())
        else:
            print(CITY_MAIN_STREET_MAIN())
    return after_game()
 




'''
CITY CODE AREA
'''



opts = "This is option area"
def Options_game():
    print(opts)
    print(OptsGame.option_1())
    print(OptsGame.option_2())
    
    ch = input('> ')
    if ch == '1':
        return OptsGame.after_option_1()
    elif ch == '2':
        return OptsGame.after_option_2()
def CITY_MAIN_STREET_MAIN():
    City_Options = input('What would you like to do in your city(ShopKeeper/Dice/Hotel/Bank) : ')
    if City_Options == 'Hotel':
        SleepIN.rent(10,5)
        return CITY_MAIN_STREET_MAIN()
    if City_Options == 'Dice':
        print(Dice_Tavern())
    if City_Options == 'Bank':
        print(Main_Bank())
    if City_Options == 'ShopKeeper':
        print(Shoopkeeper.Purchase())
    else:
        print(CITY_MAIN_STREET_MAIN())
    
def Start_game():
    time.sleep(0.6)                                  #STARTING MAIN GAME
    print(f'You\'ve been walking all on yourself')
    time.sleep(0.6)
    print(f'Suddenly you notice something like a city of some sort')
    time.sleep(0.6)
    print('Without a second of hesitation you decide to pay it a visit')
    time.sleep(0.6)
    print('The city turned out to be a massive one, filled with all sorts of buildings')
    time.sleep(0.6)
    print('It is still better than wondering outside, having some spare time, you decided to check it out')
    time.sleep(0.6)
    print(FOO_RULS.ruls())
    print(CITY_MAIN_STREET_MAIN())

    



'''
MAIN MENU ====================PRINT FIRST!!!!!
'''
def MainMenu_Options():
    print('   ######################    ')
    print('         #WELCOME#            ')
    print('   ######################')
    print('   1       -START-                    ')
    print('   2      -OPTIONS-                    ')
    print('   3       -QUIT-                    ')
    choice = input('> ')
    if choice == '1':
        Start_game()
    elif choice == '2':
        Options_game()
    elif choice == '3':
        quit()

import FunctionsForRPG
from FunctionsForRPG import Apply_Gold_Game_End
        
print(MainMenu_Options())
