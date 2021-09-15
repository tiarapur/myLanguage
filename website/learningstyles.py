#the python code for the learning style test
a_count = 0
b_count = 0
c_count = 0
d_count = 0

q1_answer = input(" First Quetsion"
                  "\nRemember when you learned how to play a new computer or board game. You learned best by:"
                  "\n a) clues from the diagrams in the instructions " 
                  "\n b) listening to somebody explaining it and asking questions" 
                  "\n c) reading the instructions"
                  "\n d) watching others do it first"
                  "\n")

if q1_answer.lower() == 'a':
        a_count += 1
elif q1_answer.lower() == 'b':
    b_count += 1
elif q1_answer.lower() == 'c':
    c_count += 1
else:
    print("Not a valid answer")

q2_answer = input("\nSecond Quetsion"
                  "\nAfter reading a play you need to do a project. Would you prefer to:"
                  "\n a) draw or sketch something that happened in the play? " 
                  "\n b) read a speech from the play?" 
                  "\n c) write about the play?"
                  "\n d) act out a scene from the play"
                  "\n")

if q1_answer.lower() == 'a':
        a_count += 1
elif q1_answer.lower() == 'b':
    b_count += 1
elif q1_answer.lower() == 'c':
    c_count += 1
else:
    print("Not a valid answer")


q3_answer = input("\nThird Quetsion"
                  "\nYou have to present your ideas to your class. You would:   "
                  "\n a) draw or sketch something that happened in the play? " 
                  "\n b) read a speech from the play?" 
                  "\n c) write about the play?"
                  "\n d) act out a scene from the play"
                  "\n")

if q1_answer.lower() == 'a':
        a_count += 1
elif q1_answer.lower() == 'b':
    b_count += 1
elif q1_answer.lower() == 'c':
    c_count += 1
else:
    print("Not a valid answer")


q4_answer = input("\nFourth Quetsion"
                  "\nYou are about to hook up your parent’s new computer. You would:"
                  "\n a) follow the diagrams that show how it is done" 
                  "\n b) phone, text or email a friend and ask how to do it" 
                  "\n c) read the instructions that came with it"
                  "\n d) unpack the box and start putting the pieces together. "
                  "\n")

if q1_answer.lower() == 'a':
        a_count += 1
elif q1_answer.lower() == 'b':
    b_count += 1
elif q1_answer.lower() == 'c':
    c_count += 1
else:
    print("Not a valid answer")

if a_count > b_count or c_count or d_count:
    print("You are a Visual Learner")
elif b_count > a_count or c_count or d_count:
    print("You are an Auditory Learner")
elif c_count > a_count or b_count or d_count:
    print("You a Reading and Writing Learner")
elif d_count > a_count or b_count or c_count:
    print("You a Kinethic Learner")




