#Student Manager app
Student = {}
#loop
while True:
    print("=====Wellcome To Student Manager=====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter Your Choice = ")

    #Add Student
    if choice == "1":
        name = input("Enter Student Name = ")
        marks = float(input("Enter Student Marks = "))
        Student[name] = marks
        print(f"{name} Susscsfully Added...")

    #View Student
    elif choice == "2":
        if not Student:
            print("No Student Found!")
        else:
            for name,marks in Student.items():
                print(name," ",marks)

    #Check Result
    elif choice == "3":
        name = input("Enter Student Name = ")      

        if name in Student:
            marks = Student[name]
            if marks >= 90:
                print("Pass with Grade A+ =",marks)
            elif marks >= 80:
                print("Pass with Grade A =",marks)
            elif marks >= 70:
                print("Pass with Grade B =",marks)
            elif marks >= 60:
                print("Pass with Grade C =",marks)
            elif marks >= 50:
                print("Pass with Grade D =",marks)
            elif marks >= 40:
                print("Pass =",marks)
            else:
                print("Fail =",marks)
        else:
            print("No Student Found")

    #Exit 
    elif choice == "4":
        print("Exiting....")  
        break

    else:
        print("Invalid Input")       
