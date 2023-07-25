class MultiFunction():
     def oddEven():
        num=int(input("Enter the number:"))
        if((num%2)==0):
            print("even number")
            message="even number"
        else:
            print("odd number")
            message="odd number"
        return message
     def BMI():
        index=int(input("Enter the BMI index:"))
        if(index<18):
            print("underweight")
            message1="underweight"
        elif(index>18 and index<25):
            print("normai")
            message1="normai"
        elif(index>25 and index<30):
            print("overweight")
            message1="overweight"
        else:
            print("very overweight")
            message1="very overweight"
        return message1
     def AgeCategory():
        age=int(input("Enter the age:"))
        if(age<18):
            print("children")
            cate="children"
        elif(age<35):
            print("adult")
            cate="adult"   
        elif(age<59):
            print("citizen")
            cate="citizen"   
        else:
            print("senior citizen")
            cate="senior citizen"
        return cate 