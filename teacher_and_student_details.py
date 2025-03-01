import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

class Person:
    def __init__(self,name,email):
        self.name = name
        self.email = email
class student(Person):
    def __init__(self,name,email,branch):
        super().__init__(name,email)
        self.branch = branch
class teacher(Person):
    def __init__(self,name,email,subject):
        super().__init__(name,email)
        self.subject = subject
class college:
    def __init__(self,cid,name):
        self.name = name
        self.cid = cid
        self.students = []
        self.teachers = []
        
    def add_teachers(self,teacher):
        self.teachers.append(teacher)
        
    def add_students(self,student):
        self.students.append(student)
        
    def display_teachers(self):
        if len(self.teachers) == 0:
            print("No Teachers Present")
        else:
            print("********")
            print("Teacher Details")
            for x in self.teachers:
                print("Name:",x.name)
                print("Email:",x.email)
                print("Subject:",x.subject)
                print("********")
                
    def display_students(self):
        if len(self.students) == 0:
            print("No Students Present")
        else:
            print("student Details:")
            for x in self.students:
                print("Name:",x.name)
                print("Email:",x.email)
                print("Branch:",x.branch)
                print("********")
                
    def display_colleges_details(self):
        print("colleges Details:")
        print("Name:",self.name)
        print("clg_id:",self.cid)
        print("Total students:",len(self.students))
        print("********")

def send_otp(email):
    otp = random.randint(1111,9999)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    username = "sairutwika1408@gmail.com"  
    password = "lkte omxr usrc jmcn"

    from_email = username
    to_email = email
    subject = "OTP Verification"
    body = f"Your OTP for teacher verification is {otp}. \nThank You."

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        server.quit()
        print(f"OTP sent successfully to {email}")
    except Exception as e:
        print("Error sending OTP:", e)

    return otp

def display_teacher_with_otp(colleges):
    clg_id = int(input("Enter College ID: "))
    clg1 = None

    for val in colleges:
        if val.cid == clg_id:
            clg1 = val
            break

    if clg1 is not None:
        email = input("Enter Teacher's Email for Verification: ")
        teacher_found = None

        for teacher in clg1.teachers:
            if teacher.email == email:
                teacher_found = teacher
                break

        if teacher_found:
            otp = send_otp(email)  
            entered_otp = int(input("Enter OTP received on your email: "))

            if entered_otp == otp:
                print("***Entered OTP sucessful..***")
                print("\nTeacher Details:")
                print("Name:", teacher_found.name)
                print("Email:", teacher_found.email)
                print("Subject:", teacher_found.subject)
                print("*******")
            else:
                print("Invalid OTP. Access Denied.\n")
        else:
            print("No teacher found with this email.\n")
    else:
        print("College Does Not Exist.\n")

def display_student_with_otp(colleges):
    """Function to verify OTP before displaying teacher details"""
    std_id = int(input("Enter College ID: "))
    clg1 = None

    for val in colleges:
        if val.cid == std_id:
            clg1 = val
            break

    if clg1 is not None:
        email = input("Enter Student's Email for Verification: ")
        student_found = None

        for student in clg1.students:
            if student.email == email:
                student_found = student
                break

        if student_found:
            otp = send_otp(email)  
            entered_otp = int(input("Enter OTP received on your email: "))

            if entered_otp == otp:
                print("***Entered otp successful..***")
                print("\nStudent Details:")
                print("Name:", student_found.name)
                print("Email:", student_found.email)
                print("Branch:", student_found.branch)
                print("*******")
            else:
                print("Invalid OTP. Access Denied.\n")
        else:
            print("No student found with this email.\n")
    else:
        print("College Does Not Exist.\n")

colleges = []
while True:
    print("choose your Option: ")
    print("1. To Create College")
    print("2. To Add Teacher")
    print("3. To Add Student")
    print("4. To Display Teacher Details")
    print("5. To Display Student Details")
    print("6. To Display College Details")
    print("7. Teacher login to Generate OTP")
    print("8. Student Login to Generate OTP")
    print("9. Exit")
    option = int(input("Enter Your Option: "))
    if option == 1:
        clg_id = int(input("Enter College Id: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                x = True
                break
        if x == True:
            print()
            print(f"College with {clg_id} already Exist, Try again")
            print()
        else:
            clg_name = input("Enter College Name: ")
            colleges.append(college(clg_id,clg_name))
            print()
            print("***College Created Sucessfully***")
            print("Colleges")
            print()
    elif option == 2:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                clg1 = val
                x = True
                break
        if x == True:
            name = input("Enter Teacher Name: ")
            email = input("Enter Teacher Email: ") 
            subject = input("Enter Teacher Subject: ")
            t = teacher(name,email,subject)
            clg1.add_teachers(t)
            print()
            print(f"***Teacher Added Sucessfully to {clg1.name}***")
            print()
        else:
            print()
            print("College Does not Exists")
            print()
    elif option == 3:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                clg1 = val
                x = True
                break
        if x == True:
            name = input("Enter Student Name: ")
            email = input("Enter Student Email: ")
            branch = input("Enter Student Branch: ")
            s = student(name,email,branch)
            clg1.add_students(s)
            print()
            print(f"***Student Added Sucessfully to {clg1.name}***")
            print()
        else:
            print()
            print("College Does not Exists")
            print()
    elif option == 4:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                clg1 = val
                x = True
                break
        if x == True:
            clg1.display_teachers()
        else:
            print()
            print("College Does not Exists")
            print()
    elif option == 5:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                clg1 = val
                x = True
                break
        if x == True:
            clg1.display_students()
        else:
            print()
            print("College Does not Exists")
            print()
    elif option == 6:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                clg1 = val
                x = True
                break
        if x == True:
            clg1.display_colleges_details()
        else:
            print()
            print("College Does not Exists")
            print()
    elif option == 7:
        display_teacher_with_otp(colleges)
    elif option == 8:
        display_student_with_otp(colleges)
    elif option == 9:
        print()
        print("Thank you Visit again")
        print()
    else:
        break



    
