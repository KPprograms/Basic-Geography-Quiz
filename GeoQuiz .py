countries=[]
capitals=[]
option_list=[]
players=[]
player_percentage=[]
leaderboard_names=[]
leaderboard_scores=[]


#Check Definitions:

def check_name_list(user_name):#This definition checks whether the player already exists in the player's list 
    for i in players:
        if user_name==i:
            return ("true")
        else:
            continue
    return("false")


def check_user_name(user_name):#This checks the validity of the user's name 
    if len(user_name)<2:# since this is a casual quiz, so the requirements are not that strict. 
        return ("false")
    elif len(user_name)>11:
        return ("false")
    else:
        return("true")
    


def check_yes_or_no(user_input):#This definition checks that the user has inputted a valid answer
    user_input=user_input.lower()
    valid_characters="yesno"# These are the valid characters 
    if all(char in valid_characters for char in user_input):#this checks if the input given falls within the valid characters 
        if user_input=="yes" or user_input=="y":
            return("yes")
        elif user_input=="no" or user_input=="n":
            return "no"
        else:
            return "false"
    else:
        return "false"  
     
        
def check_integer(user_input):#This definition check if the input is a integer or not.
    if user_input.isalpha():#checks if the input is alphabetical
          return("false")
    elif user_input.isdigit():# This function checks if the input is an integer.
          return ("true")
    else:
         return("false")
     
def check_answer(user_input):# This checks the answer (option) the user has entered for the quiz.      
    if user_input.isalpha():#checks if the input is alphabetical
          return("false")
    elif user_input.isdigit():# This function checks if the input is an integer.
        if int(user_input)<=4 and int(user_input)>=0:
          return ("true")
        else:
            return("false")
    else:
         return("false")


# Import and export functions

def export_scores():#This definition takes the score's from the lists and updates the file
    file=open("player_scores","r")
    for i in file:
        del (i)
    file.close()
    file=open("player_scores","w")
    for i in range (len(players)):
        file.write(players[i])
        file.write("\n")
        file.write(str(player_percentage[(i*3)]))#i*3 is the formula for the index value of player i's score
        file.write("\n")
        file.write(str(player_percentage[(i*3)+1]))
        file.write("\n")
        file.write(str(player_percentage[(i*3)+2])) 
        file.write("\n")
    file.close()
    del players[0:]#this clears the lists so that data is not written twice
    del player_percentage[0:]
    
    
def import_scores():#This definition imports the player scores from the file and adds to the list 
    del players[0:]
    del player_percentage[0:]
    file=open("player_scores","r")
    temp_list=[]
    for i in file:
        temp_list.append(i.strip())
    number=0
    while number<(len(temp_list)):
        players.append(temp_list[number])
        player_percentage.append(float(temp_list[number+1]))
        player_percentage.append(float(temp_list[number+2]))
        player_percentage.append(float(temp_list[number+3]))
        number=number+4# This is because one player takes 4 index spaces, which is the name and the top 3 scores    
    
def export_leaderboard():#this definition updates the leaderboard file with the new leaderboard players and scores 
    import_scores()
    temp_list=[]
    for i in range (len(players)):
        temp_list.append(players[i])
        high_score=((i*3)+2)# This is the index formula for the user's score 
        temp_list.append(player_percentage[high_score])
        file=open("leaderboard","w")
    for i in temp_list:
        file.write(str(i))
        file.write("\n")
    file.close()
        

def import_leaderboard():
    del leaderboard_names[0:]
    del leaderboard_scores[0:]
    file=open("leaderboard","r")
    number=0
    for l in file:
        if number%2==0:
            leaderboard_names.append(l.strip())
        else:
            leaderboard_scores.append(l.strip())
        number=number+1
    file.close()

def get_scores():#This definition gets the top 3 scores of the player 
    temp_list=[]
    score_number=0
    for i in range (len(players)):
        if players[i]==current_user:
            temp_list.append(player_percentage[i*3])#These are the top 3 scores
            temp_list.append(player_percentage[(i*3)+1])
            temp_list.append(player_percentage[(i*3)+2])
        else:
            continue
    print(current_user,",your top 3 previous scores are:")
    for i in temp_list:
        print("\t",i,"%")
    print("Try beaing your highscore! Good Luck")

def print_leaderboard():#This definition outputs the leaderboard to the users 
    import_leaderboard()#This is to import all the names for before printing, so that the most updated leaderboard is printed to the users. 
    temp_list_1=[]
    temp_list_2=[]
    for i in range (len(leaderboard_names)):
        temp_list_1.append(leaderboard_names[i])
        temp_list_2.append(leaderboard_scores[i])
    del leaderboard_names[0:]
    temp_list_2.sort(reverse=True)
    number=0
    for i in range(len(temp_list_2)):#This is to align the highscore and name to print the leaderboard in decending order. 
        for j in range (len(temp_list_2)):
            if temp_list_2[i]==leaderboard_scores[j]:
                leaderboard_names.append(temp_list_1[j])
            else:
                continue
    del leaderboard_scores[0:]
    for i in temp_list_2:
        leaderboard_scores.append(i)
    number=1 
    print(" LEADER BOARD: ")
    for i in range (len(leaderboard_scores)):
        print(number, leaderboard_names[i],"\t", leaderboard_scores[i],"%")
        number=number+1
    

def import_data():# This imports the data, which is the countries and capitals from the data list.       
    file=open("level_1","r")
    n=-1
    for l in file:
        n=n+1
        if n%2==0:#This is because all the even line numbers are countries and the odd line numbers are capitals. 
            countries.append(l.strip())
        else:
            capitals.append(l.strip())
    file.close()
    


def title_page():# this is the starting page of the whole quiz
    print("\t \t \t GEOGRAPHY QUIZ")
    print("please enter your option")
    print("1. PLAY GAME ")
    print("2. VIEW LEADER BOARD")
    user_input=input("option: ")
    if check_integer(user_input)=="true":
        user_input=int(user_input)
        if user_input==1:
            home()
        elif user_input==2:
            print_leaderboard()
        else:
            print("Invalid input- out of range")
            title_page()
    else:
        print("Invalid input")
        print("Please input an integer")
        title_page()
    
    
    
def home():#This definition is the home page of the quiz program
    print("Please enter your name below")
    user_name=input("Name: ")
    if check_user_name(user_name)=="false":#This checks the user name entered by the user through the check user name function. 
        print("Invalid user name, user_name should be within 3-10 characters")
        home()  
    else:
        if check_name_list(user_name)=="true":#This checks the name list if this user has been entered before. 
            print("looks like you have played this game already? Do you want to overwrite your scores?")
            status="true"
            while status=="true":
                user_choice=input("yes(Y) or no(N)?")
                if check_yes_or_no(user_choice)=="yes":
                    global current_user
                    current_user=(user_name)                    
                    get_scores()
                    global score
                    score=0                    
                    No_of_Questions()   
                elif check_yes_or_no(user_choice)=="no":
                    print("Please enter a new user name")
                    print("Note: you can use symbols and numbers")
                    home()
                else:
                    print("Invalid input")
        else:
            current_user=(user_name)
            players.append(user_name)
            for i in range (3):
                player_percentage.append(0)#this appends 0 to the 3 scores for a new player in order to save 3 index values for each user. 
            export_scores()
            export_leaderboard()
            score=0
            No_of_Questions()
            
                        

def No_of_Questions():#This asks the user the number of questions they want to play 
    global current_user
    print(current_user, "How many questions would you like to play")
    print("\t 5 Questions")
    print("\t 10 Questions")
    print("\t 15 Questions")
    print("\t 20 Questions")
    number_of_Q=input("Please enter your option: ")
    if check_integer(number_of_Q)=="true":
        number_of_Q=int(number_of_Q)
        if number_of_Q==5 or number_of_Q==10 or number_of_Q==15 or number_of_Q==20:
            print("STARTING NEW GAME...")
            level_1_question(number_of_Q)
        else:
            print(current_user, "please enter a valid question number")
            No_of_Questions()      
    else:
        print(current_user, "please enter a valid question number")
        No_of_Questions()


def level_1_question(no_of_questions):#This outputs all the questions 
    import_data()
    q_number=0
    while q_number<no_of_questions:# This loops for the number of questions the user wants to play 
        q_number=q_number+1
        print("Question number:",q_number)
        question=random_question()
        print_question(question)# calls the print question definition which outputs the questions and the options. 
    print("Great! thanks for playing")
    global score
    print(current_user,"you got",score,"out of",no_of_questions)#Outputs the user score and percentage 
    percentage=((score/no_of_questions)*100)
    print("This is",percentage,"%")
    append_score(percentage)
    status="true"
    while status=="true":# This is a forever loop, so it will work forever, until user has inputted a valid input 
        user_choice=input("Would you like to play again? yes (Y) or no (N)?")      
        if check_yes_or_no(user_choice)=="yes":
            get_scores()
            score=0
            No_of_Questions()   
        elif check_yes_or_no(user_choice)=="no":
            print("Thanks for playing")
            print_leaderboard()
        else:
            print("Invalid input")


def append_score(percentage):#This definition appends the percentage score of the user which is a global variable and the  percentage given 
    import_scores()
    temp_list=[]
    for i in range (len(players)):
        if players[i]==current_user:
            score_number=(i*3)#This is the idex formula 
            temp_list.append(player_percentage[(i*3)])
            temp_list.append(player_percentage[(i*3)+1])
            temp_list.append(player_percentage[(i*3)+2])
        else:
            continue
    temp_list.sort()
    if percentage>temp_list[0]:#This checks if the recent score is larger than  the lowest of the top 3 scores 
        del temp_list[0]
        temp_list.append(percentage)#It will append the recent score if it is higher than the lowest of the two scores. 
        temp_list.sort()
        del player_percentage[score_number:score_number+3]
        for i in range (len(temp_list)):
            player_percentage.append(temp_list[i])     
        print("congratualtions! You beat one of your top 3 scores")
    else:
        print("")
    export_scores()#This then updates the files 
    export_leaderboard()
    

def random_question():#This definition generates a random question 
    import random
    del option_list[0:]# This is to clear the option list so that options are not overwriiten 
    random_number=random.randint(0,(len(countries))-1)
    answer=(capitals[random_number])
    for i in range (0,3):
        random_option=random.randint(0,(len(countries))-1)
        if random_option==random_number:#This checks if the option is the answer to the question, in order to avoid printing the answer twice 
            option_list.append(capitals[random_option-2])# if its the same option it choses the the capital city below the answer. 
        else:
            option_list.append(capitals[random_option])
    global answer_number
    answer_number=random.randint(1,4)
    option_list.insert(answer_number-1,answer)
    return(random_number)# this returns the random question 
    
      

def print_question(country_no):#This definition takes the random question generated by the definition above and prints the question for the user. 
    global score
    import random
    print("press 0 to quit")# This allows the user to quit 
    print("what is the capital city of",countries[country_no])
    answer=(capitals[country_no])
    option_number=1
    for i in option_list:
        print("\t",option_number, i)
        option_number=option_number+1    
    user_answer=input("\tAnswer: ")
    if check_answer(user_answer)=="true":
        user_answer=int(user_answer)
        if user_answer==0:
            status="true"
            while status=="true":
                user_choice=input(" Are you sure you want to quit? yes(Y) or No(N)?")
                if check_yes_or_no(user_choice)=="yes":
                    title_page()
                    break# This breaks if the value is valid 
                elif check_yes_or_no(user_choice)=="no":
                    print_question(country_no)
                    break
                else:
                    print("Invalid input- type either y or n")#The program goes on forever until the user inputs a valid input 
        elif user_answer==answer_number:
            print ("Correct! :)")
            del countries[country_no:country_no+1]
            del capitals[country_no:country_no+1]
            score=score+1
        else:
             print("Incorrect :(")
             print("The correct answer is",answer_number, answer)
             del countries[country_no:country_no+1]
             del capitals[country_no:country_no+1]
    else:
        print("Invalid Input, please answer the Question again")
        print_question(country_no)




title_page()

