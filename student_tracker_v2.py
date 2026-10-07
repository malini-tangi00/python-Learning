import json
students=[]
def get_valid_roll_no():
    while True:
        try:
            roll_no=int(input("enter a roll no:"))
            duplicate=False
            for student in students:
                if student["roll_no"]==roll_no:
                    duplicate=True
                    break
            if duplicate:
                print("roll no already exists")
            else:
                return roll_no
        except ValueError:
            print("enter number only")
def get_valid_text(field):
    while True:
            value=input(f"enter a {field}:").strip()
            if value!="":
                return value 
            else:
                print(f"{field} cannot be empty.")
def get_valid_marks(subject):
    while True:
        try:
            marks=int(input(f"enter {subject} marks:"))
            if 0<=marks<=100:
                return marks
            else:
                print("invalid marks.enter 0-100.")
        except ValueError:
            print("enter numbers only")
def add_student():
    print("\n=======================================ADD STUDENT=====================================================")
    roll_no=get_valid_roll_no()
    name=get_valid_text("name")
    course= get_valid_text("course")
    python_marks= get_valid_marks("python")
    sql_marks= get_valid_marks("sql")
    dsa_marks= get_valid_marks("dsa")
    student={
        "roll_no":roll_no,
        "name":name,
        "course":course,
        "python":python_marks,
        "sql":sql_marks,
        "dsa":dsa_marks
    }
    students.append(student)
    print("\nstudent added successfully!")
def view_student():
    if len(students)==0:
        print("No students available.")
        return
    print("\n==============================================")
    print("                 ALL STUDENTS                   ")
    print("\n==============================================") 
    for student in students:
        print("============================================")
        print("roll_no:",student["roll_no"])
        print("name   :",student["name"])
        print("course :",student["course"])
        print("python :",student["python"])
        print("sql    :",student["sql"])
        print("dsa    :",student["dsa"])
def search_student():
    print("1.search with roll no")
    print("2.search with name")
    choice= input("enter a choice:")
    if choice=="1":
        while True:
            try:
                roll_no= int(input("enter a roll no:"))
                for student in students:
                    if student["roll_no"]==roll_no:
                        print("=========== STUDENT FOUND============")
                        print("roll_no:",student["roll_no"])
                        print("name   :",student["name"])
                        print("course :",student["course"])
                        print("python :",student["python"])
                        print("sql    :",student["sql"])
                        print("dsa    :",student["dsa"])
                        return
                print("no student found with this roll no.")
            except ValueError:
                print("enter number only")
    elif choice=="2":
        name=input("enter student name:").strip()
        found=False
        for student in students:
            if student["name"].lower()==name.lower():
                print("=============================== STUDENT FOUND======================================")
                print("roll_no:",student["roll_no"])
                print("name   :",student["name"])
                print("course :",student["course"])
                print("python :",student["python"])
                print("sql    :",student["sql"])
                print("dsa    :",student["dsa"])
                found=True
        if not found:
            print("student not found with this name.")    
    else:
        print("invalid choice.")
def update_student():
    roll_no=int(input("enter a roll_no to update:"))
    for student in students:
        if student["roll_no"]==roll_no:
            print("STUDENT FOUND.")
            student["name"]=get_valid_text("new name")
            student["course"]=get_valid_text("course")
            student["python"]=get_valid_marks("new python marks")
            student["sql"]=get_valid_marks("new sql marks")
            student["dsa"]=get_valid_marks("new dsa marks")
            print("student updated successfully")
            return
    print("\n no student found this roll no.")  
def delete_student():
    roll_no=get_valid_marks()
    confirmation=input("do you want to delete this student record (yes/no):")
    if confirmation.lower()=="yes":
        for student in students:
            if student["roll_no"]==roll_no:
                students.remove(student)
                print("student deleted successfully.") 
                return   
    else:
        print("\ndelete cancelled.")
def calculation_total(student):
    return student["python"]+student["sql"]+student["dsa"]
def calculation_percentage(total):
    return (total/300)*100
def calculation_grade(percentage):
    if percentage>=90:
        return "A+"
    elif percentage>=80:
        return "A"
    elif percentage>=70:
        return "B" 
    elif percentage>=60:
        return "C" 
    elif percentage>=50:
        return "D"
    elif percentage>=40:
   
      return "E"
    else:
        return "F" 
def calculation_result(percentage):
    if percentage>=50:
        return "pass"
    else:
        return "fail"       
def performance_report():
    roll_no=int(input("enter a roll no for performance report:"))
    for student in students:
        if student["roll_no"]==roll_no:
            total=calculation_total(student)
            average=total/3
            percentage=calculation_percentage(total)
            marks={
                "python":student["python"],
                "sql":student["sql"],
                "dsa":student["dsa"]
            }
            highest_subject=max(marks,key=marks.get)
            lowest_subject=min(marks,key=marks.get)
            highest_marks=marks[highest_subject]
            lowest_marks=marks[lowest_subject] 
            grade=calculation_grade(percentage)
            result=calculation_result(percentage)
            print("\n=========================================================================") 
            print("                        STUDENT PERFORMANCE REPORTER                       ")  
            print("\n=========================================================================") 
            print("-----------------------------STUDENT DETAILS-----------------------------------")
            print("\nrollno:",student["roll_no"])
            print("name    :",student["name"])
            print("course  :",student["course"]) 
            print("--------------------------------MARKS---------------------------------------------")
            print("\npython:",student["python"])
            print("sql     :",student["sql"])
            print("dsa     :",student["dsa"])
            print("\n-----------------------------PERFORMANCE--------------------------------------")
            print("\ntotal  :",total,"/300")
            print("percentage:",round(percentage,2),"%")
            print("average   :",round(average,2))
            print("highest   :",highest_subject,"-" ,highest_marks)
            print("lowest    :",lowest_subject,"-", lowest_marks)
            print("---------------------------------RESULT-------------------------------------------")
            print("grade     :",grade)
            print("result    :",result)
            return
    print("\nNo student found with this roll_no.")        
def top_3_performers():
    if len(students)==0:
        print("\nNo student available")
        return
    ranked_students=sorted(students,key=lambda student:calculation_total(student),reverse=True)    
    print("\n==============================TOP 3 PERFORMERS======================================")
    for position,student in enumerate(ranked_students[:3],start=1):
        total=calculation_total(student)
        percentage=calculation_percentage(total)
        print(f"\n{position} place")
        print("roll_no    :",student["roll_no"])
        print("name       :",student["name"])
        print("total      :",total)
        print("percentage :",round(percentage,2),"%")
def class_statistics():
    if len(students)==0:
        print("no students available.")
        return
    total_students=len(students)
    passed=0
    failed=0
    total_percentage=0
    for student in students:
        total=calculation_total(student)
        percentage=calculation_percentage(total)
        total_percentage+=percentage
        if percentage>=50:
            passed+=1
        else:
            failed+=1
    class_average=total_percentage/total_students
    highest_student=max(students,key=calculation_total)
    lowest_student=min(students,key=calculation_total)
    print("\n====================================CLASS STASTISTICS====================================")
    print("\ntotal students :",total_students)
    print("passed           :",passed)
    print("failed           :",failed)
    print("class average    :",round(class_average,2),"%") 
    print("\nhighest scorer :",highest_student["name"])
    print("highest_total    :",calculation_total(highest_student))
    print("\nlowest scorer  :",lowest_student["name"])
    print("lowest_total     :",calculation_total(lowest_student))
def save_data():
    with open("students.json","w") as file:
        json.dump(students,file,indent=4)
    print("\n student data saved successfully!")
def load_data():
    global students
    try:
        with open("students.json","r") as file:
            students=json.load(file)
    except FileNotFoundError:
        students=[]
    except json.JSONDecodeError:
        students=[]
        print("\ninvalid json data.starting with empty student data")
def clear_all_data():
    global students
    students.clear()
    with open("students.json","w") as file:
        json.dump(students,file,indent=4)
    print("\n All students data cleared successfully!")
load_data()           
while True:
    print("\n")
    print("=======================================================================================")
    print("                        STUDENT PERFORMANCE TRACKER                                    ")              
    print("=======================================================================================")
    print("1. Add Student")
    print("2.View all students")
    print("3.Search student")
    print("4.Update student")
    print("5.Delete student")
    print("6.Student performance report")
    print("7.Top 3 performers")
    print("8.Class statistics")
    print("9.Save data")
    print("10.Clear all data") 
    print("11.Exit")
    print("=======================================================================================")    
    choice=input("ENTER YOUR CHOICE:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_student()
    elif choice=="3":
        search_student()
    elif choice=="4":
        update_student()
    elif choice=="5":
        delete_student()
    elif choice=="6":
        performance_report()
    elif choice=="7":
        top_3_performers()
    elif choice=="8":
        class_statistics()
    elif choice=="9":
        save_data()
    elif choice=="10":
        clear_all_data()
    elif choice=="11":
        print("\n Thank you for using student performance tracker!")
        break
    else:
        print("\n Invalid choice!")   






