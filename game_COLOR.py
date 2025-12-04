import os, sys, time, random
from os import system
from time import sleep as s
from termcolor import colored as c
import importlib.util
name = 0 #do not move this line
def clear():
    if name == 'nt':
        _ = system('cls')
    
    else:
        _ = system('clear')

#ALL CODE MUST GO BELOW THIS LINE, UNLESS IT IS AN IMPORT OR FUNCTION.

module_name = "termcolor"

spec = importlib.util.find_spec(module_name)
clear()
if spec is not None:
    print(c("You installed termcolor correctly! Good Job.", 'light_blue', attrs=['bold', 'underline']))
else:
    print("'termcolor' is not installed. Please type 'pip install termcolor' in your terminal.")
    sys.exit()

name = 0
FORCE_COLOR = 'light_blue'

#sadly, due to codio's inablility to bring data between runs, this must be updated yourself.
highuser = "jartycuck_hunter"
highscore = 81000000341736636768782007240
highgame = ["Dice"]
newhigh = 0
beststreak = 0
print("")
showtitle = int(input("Show Big Title? (PC Recommended, 1 for YES, 0 For NO) "))
if showtitle == 1:
    clear()
    print("")
    print(c(" /$$$$$$$$ /$$                         /$$$$$$                      /$$                    ", 'green', attrs=['bold','blink']))
    print(c("|__  $$__/| $$                        /$$__  $$                    |__/                    ", 'green', attrs=['bold','blink']))
    print(c("   | $$   | $$$$$$$   /$$$$$$        | $$  \__/  /$$$$$$   /$$$$$$$ /$$ /$$$$$$$   /$$$$$$ ", 'green', attrs=['bold','blink']))
    print(c("   | $$   | $$__  $$ /$$__  $$       | $$       |____  $$ /$$_____/| $$| $$__  $$ /$$__  $$", 'green', attrs=['bold','blink']))
    print(c("   | $$   | $$  \ $$| $$$$$$$$       | $$        /$$$$$$$|  $$$$$$ | $$| $$  \ $$| $$  \ $$", 'green', attrs=['bold','blink']))
    print(c("   | $$   | $$  | $$| $$_____/       | $$    $$ /$$__  $$ \____  $$| $$| $$  | $$| $$  | $$", 'green', attrs=['bold','blink']))
    print(c("   | $$   | $$  | $$|  $$$$$$$       |  $$$$$$/|  $$$$$$$ /$$$$$$$/| $$| $$  | $$|  $$$$$$/", 'green', attrs=['bold','blink']))
    print(c("   |__/   |__/  |__/ \_______/        \______/  \_______/|_______/ |__/|__/  |__/ \______/ ", 'green', attrs=['bold','blink']))
    print("")                                                                                                              
    print(c("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-", 'green', attrs=['bold','blink']))                                                                                                             
                                                                                                              
else:
    clear()
    print("")
    print(c("-.- |    _    /¨\      ___ o", 'green'))
    print(c(" |  |-. |_|   |   /¨¨\ \_. _ ,_  /¨\\", 'green'))
    print(c(" |  | | L_-   \_/ \_/| __/ | | | \_/ ", 'green'))
    print(c("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~", 'green'))
    print("")
username = str(input(c("What is Your Name? ", 'light_green')))
print("")
money = random.randint(200,2000)
if username == "deadbeatdad":
    money = 100000
    print(c("Ready To Gamble Your Kid's College Fund?", 'red'))
if username == "thrembo_dev":
    print(c("Hello soyteen, how can I help you?", "light_magenta", attrs=['bold', 'underline']))
    money = int(input("How much money do you need today? "))
luck = 0
debt = 0
hardmode = 0
ach1 = 0
game = 1
streak = 0
jackwin = 5
dicewin = 5
colorwin = 0
insidewin = 0
losestreak = 0
bestinrun = 0
print("Welcome To The Casino, You have ", money, " dollars. GAMBLE YOUR LIFE AWAY.")
areaselect = 1
while areaselect != 0:
    area = input("Where Do You Want To Play? [Blackjack] [Dice] [Slots] [Roulette] ")
    if area == "Blackjack" or area == "Dice" or area == "Slots" or area == "Roulette" or area == "blackjack" or area == "dice" or area == "slots" or area == "roulette":
        areaselect = 0
    else:
        clear()    
        print(c("Invalid Option, Retry.", 'red'))
arealist = []
arealist.append(area)
turnsindebt = 0
while 1:
    if debt <= 0 and hardmode == 1:
        money = (money*turnsindebt)+1
    if bestinrun < money:
        bestinrun = money
    if hardmode == 1:
        if debt > 0:
            debt -= money/2
            print("Thanks for the money kid!")
            print("")
            turnsindebt += 1
    allin = 0
    clear()
    quote = random.randint(0,20)
    print(c("                                             -$-  Funny Casino Game  -$-", 'light_green', attrs=['bold']))
    print(c("------Highscore------", 'blue'))
    print("User: ", highuser)
    print("Score: ", highscore)
    print("Game: ", highgame)
    print(c("I got really lucky in B1.", 'blue'))
    print(c("---------------------", 'blue'))
    print("")
    print(c("----====+Money Stats+====----", 'dark_grey'))
    print("Most Money this run: ", bestinrun)
    if debt > 0:
        print("Debt: ", debt)
    print(c("----====+           +====----", 'dark_grey'))
    print("")
    print("Name: ", username)
    print("Money: ", money)
    print("Game: ", area)
    print("")
    if quote > 0:
        if quote == 1:
            print("I LOVE GAMBLING")
        elif quote == 2:
            print("Don't Quit Now")
        elif quote == 3:
            print("As RAXDFLIPNOTE once said...")
        elif quote == 4:
            print("It's mathematically impossible to win against the casino, but you can try!")
        elif quote == 5:
            print("Ur doin great lad. :3")
        elif quote == 6:
            print("99% Of Gamblers Quit Before they Win Big!")
        elif quote == 7:
            print("Here at Arby's™, all our food keeps blowing up!")
        elif quote == 8:
            print("Gambling Is Awesome!")
        elif quote == 10:
            print("ohmygod KITTY YAYYYYYYYY")
        elif quote == 11:
            print("'I'm Gonna Touch Gabe, Appropriately.' - Izak Patton")
        elif quote == 12:
            print("Are we so back or are we cooked?")
        elif quote == 13:
            print("The Different Games have different luck and money-making stats!")
        elif quote == 14:
            print("'I need my chinese brainrot app.' - Izak Patton")
        elif quote == 15:
            print("It is Advised To Only Bet half Of what you have... but who cares? GO ALL IN!!!")
        elif quote == 16:
            print("It's Better to Pee In The Shower Than It Is To Shower In The Pee.")
        elif quote == 17:
            print("'All Clothing Is Unisex if you Think About It long enough.' - ghandi, the art of war (i think)")
        elif quote == 18:
            print("♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪")
        elif quote == 19:
            if area == "Blackjack":
                print("The Dealer Lies About Their Score Withing a Range of 1-5 less than what he has. Be sure to account for that when playing!")
            elif area == "Dice":
                print("The Dice Are Luck Based, But They will roll lower the more you've won, and high the more you've lost!")
            elif area == "Slots":
                print("Slots? A True Gambler I See...")
        elif quote == 20:
            print("Part I: Feuerbach. | Opposition of the Materialist and Idealist Outlook | A. Idealism and Materialism | The Illusions of German Ideology")
                

        print("")
    print("Streak: ", streak)
    #rank system:
    if username == "thrembo_dev":
        print(c("Developer Mode in Use", 'light_cyan'))
    elif money >= 10000000:
        print("")
        print(c("Rank: Casino Killer", 'magenta'))
    elif money >= 1000000:
        print("")
        print(c("Rank: Elite Gambler", 'yellow'))
    elif money >= 10000:
        print("")
        print(c("Rank: Average Gambler", 'green'))
    elif money >= 1000:
        print("")
        print(c("Rank: Lucky", 'green'))
    elif money < 0:
        print(c("Rank: How Did We Get here?", 'light_magenta', 'on cyan', attrs=[bold]))
    if money < bestinrun and money < 1000:
        if bestinrun >= 10000000:
            print("")
            print(c("Casino's Revenge", 'light_magenta'))
        elif bestinrun >= 1000000:
            print("")
            print(c("Fell Off", 'light_red'))
        elif bestinrun >= 10000:
            print("")
            print(c("Light Work, No Reaction.", 'light_green'))
        elif bestinrun >= 1000:
            print("")
            print(c("Not Important.", 'cyan'))
        elif bestingrun >= 0:
            print("")
            print(c("Heavy in Tree? What how? What how?", 'blue'))
    
    else: 
        print("")
    print("")
    if streak > beststreak:
        beststreak = streak
    if money > highscore:
        highscore = money
        highuser = username
        highgame = arealist
        newhigh = 1
    print("Bet any Number, or type -1, to bet all, or -2 to switch games.")
    action = int(input("How Much Would You Like To Bet? "))
    if action == -1:
        allin = 1
        action = money
    elif action == -2:
        areaselect = 1
        clear()
        while areaselect != 0:
            print(c("------------------------------------", 'light_blue'))
            print("[Blackjack] [Dice] [Slots] [Roulette]")
            area = input("What Do You Want To Play? ")
            if area == "Blackjack" or area == "Dice" or area == "Slots" or area == "Roulette" or area == "blackjack" or area == "dice" or area == "slots" or area == "roulette":
                areaselect = 0
                action = money+1
                if not area in arealist:
                    arealist.append(area)
            else:
                print(c("Invalid Option, Retry.", 'red'))
    if action <= money or not action >= 0:
        if area == "Blackjack" or area == "blackjack":
            clear()
            jackwin = 0
            jackplay = 1
            playertotal = 0
            dealertotal = 0
            dealer = []
            player = []
            dealer.append(random.randint(1,10))
            dealer.append(random.randint(1,10))
            player.append(random.randint(1,10))
            player.append(random.randint(1,10))
            while jackplay == 1:
                dealertotal = 0
                playertotal = 0
                print(c("---+---+---+---+---+---+---+---", 'light_magenta'))
                for x in dealer:
                    dealertotal += x
                for y in player:
                    playertotal += y
                if dealertotal > 7:
                    print("Dealer: ", dealertotal - random.randint(1,5))
                else:
                    print("Dealer: ", random.randint(2,10))
                    hint = random.randint(1,10)
                    if hint < 8 and hint > 5:
                        print(c("Random Guy: Hey dude! The Dealer's Lying! His Score is Between 1 and 7!", 'cyan'))
                print(username,":", player)
                print("")
                print("Actions: [Stay] [Hit] [Fold] [Guess] [Score]")
                print("")
                print(c("---+---+---+---+---+---+---+---", 'light_magenta'))
                actionjack = input("Your Action? ")
                if actionjack == "Stay" or actionjack == "Hit" or actionjack == "Fold" or actionjack == "Guess" or actionjack == "Score" or actionjack == "stay" or actionjack == "hit" or actionjack == "fold" or actionjack == "guess" or actionjack == "score":
                    if actionjack == "Stay" or actionjack == "stay":
                        if dealertotal < playertotal and dealertotal < 18:
                            dealer.append(random.randint(1,10))
                            dealertotal = 0
                            for x in dealer:
                                dealertotal += x
                            print("Dealer Hit")
                        else:
                            print("Dealer Stays...")
                            s(.5)
                        if dealertotal > 21:
                            dealerlose = dealertotal
                            dealertotal = 0
                            print("Dealer Lost...")
                            print("Dealer Had ", dealerlose)
                            s(2)
                        if playertotal > dealertotal:
                            jackwin = 1
                            jackplay = 0
                            clear()
                        elif playertotal == dealertotal:
                            jackwin = 2
                            jackplay = 0
                            clear()
                        elif dealertotal > playertotal:
                            jackwin = 0
                            jackplay = 0
                            clear()
                    elif actionjack == "Hit" or actionjack == "stay":
                        player.append(random.randint(1,10))
                        playertotal = 0
                        for y in player:
                            playertotal += y
                            if playertotal > 21:
                                jackwin = 0
                                jackplay = 0
                                clear()
                        clear()
                    elif actionjack == "Fold" or actionjack == 'fold':
                        if playertotal < dealertotal:
                            jackwin = 2
                            jackplay = 0
                            clear()
                        elif playertotal > dealertotal:
                            jackwin = 0
                            jackplay = 0
                            clear()
                    elif actionjack == "Guess" or actionjack == 'guess':
                        guess = int(input("What Is The Dealer's Score? (Hint: The Chart Is Untrue): "))
                        if guess == dealertotal:
                            jackwin = 1
                            jackplay = 0
                            clear()
                            print(c("You Guessed Correctly!", 'green'))
                            s(1)
                            clear()
                        else:
                            clear()
                            print(c("EHHHHH, WRONG", 'red'))
                            s(2)
                            jackwin = 0
                            jackplay = 0
                            clear()
                    elif actionjack == "Score" or actionjack == 'score':
                        print("Your Current Score Is")
                        print("")
                        print(playertotal)
                        print("")
                else:
                    print(c("Invalid Option, Retry.", 'red'))
        elif area == "Roulette" or area == "roulette":
            insidewin = 0
            colorwin = 0
            spinchoice = 0
            while spinchoice != 1:
                clear()
                print(c("Color: Bet on Red or Black for a small prize.", 'yellow'))
                print(c("Number: Bet On Any Number Between 1 and 50 for a massive prize!", 'green'))
                print("")
                betchoice = input("What would You like To bet on? [Color] [Number]")
                if betchoice == "Color" or betchoice == 'color':
                    colorpick = 0
                    clear()
                    while colorpick != 1:    
                        colorchoice = input("Red or Black? (50/50) ")
                        if colorchoice == "Red" or colorchoice == 'red':
                            colorpick = 1
                        elif colorchoice == "Black" or colorchoice == 'black':
                            colorpick = 1 
                        else:
                            print("Invalid color Choice.")
                    colortonumber = 0
                    if colorchoice == "Red" or colorchoice == 'red':
                        colortonumber = 1
                    elif colorchoice == "Black" or colorchoice == 'black':
                        colortonumber = 2
                    spinchoice = 1
                elif betchoice == "Number" or betchoice == 'number':
                    numberpick = 0
                    clear()
                    while numberpick != 1:
                        numberchoice = int(input("Select A Number 1 to 50: "))
                        if numberchoice > 0 and numberchoice < 51:
                            numberpick = 1
                            spinchoice = 0

                        else:
                            print(c("Invalid Number Choice, Retry. (1-50)", 'red'))
                else:
                    print(c("Invalid Choice, Retry.", 'red'))
            wincolor = random.randint(1,2)
            winnumber = random.randint(1,50)
            if betchoice == "Color" or betchoice == 'color':
                if colortonumber == wincolor:
                    colorwin = 1
                    clear()
            elif betchoice == "Number" or betchoice == 'number':
                if numberchoice == winnumber:
                    insidewin = 1
                    clear()
            else:
                clear()
                



        elif area == "Dice" or area == 'dice':
            clear()
            playerdice = []
            house = []
            house.append(random.randint(1,6))
            house.append(random.randint(1,6))
            if losestreak <= 3 and streak <= 3:
                playerdice.append(random.randint(1+losestreak,6))
                playerdice.append(random.randint(1+streak,6))
            elif losestreak > 3:
                playerdice.append(random.randint(4,6))
                playerdice.append(random.randint(3,6))
            elif streak > 3:
                playerdice.append(random.randint(1,6))
                playerdice.append(random.randint(1,4))
            diceplay = 1
            housetrade = 0
            dicetrade = 0
            urcooked = 0
            while diceplay != 0:
                housetotal = 0
                dicetotal = 0
                for x in house:
                    housetotal += x
                for y in playerdice:
                    dicetotal += y
            
                print(c("---------=====---------", 'yellow'))
                print("House: ", house,)
                print(c(""))
                print(username,": ", playerdice)
                print(c("---------=====---------", 'yellow'))
                if housetotal > dicetotal and dicetrade == 1:
                    print("")
                    print(c("I Hope You didn't go All In!", 'red'))
                    print("")
                print("Actions: [Stay] [Trade]")
                diceact = input("Action: ")
                if diceact == "Stay" or diceact == 'stay' or diceact == "Trade" or diceact == 'trade':
                    if diceact == "Stay" or diceact == 'stay':
                        clear()
                        if housetotal >= dicetotal:
                            for x in house:
                                if x > 6 and housetrade != 1:
                                    house.remove(x)
                                    house.append(random.randint(1,6))
                                    housetrade = 1
                            housetotal = 0
                            for x in house:
                                housetotal += x
                        if dicetotal > housetotal:
                            dicewin = 1
                            diceplay = 0
                        elif dicetotal == housetotal:
                            dicewin = 2
                            diceplay = 0
                        else: 
                            dicewin = 0
                            diceplay = 0
                    elif diceact == "Trade" and dicetrade != 1 or diceact == "trade" and dicetrade != 1:
                        clear()
                        print("Your Dice: ", playerdice)
                        print("Total: ", dicetotal)
                        print("")
                        tradeact = int(input("What Dice Would You Like To Trade? (1-6 Integer Value) "))
                        for f in playerdice:
                            if f == tradeact and dicetrade != 1:
                                playerdice.remove(f)
                                playerdice.append(random.randint(1,6))
                                dicetrade = 1
                    elif diceact == "Trade" and dicetrade == 1:
                        clear()
                        print(c("Trade Already Made, Invalid.", 'red'))
                else:
                    clear()
                    print(c("Invalid Action, Retry.", 'red'))
        elif area == "Slots":
            luck = random.randint(1+losestreak,20-streak)
        if luck > 10 or jackwin == 1 or dicewin == 1:
            calc = 0
            calc = action*2
            if area == "Roulette" or area == 'roulette':
                money = money + (action*(2+losestreak+streak))
            else:
                money = money + (action*2)
            if area == "Slots" or area == 'slots':
                clear()
                print("[O][O][O]")
                s(.3)
                clear()
                print("[O][X][O]")
                s(.3)
                clear()
                print("[O][X][X]")
                s(.3)
                clear()
                print("[X][X][X]")
            elif area == "Blackjack" or area == 'blackjack':
                print("Dealer had ", dealertotal)
                print("")
            print("You Made ", calc, "Dollars!")
            s(1)
            streak += 1
            losestreak = 0
        elif jackwin == 2:
            print("You Tied With The Dealer. No Money Was Gained or Lost.")
            s(2)
            streak = 0
            losestreak = 0
        elif dicewin == 2:
            print("You tied with the House, No Money was Gained or Lost.")
            s(2)
            streak = 0
            losestreak = 0
        elif colorwin == 1:
            money = money*(2+losestreak)
        elif insidewin == 1:
            money = money*(10+(losestreak*losestreak))
        else:
            if area == "Slots" or area == 'slots':
                clear()
                print("[X][O][O]")
                s(.3)
                clear()
                print("[O][X][X]")
                s(.3)
                clear()
                print("[X][O][X]")
                s(.3)
                clear()
                print("[O][O][X]")
            calc = 0
            calc = action
            money -= action    
            print("You lost ", calc, "Dollars.")
            streak = 0
            losestreak +=1
            s(1)
    if money <= 0:
        clear()
        object = random.randint(1,10)
        if object == 1:
            object = "Cheeseburger"
        elif object == 2:
            object = "2007 Nissan Altima"
        elif object == 3:
            object = "Whole Walmart™ Bread Section You Always Wanted"
        elif object == 4:
            object = "3 Whole Popcorn Kernels"
        elif object == 5:
            object = "Highscore"
        elif object == 6:
            object = "Sexual Relationship with ",highuser
        elif object == 7:
            object = "5 Trillion Dollars"
        elif object == 8:
            object = "Private Airliner"
        elif object == 9:
            object = "death by gettin' shot in the head, just like JFK"
        elif object == 10:
            object = "One Gallon of Whole Milk. All to yourself"
        print("You Lost.")
        print("Betting ", action, " made you lose.")
        if area == "Blackjack" or area == 'blackjack':
            jacklosscalc = dealertotal - playertotal
            print("Dealer Had ", dealertotal, ", ", jacklosscalc, "more than you.")
            print("Highest Streak: ", beststreak, )
        print("")
        if money > highscore:
            print("Your did it! You got a new highscore! Screenshot that and bring it to dylan so he can publish new code.")
        elif money == highscore:
            print("awwww, so close")
        else:
            print("Never Give Up On That",object,"!")
        print("")
        if username == "thrembo_dev":
            highscore = c(highscore, 'light_red', attrs=['strike'])
        if newhigh == 1:
            print(c("New Highscore!", 'light_blue', attrs=['bold','underline']))
            print(c("-------------------", 'blue'))
            print(username)
            print(highscore)
            print(area)
            if hardmode == 1:
                print(c("Won After Going In Debt. BASED!1!!!11!", 'green', attrs=['bold']))
            print(c("-------------------", 'blue'))
            if username != 'thrembo_dev':
                print("")
                print(c("Go Tell Dylan Nemeth So It Can Be Updated.", 'blue'))
            else:
                print(c("Developer Tools Are Openly available to anyone who can read code.", 'light_magenta'))
                print("")
                print(c("-----------------------+----------------------", 'magenta'))
                print(c("If you want a highscore, please play normally.", 'light_cyan'))
                print(c("-----------------------+----------------------", 'magenta'))
            clear()
            print(c("Hey, kid, wanna take a loan? (Activate Hard Mode)", 'light_red', attrs=['bold', 'underline']))
            print(c("Get more money when you win, but you also gotta pay off an exorbatant amount of money."))
            goindebt = int(input("Type 1 for yes, anything else for no. "))
            if goindebt == 1:
                hardmode = 1
                money = 1000
                debt = 100000
            else:
                print(c("Lame.", 'red'))
                break