

#hidden game

def hidden_game():



    #hidden mod coming soon to update 2


    print("*****welcome to the hidden game***** ... \n If you are at this stage, congratulations on finishing the game, please read the help :)")
    hidden_game_menu=input("menu ...\n type : play or help ?--->")
    if hidden_game_menu == "help":
        print("In this part\n you have to put together all the sentences\n  that you have obtained in the game to get the main sentence ...\n  Good luck and try to have fun :)")
    elif hidden_game_menu == "play":
        return        

def help_word(wordkey):
    print("-----------------------------------------------------------------------")
    print(f"You must find the word {wordkey} among the given letters at this stage")
    print("and for exit the mode game just type exit :)")
    return input(".......enter.......")

def true_words(data,mylist):
    mylist=[]
    while True:
        data=input("-- You have already found this word --")
        print("--------------------")

        if data in mylist :
            print("---")
            continue
        else:
            mylist.append(data)
            
            break


def passmision(words):
    print("*******************")
    print(f"The stage is over ... The words found in this stage ...{words}... ")
    print("*******************")

                    



#welcome to game Guess the word
print("**********wellcome to Guess the word game*************")

#menu
while(1):
    menu=input("menu...(---Type the desired option---)\n start ... help...exit:")
    
    # code on menu

    if menu == "start":
        print("go to game...")
        break
    # if menu (help commond)
    elif menu == "help":
        print("*****The structure of the game is very similar to the Iranian game (Aq Mirza).In this game. You have three easy modes. There are medium and hard, in the easy case you have 3 steps, in the middle 5 steps and in the hard 10 steps, and next to these options there is a hidden option that you have to open with a secret code \n (At each step, if you need help, just write the word help)... have fun****")
        continue
    # if menu for exit game
    elif menu =="exit":
        print("see you later .. :>")
        exit()
        break



#level1
words_easy_1=[]
word_easy_1= 0
#level2
words_meduim=[]
word_meduim= 0
#level 3
words_hard=[]
word_hard=0




while(2):
    modes=input("select your mode game \n easy ... meduim ... hard ... hidden mode (hm)...guessrd words (type : gw ) :")

    # modes is easy 
    if modes == "easy":
                while (1111):
                    print(f"... E  I  E  F ...  words :{words_easy_1} number word {word_easy_1} ((---help---))")
                    seleasy=input(f"---->")
                
                    if word_easy_1 == 3 :
                        passmision(words_easy_1)
                        break
                    #exit mode game

                    elif seleasy == "exit":
                        print(f"exit the {modes} mode")
                        break
                     
                    #word in list 
                    if seleasy in words_easy_1 :
                        true_words(seleasy,words_easy_1,)
                        continue
                    
                    #word 1
                    elif seleasy == "evil":
                        print("true word :)")
                        word_easy_1 +=1
                        words_easy_1.append(seleasy)
                        continue

                    #word 2
                    elif seleasy == "life":
                        print("true word :)")
                        word_easy_1 +=1
                        words_easy_1.append(seleasy)
                        
                        continue
                    
                    #word 3
                    elif seleasy == "five":
                        print("true word :)")
                        word_easy_1 +=1
                        words_easy_1.append(seleasy)
                        
                        continue

                    #help commond
                    elif seleasy == "help":
                        help_word(3)
                        continue

                    
                    
                    else:
                        print("////The entered word is incorrect////")
                        continue
    elif modes == "meduim" or modes == "medum":
                while (1112):
                    print(f"... M S I T G A E O L R ...  words :{words_meduim} number word {word_meduim} ((---help---))")
                    selmedu=input(f"---->")
                
                    if word_meduim == 5 :
                        passmision(words_meduim)
                        break
                    #exit the mode game

                    elif selmedu == "exit":
                        print(f"exit the {modes} mode")
                        break
                     
                    #word in list 
                    if selmedu in words_meduim :
                        true_words(selmedu,words_meduim)
                        continue
                    
                    #word 1
                    elif selmedu == "setting":
                        print("true word :)")
                        word_meduim +=1
                        words_meduim.append(selmedu)
                        
                        continue

                    #word 2
                    elif selmedu == "tools":
                        print("true word :)")
                        word_meduim +=1
                        words_meduim.append(selmedu)
                        
                        continue
                    
                    #word 3
                    elif selmedu == "messages":
                        print("true word :)")
                        word_meduim +=1
                        words_meduim.append(selmedu)
                        
                        continue

                    #word 4
                    elif selmedu == "email":
                        print("true word :)")
                        word_meduim +=1
                        words_meduim.append(selmedu)
                        
                        continue
                    #word 5
                    elif selmedu == "smart":
                        print("true word :)")
                        word_meduim +=1
                        words_meduim.append(selmedu)
                        
                        continue

                    #help commond
                    elif selmedu == "help":
                        help_word(5)
                        continue

                    
                    
                    else:
                        print("////The entered word is incorrect////")
                        continue
    elif modes=="gw":
        print(f"is Guessed Words is {print(list(words_easy_1+words_meduim+words_hard))}")
        input("enter for go to menu....>")
        continue
    
    elif modes == "hard":
                while (1114):
                    print(f"... L E A R N M O U G \n  W A T F C H X Z K ...  words :{words_hard} number word {word_hard} ((---help---))")
                    selhard=input("---->")
                
                    if word_hard == 10 :
                        passmision(words_hard)
                        break
                    #exit the mode game

                    elif selhard == "exit":
                        print(f"exit the {modes} mode")
                        break
                     
                    #word in list 
                    if selhard in words_hard :
                        true_words(selhard,words_hard)
                        continue
                    
                    #word 1
                    elif selhard == "learn":
                        print("true word :)")
                        word_hard +=1
                        words_hard.append(selhard)
                        
                        continue

                    #word 2
                    elif selhard == "lemon":
                        print("true word :)")
                        word_hard +=1
                        words_hard.append(selhard)
                        
                        continue
                    
                    #word 3
                    elif selhard == "rung":
                        print("true word :)")
                        word_hard +=1
                        words_hard.append(selhard)
                        
                        continue

                    #word 4
                    elif selhard == "waterfall":
                        print("true word :)")
                        word_hard +=1
                        words_hard.append(selhard)
                        
                        continue
                    #word 5
                    elif selhard == "code":
                        print("true word :)")
                        word_hard +=1
                        words_hard.append(selhard)
                        
                        continue
                    
                    #word 6
                    elif selhard == "python":
                        print("true word :)")
                        word_hard +=1
                        words_hard.append(selhard)
                        
                        continue

                    #word 7

                    elif selhard == "linux":
                        print("true word :)")
                        word_hard +=1
                        words_hard.append(selhard)
                        
                        continue

                    #word 8

                    elif selhard == "glue":
                        print("true word :)")
                        word_hard +=1
                        words_hard.append(selhard)
                        
                        continue

                    #word 9

                    elif selhard == "minimize":
                        print("true word :)")
                        word_hard +=1
                        words_hard.append(selhard)
                        
                        continue

                    #word 10

                    elif selhard == "dark":
                        print("true word :)")
                        word_hard +=1
                        words_hard.append(selhard)
                        
                        continue


                    #help commond
                    elif selhard == "help":
                        help_word(10)
                        continue

                    
                    
                    else:
                        print("////The entered word is incorrect////")
                        continue

    elif modes == "exit":

    

        ifexit=input("exit the game ... ?:)")
        if ifexit == "yes":
            input("see you :)")
            break
        elif ifexit == "no":
            print ("ok back to menu ...")
            continue
        else:
            print("just type yes or no ....")
            input("---")
            continue

    elif modes == "hm":
        print("coming soon :)")
        continue