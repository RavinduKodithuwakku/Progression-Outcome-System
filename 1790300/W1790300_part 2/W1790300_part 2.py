#part 2

print("Part 2 - Staff Version ")
print()

Progress_count=0
Trailing_count=0
Retriever_count=0
Excluded_count=0
Total_count=0
quit_code=0


Total_count = Total_count + 1
pass_marks=0                     #variables
defer_marks=0
fail_marks=0
marks_range=(0,20,40,60,80,100,120)  #marks should be in this range 


    
def input_marks():             #user define fuction

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
            break

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
           break
        
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
        else:
            break
        
     if pass_marks + defer_marks + fail_marks != 120:   #total marks
        print("Total Incorrect")
        input_marks()

        
def outcome():                 #user define fuction                      
    if  pass_marks==120:                            
         print("Your Progression Outcome: Progress")
         global Progress_count
         Progress_count=Progress_count + 1
    
    elif pass_marks==100:
         print("Your Progression Outcome: Progress-module trailer")
         global Trailing_count
         Trailing_count=Trailing_count + 1
       

    elif fail_marks>=80:
         print("Your Progression Outcome: Exclude")
         global Excluded_count
         Excluded_count=Excluded_count + 1

    else:
         print("Your Progression Outcome: Do not progress-module retriever")
         global Retriever_count
         Retriever_count=Retriever_count + 1



#histogram

def histogram():                                                  #user define fuction
    print("progress :" , Progress_count, "*" * Progress_count )
    print("Trailing :" , Trailing_count,"*" * Trailing_count)
    print("Retriever:" , Retriever_count, "*" * Retriever_count )
    print("Excluded :" ,Excluded_count,  "*" * Excluded_count )
    Total_count = (Progress_count + Trailing_count + Retriever_count + Excluded_count)
    print("Total    :", Total_count )

while quit_code != "q":
    input_marks()
    outcome()

    quit_code=input("If you want to quit the programe press 'q' or press 'enter':  ")
    
histogram()

    
