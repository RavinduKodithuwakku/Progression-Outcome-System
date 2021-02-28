#part 1

print("Part 1 - Student Version ")
print()

pass_marks=0      #variables
defer_marks=0
fail_marks=0
marks_range=(0,20,40,60,80,100,120) #marks should be in this range

def input_marks():        #user define fuction

    #pass_marks

    while True:
        
        try:
            global pass_marks
            pass_marks=int(input("Enter your pass marks: "))        
        except ValueError:
            print("Intreger Required")
            continue
        if (pass_marks) not in marks_range:
            print("Range Error")
        else:
            break;

     #defer_marks

    while True:
       
       try:
           global defer_marks
           defer_marks=int(input("Enter your defer marks: "))        
       except ValueError:
           print("Intreger Required")
           continue
       if (defer_marks) not in marks_range:
           print("Range Error")
       else:
           break;
        
    #fail_marks
    while True:
        try:
            global fail_marks
            fail_marks = int(input("Enter your fail marks: "))        
        except ValueError:
            print("Intreger Required")
            continue
        if (fail_marks) not in marks_range:
            print("Range Error")
            global credit_total
        elif pass_marks + defer_marks + fail_marks != 120:
            print("Total Incorrect")
          
        else:
            break;
        
input_marks()
if  pass_marks==120:
     print("Your Progression Outcome: Progress")                            #progression outcome
    
elif pass_marks==100:
     print("Your Progression Outcome: Progress-module trailer")             #progression outcome

elif fail_marks>=80:
     print("Your Progression Outcome: Exclude")                             #progression outcome

else:
     print("Your Progression Outcome: Do not progress-module retriever")    #progression outcome

