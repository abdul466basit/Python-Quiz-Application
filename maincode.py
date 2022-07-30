
def compliment():          # THIS FUNCTION IS FOR PRINTING COMPLIMENT ACCORDING TO SCORE
    if count >= 8:
        print('That was GREAT!!', name)
    elif count > 5:
        print('NOT BAD!!', name)
    elif count > 3:
        print('Ohh NO,That was not Good!!', name)
    elif count <= 3:
        print('Ohh NO, You need Serious Focus', name)


def maths_question():           # THIS IS A FUNCTION FOR OPENING MATHS QUESTION FILE AND CONVERT THE CONTENT INTO LIST
    with open('maths.txt') as ff:
        for item in ff:
            item = item.strip()
            item = item.split(',')
            maths.append(item)


def cs_question():          # THIS IS A FUNCTION FOR OPENING CS QUESTION FILE AND CONVERT THE CONTENT INTO LIST
    with open('cs.txt') as cc:
        for item in cc:
            item = item.strip()
            item = item.split(',')
            cs.append(item)


def gk_question():            # THIS IS A FUNCTION FOR OPENING GK QUESTION FILE AND CONVERT THE CONTENT INTO LIST
    with open('gk.txt') as gg:
        for item in gg:
            item = item.strip()
            item = item.split(',')
            gk.append(item)


def admin_menu():     # THIS FUNCTION IS TO SHOW ADMIN THE MENU LIST
    print('Select What you want to do')
    print('\t1) View Questions\n\t2) Add Questions\n\t3) Remove a Question')
    print('\t4) Replace a Question\n\t5) RULES/GUIDE\n\t6) Change Password\n\t7) BACK')


def categories():   # THIS FUNCTION PRINT CATEGORIES NAME
    print('\t1) MATHS\n\t2) GENERAL KNOWLEDGE\n\t3) COMPUTER SCIENCE\n')


def taking_question():     # THIS FUNCTION IS TO TAKE INPUT A NEW QUESTION FROM ADMIN
    global Q
    a = input('Enter Question (with Qno): ')
    b = input('Enter Option 1 (with "1)" ): ')
    c = input('Enter Option 2 (with "2)" ): ')
    d = input('Enter Option 3 (with "3)" ): ')
    e = input('Enter Correct Option No.: ')
    Q = [a, b, c, d, e]


def rules():        # THIS FUNCTION PRINTS RULES
    print('''Hello ADMIN
Please read the following RULES carefully !!
1)	Do not Enter wrong option numbers, they are count as wrong.
2)	You can view all Questions of the chosen category.
3)	You can ADD, REMOVE and REPLACE a particular question at a particular place.
4)	For adding and removing a question, please ensure the correct sequence order of the questions.
5)	When writing new Question please follow the below pattern..
 >	New Question should have the correct sequence number, also the options should have the numbering.
 >	Add a space in between (Qno and Question) and (option no and options).
 >	EXAMPLE:
        Write according to this:
    Q:11 what is ........ ?
    1) aaaa 
    2) bbbb
    3) cccc
    1  (correct option)
    ''')


def password_change():      # THIS FUNCTION IS FOR CHANGING PASSWORD
    with open('password.txt', 'w') as f:
        p = input('Enter New Password: ')
        f.write(p)
        print('You have successfully change the Password')


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  MAIN CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

while True:
    print(':::::::::::::::::::::::::::::::::::::')
    print('=============== ***** ===============')
    print('\n\t\t  WELCOME TO\n\t\tTEST YOUR MIND\n')
    print('You Want To Test How Good Your Knowledge Is???\n\tThen Try This!!')
    print('=============== ***** ===============')
    print('Select How You Want To Play The Game:')
    print('\t1) USER\n\t2) ADMIN\n\t3) EXIT')

    #       HERE ASKING FOR IN WHICH SECTION USER WANTS TO GO
    mode = input('Enter Choice Number: ')
    print()

    if mode == '3':   # THIS WILL TERMINATE THE CODE
        break

# !!!!!!!!!!!!!!!!!!!!!!  USER INTERFACE  !!!!!!!!!!!!!!!!!!!!!

    elif mode == '1':
        print('Hi!!')
        name = input('Please Enter Your Name: ')
        while True:
            print('=============== ***** ===============')
            print('\nWELLCOME', name, '\nChoose What Area You Want To Test.')
            print('\t1) MATHS\n\t2) GENERAL KNOWLEDGE\n\t3) COMPUTER SCIENCE\n\t4) BACK')

            #               TAKING INPUT THE CATEGORY IN WHICH HE WANTS TO PLAY
            area = input('Enter Option Number: ')
            print('=============== ***** ===============')
            print()

            # here the condition is checked then function is called which converts the file into
            # list and assigning that list into new variable QUESTIONS

            if area == '1':
                maths = []
                maths_question()
                questions = maths
                print('GREAT You Want To Test Your Maths Skills...\nLets Check How Much You Can Score...\n')

            elif area == '2':
                gk = []
                gk_question()
                questions = gk
                print('GREAT You Want To Check How Good Your General Knowledge is...\nLets Check It...\n')

            elif area == '3':
                cs = []
                cs_question()
                questions = cs
                print('GREAT You Want To Test Your Computer Knowledge...\nLets Check How Much You Can Score...\n')

            elif area == '4':   # THIS WILL GO BACK TO PREVIOUS INTERFACE
                break

            else:
                print('Enter Correct Option Number!!!')
                continue

        # AFTER CHECKING FOR CONDITIONS NOW THIS IS MAIN CODE FOR DISPLAYING QUESTION AND UPDATING SCORE
            aa = input('Press any key to continue: ')
            print()
            count = 0
            for i in range(len(questions)):
                for j in range(len(questions[0]) - 1):
                    print(questions[i][j])

                print()
                ans = input('Enter  Correct Option Number: ')
                if ans == questions[i][4]:   # checking whether answer is correct or wrong
                    print('GREAT!! Correct Answer\n')
                    count += 1
                else:
                    print('Wrong,the Correct option is', questions[i][4], '\n')
            print()
            compliment()
            print('You Scored', count, 'out of', len(questions))

            print('\nPress any Key to Return', end=' ')
            ret = input()
            print('=============== ***** ===============')
            # print()
            continue

# !!!!!!!!!!!!!!!!!!!!!! ADMIN INTERFACE !!!!!!!!!!!!!!!!!!!!!!!!

    elif mode == '2':
        while True:
            print('=============== ***** ===============')
            print('If You Want To Access Administrator Option\nThen Please Login First')
            print('\t1) LOGIN\n\t2) BACK')
            ad_1 = input('Enter Option Number: ')     # TAKING INPUT WHAT HE WANTS TO DO
            print('=============== ***** ===============')

            if ad_1 == '2':    # THIS WILL GO BACK TO PREVIOUS INTERFACE
                break

            elif ad_1 == '1':      # ADMIN ACCESS
                password1 = input('Enter Password for Accessing: ')     # TAKES INPUT THE PASSWORD

                with open('password.txt') as f:
                    p = f.read()
                if password1 != p:
                    print('PLEASE!!! Enter Correct Password\n')
                else:
                    while True:
                        print('LOGIN SUCCESSFUL')
                        print('=============== ***** ===============')
                        print('\tWelcome Admin')
                        admin_menu()     # PRINT THE MENU LIST
                        print()

                        choice = input('Enter Option Number: ')
                        print('=============== ***** ===============')

                        if choice == '7':    # THIS WILL GO BACK TO PREVIOUS INTERFACE
                            break

                        elif choice == '6':   # THIS IS FOR CHANGING PASSWORD
                            password_change()
                            print('\nPress any Key to Return', end=' ')
                            ret = input()
                            print()
                            continue

                        elif choice == '5':
                            rules()
                            print('\nPress any Key to Return', end=' ')
                            ret = input()
                            print()
                            continue

                            #      FOR VIEWING QUESTIONS !!!!!
                        elif choice == '1':
                            categories()
                            v = input('Enter Category Option: ')

                            if v == '1':                   # according to category, it stores file name in a variable
                                file = 'maths.txt'
                            elif v == '2':
                                file = 'gk.txt'
                            elif v == '3':
                                file = 'cs.txt'
                            else:
                                print('PLEASE!!! Enter Correct Option Number')
                                continue

                            print('Here are the Questions!!\n')

                            # it will read the file and print the contents of the file specified
                            with open(file) as f:
                                print(f.read())
                            print('\nPress any Key to Return', end=' ')
                            ret = input()
                            print()
                            continue

                            # FOR ADDING A QUESTION   !!!!
                        elif choice == '2':
                            categories()
                            v = input('Enter Category Option: ')

                            if v == '1':
                                maths = []
                                maths_question()                    # here we are calling the same function which
                                file = 'maths.txt'                  # converts question into list and also storing that
                                questions = maths                   # list into variable QUESTIONS

                            elif v == '2':
                                gk = []
                                gk_question()
                                file = 'gk.txt'
                                questions = gk

                            elif v == '3':
                                cs = []
                                cs_question()
                                file = 'cs.txt'
                                questions = cs

                            else:
                                print('PLEASE!!! Enter Correct Option Number')
                                continue

                            # AFTER CHECKING THE CONDITION THE BELOW CODE EXECUTES
                            n = int(input('Enter where you want to add Question: '))
                            Q = []
                            taking_question()  # this function takes input a new question
                            questions.insert(n-1, Q)    # this will insert question at the specified position

                            with open(file, 'w') as z:   # this is for writing question back to file in the same format
                                for items in questions:
                                    z.write(items[0] + ',' + items[1] + ',' + items[2] + ',' + items[3] + ',' + items[4] + '\n')
                            print('\nPress any Key to Return', end=' ')
                            ret = input()
                            print()
                            continue

                            # FOR REMOVING A QUESTION  !!!!
                        elif choice == '3':
                            categories()
                            v = input('Enter Category Option: ')
                            if v == '1':
                                file = 'maths.txt'
                                maths = []                # here we are calling the same function which
                                maths_question()          # converts question into list and also storing that
                                questions = maths         # list into variable QUESTIONS

                            elif v == '2':
                                file = 'gk.txt'
                                gk = []
                                gk_question()
                                questions = gk

                            elif v == '3':
                                file = 'cs.txt'
                                cs = []
                                cs_question()
                                questions = cs

                            else:
                                print('PLEASE!!! Enter Correct Option Number!!!')
                                continue

                    # here the particular question is removed and rest of question will be written back to the file
                            n = int(input('Enter Question Number You Want to Remove: '))
                            if n <= len(questions):
                                print('The Below Question is Removed')
                                for i in questions[n-1]:
                                    print(i)       # this will print the question to be removed
                                questions.pop(n-1)      # this remove the question

                                with open(file, 'w') as z:
                                    for items in questions:
                                        z.write(
                                            items[0] + ',' + items[1] + ',' + items[2] + ',' + items[3] + ',' + items[4]
                                            + '\n')
                                print('\nPress any Key to Return', end=' ')
                                ret = input()
                                print()
                                continue

                            else:
                                print('No such Question in Question Bank')

                            # FOR REPLACING A QUESTION !!!!
                        elif choice == '4':
                            categories()
                            v = input('Enter Category Option: ')
                            if v == '1':
                                file = 'maths.txt'     # here we are calling the same function which
                                maths = []             # converts question into list and also storing that
                                maths_question()       # list into variable QUESTIONS
                                questions = maths

                            elif v == '2':
                                file = 'gk.txt'
                                gk = []
                                gk_question()
                                questions = gk

                            elif v == '3':
                                file = 'cs.txt'
                                cs = []
                                cs_question()
                                questions = cs

                            else:
                                print('PLEASE!!! Enter Correct Option Number!!!')
                                continue

                            # AFTER CHECKING THE CONDITION THE BELOW CODE EXECUTES
                            n = int(input('Enter Question Number You Want to Replace: '))
                            if n <= len(questions):
                                print('The Below Question is Removed')
                                for i in questions[n-1]:
                                    print(i, end=' ')
                                print()
                                questions.pop(n-1)

                                Q = []
                                taking_question()    # this function takes input a new question
                                questions.insert(n-1, Q)   # this will insert question at the specified position

                                # this is for writing question back to file in the same format
                                with open(file, 'w') as z:
                                    for items in questions:
                                        z.write(
                                            items[0] + ',' + items[1] + ',' + items[2] + ',' + items[3] + ',' + items[4]
                                            + '\n')
                                print('\nPress any Key to Return', end=' ')
                                ret = input()
                                print()
                                continue

                            else:    # if Qno is not found then this will print
                                print('No such Question in Question Bank')

                        # IF OPTION NUMBER IS NOT CORRECT !!!!
                        else:
                            print('PLEASE!!! Enter Correct Option Number!!!')
                            continue

            else:
                print('PLEASE!!! Enter Correct Option Number!!!\n')
                continue
