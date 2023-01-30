print("""
                                                                                                                                                
,--.   ,--.  ,--.    ,--.  ,--.           ,------.           ,--.    ,------. ,--.   ,--.,--.                   ,--.  ,--.                 ,--. 
|  |   `--',-'  '-.,-'  '-.|  | ,---.     |  .--. ' ,---.  ,-|  |    |  .--. '`--' ,-|  |`--',--,--,  ,---.     |  '--'  | ,---.  ,---.  ,-|  | 
|  |   ,--.'-.  .-''-.  .-'|  || .-. :    |  '--'.'| .-. :' .-. |    |  '--'.',--.' .-. |,--.|      \| .-. |    |  .--.  || .-. || .-. |' .-. | 
|  '--.|  |  |  |    |  |  |  |\   --.    |  |\  \ \   --.\ `-' |    |  |\  \ |  |\ `-' ||  ||  ||  |' '-' '    |  |  |  |' '-' '' '-' '\ `-' | 
`-----'`--'  `--'    `--'  `--' `----'    `--' '--' `----' `---'     `--' '--'`--' `---' `--'`--''--'.`-  /     `--'  `--' `---'  `---'  `---'           
""")


def start():
    print("\nYour mum sends you on a mission to deliver cookies to Grandma's house")
    print("There are two paths through the forest to Grandma's, which one do you take? (l or r)")
    answer=input(">").lower()

    if "l" in answer:
        bear()
    elif "r" in answer:
        wolf()
    else:
        game_over("Don't you know how to type?")

def bear():
    print("\n There is a bear here.")
    game_over("The bear killed you!")

def wolf():
    print("\nThere is a wolf here")
    print("The wolf asks you where you're going, what do you do?")
    print("1). Tell the truth; that you're going to Grandma's")
    print("2). Lie and tell him you're going to a wolf killing convention")
    answer=input(">")

    if answer=="1":
        safe_passage()
    elif answer=="2":
        game_over("The wolf could smell you were lying and ate you")
    else: 
        game_over("Don't you know how to type?")

def safe_passage():
    print("\nYou are now on a clear path to Grandma's")
    print("You see her house")
    print("What do you do? (1 or 2)")
    print("1). Eat the cookies yourself and go back home")
    print("2). Go to Grandma's house")
    answer=input(">")

    if answer == "1":
        game_over("The cookies had nuts and you're allergic to nuts!")
    elif answer == "2":
        print("\n Nice! You made it to Grandma's house safely! You win the game")
        play_again()
    else:
        game_over("Don't you know how to type?")

def play_again():
    print("\nDo you want to play again? (y or n)")
    answer=input(">").lower()

    if "y" in answer:
        start()
    else:
        exit()

def game_over(reason):
    print("\n"+reason)
    print("Game over!")
    play_again()

start()