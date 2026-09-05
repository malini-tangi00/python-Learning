import json
students=[]
def add_student():
    print("\n=======================================ADD STUDENT=====================================================")
    roll_no=int(input("enter a roll no:"))
    name=input("enter a name:")
    course=input("enter a course:")
    python_marks=int(input("enter a python marks:"))
    sql_marks=int(input("enter a sql marks:"))
    dsa_marks=int(input("enter a dsa marks:"))
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
    roll_no=int(input("enter a roll no:"))
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
    print("\n no student found with this roll no")
def update_student():
    roll_no=int(input("enter a roll no to update:"))
    for student in students:
        if student["roll_no"]==roll_no:
            print("STUDENT FOUND.")
            student["name"]=input("enter a new nmae:")
            student["course"]=input("enter a new course:")
            student["python"]=int(input("enter a new python marks:"))
            student["sql"]=int(input("enter a new sql marks:"))
            student["dsa"]=int(input("enter a new dsa marks:"))
            print("student updated successfully")
            return
    print("\n no student found this roll no.")  
def delete_student():
    roll_no=int(input("enter a roll no to delete a student:"))
    for student in students:
        if student["roll_no"]==roll_no:
            students.remove(student)
            print("student deleted successfully.") 
            return       
    print("\n no student found with this roll no")
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
    roll_no=int(input("enter a roll no fornperformance report:"))
    for student in students:
        if student["roll_no"]==roll_no:
            total=calculation_total(student)
            percentage=calculation_percentage(total)
            grade=calculation_grade(percentage)
            result=calculation_result(percentage) 
            print("\n=====================PERFORMANCE REPORTER==========================")    
            print("\nrollno:",student["roll_no"])
            print("name    :",student["name"])
            print("course  :",student["course"]) 
            print("\npython:",student["python"])
            print("sql     :",student["sql"])
            print("dsa     :",student["dsa"])
            print("\ntotal  :",total,"/300")
            print("percentage:",round(percentage,2),"%")
            print("grade     :",grade)
            print("result    :",result)
            return
    print("\n no student found with this roll no")
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
        print("roll no :",student["roll_no"])
        print("name    :",student["name"])
        print("total   :",total)
        print("percentage:",round(percentage,2),"%")
def class_statistics():
    if len(students)==0:
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
    print("\n====================================CLASS STASTISTICS====================================")
    print("\ntotal students:",total_students)
    print("passed           :",passed)
    print("failed           :",failed)
    print("class average    :",round(class_average,2),"%") 
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















