""" Fill in The Blanks Quiz.
There are three level in this game. User will be asked in a quiz
from each diffuculty level. The User should have to fill in the blank.
The uppercase or lowercase can be insert while user answering the quiz.
"""

quizes = {'easy':
"""This is a quiz developed by ___1___ programming language.
Python is a widely used ___2___-level, general-purpose, interpreted,
dynamic programming language. Python was conceived in the late 1980s,
and its implementation began in December ___3___ by Guido ___4___ Rossum.""",
          
        'medium':
"""The ___1___ is the program that manages the hardware of the ___2___
system, including the CPU, memory,___3___ devices, and input/output
devices.The type of ___4___ system software you use depends on your
computers ___5___.""",
          
        'hard':
"""The ___1___ are the fastest and most expensive computers.Supercomputers
were introduced in the ___2___s. Traditionally, supercomputers have been
used for ___3___ and ___4___ applications that must handle very large
___5___ or do a great amount of computation (or both)."""}

answers = {'easy': [['python'],
                    ['high'],
                    ['1989'],
                    ['van']],
            'medium': [['operating system'],
                    ['computer'],
                    ['storage'],
                    ['operating'],
                    ['platform']],
            'hard': [['supercomputer'],
                    ['1960'],
                    ['scientific'],
                    ['engineering'],
                    ['databases']]}


def play():
    """
    NOTE :
    To understand the logic must see
    quiz = number of question , loop_quiz = number of answers in list + 1
    Eg: Assume that 4 question will be asked in this game. 4 questions should have 4 answers in list.
    Then question start from 1 which means quiz = 1, and loop_quiz = len(answers[level]) is 4 "I PUT +1, TO MAKE SURE THE GAME LOOP WELL and this is the way i simplify the code.)
    So : while 1 < 5:
              question()
              quiz += 1
    It Will Successful Loop 4 times with 4 question. Every time loop will +1, which means question 1 to question 2 and the answer list also direct to question 2 answer.

    This is the Main function to run the game
    """
    global quiz, quiz_question
    level()
    # Start with 1st question
    quiz = 1
    quiz_question = None
    # number of answers in list + 1
    loop_quiz = len(answers[game_level]) + 1
    # Loop from different question
    while quiz < loop_quiz: 
        question()
        quiz += 1

def level():
    """
    Difficulty level selection
    """
    global game_level
    print "Welcome to Programming and Computer Quiz Game."
    # Select Game Level
    levels= raw_input("Please enter a level 'easy', 'medium', 'hard': ")  
    # To fix upper/lower string error enter when Select Game Level
    game_level = levels.lower()
    # .lower() function to fixed upper/lower string error
    while game_level.lower() not in quizes:  
        game_level = raw_input("Please enter 'easy', 'medium', 'hard': ")
    print "Welcome to " + game_level + " game."


def question():
    """
    To display the question from first question to last question
    """
    global yourans, answers,ans
    # Point to the direct answers in list
    ans = quiz - 1 
    print "Question %s" % quiz 
    print "=" * 11
    # Print filled quiz function if filled
    if quiz_question == None:
        print quizes[game_level] +"\n"
    else:
        print quiz_question
    print "What goes in ___%s___ ?" % quiz
    answer = answers[game_level][ans]
    yourans = raw_input("Your answer: ")
    # While wrong answer, and repeated then use while loop
    while yourans.lower() not in answer: 
        print "\nIncorrect answer, try again..."
        yourans = raw_input("Your new answer: ")
    # Check answer if correct
    if yourans.lower() in answer :
        print "Correct!"
    after_filled()


def after_filled():
    """
    To replace the blank list that you successful filled 
    """
    global quiz_question
    if quiz_question == None:
        quiz_question = quizes[game_level]
    quiz_question = quiz_question.replace('___%s___' % str(quiz), yourans)
    print '-' *80
    print quiz_question
    print '-' *80 + "\n\n"

"""          
Start and Play The game
"""
play()
print "Thanks for playing"
print "This game is developed by Jorcus.com"
