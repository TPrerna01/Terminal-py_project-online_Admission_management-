from query import ExeQueries
from validation import validation
from terminaltables import AsciiTable
from datetime import datetime
from payment import Payment

# from dbconnect import Database_connection as db_connection

class MainMenu:
    def __init__(self):
        self.validator = validation()
        self.query_handler = ExeQueries()
        self.pay = Payment()
        # self.db_connection = Database_connection()

    def admin_data(self):
        '''' Main Admin Bydefault '''
        self.email = "admin@yahoo.com"
        self.pswd = "adminworld" 
        return self.email, self.pswd

    def display_menu(self):
        '''Home Page Menu'''
        print("Welcome to College Admission Management System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

    def run(self):
        '''Responsible func for running Home page menu'''
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.register_user()
            elif choice == '2':
                user = self.login_user()
                if user:
                    self.user_actions_menu()
            elif choice == '3':
                print("Exiting program")
                break
            else:
                print("Invalid choice. Please try again.")

    def register_user(self):
        ''' Registeration function'''
        while True:
            ''''user registeration'''
            user_type = input("Account for 1.Admin & 2.User : ")
            if user_type == '1':
                pass
                # self.query_handler.alter_data('user', data = {'is_admin' : 1})
            elif user_type == '2':
                pass
                # self.query_handler.alter_data('user', data = {'is_admin' : 0})
            else:
                print("\n Invalid input\n")
            print("********* Courage Education *********************")
            name = input("Enter your name: ")
            ph_no = input("Enter your phone number: ")
            email = input("Enter your email: ")
            password = input("Enter your password(atleast 8 char): ")
            dob = input("Enter your date of birth (YYYY-MM-DD): ")
            gender = input("Enter your gender (1. Male ,2. Female ,3. Other): ")
            if gender == '1' or gender == 'm' or gender == 'M' or gender == 'male' or gender == "Male":
                    gender = f"Male"
            elif gender == '2' or gender == 'f' or gender == 'F' or gender == 'female' or gender == "Female":
                    gender = f"Female"
            else :
                    gender = f"Other"

            user_table_data = [name, ph_no, email, password, dob, gender]
            if all(user_table_data) :
                for item in user_table_data:
                    print(f" { item }")
                user_confirm = input(" To store data [y/n]: ")
                if user_confirm == 'y' or user_confirm == 'Y':
                    error_check = self.validator.register(name,ph_no,email,password,dob)
                    if error_check:
                        for errors in error_check:
                            print(errors)
                    else: 
                        if user_type == '1':
                            admin = 1
                            user_data = { 'name' : name, 'email' : email, 'password' : password, 'ph_no' : ph_no, 'gender' : gender, 'dob' : dob , 'is_admin' : admin}
                        else :
                            user_data = { 'name' : name, 'email' : email, 'password' : password, 'ph_no' : ph_no, 'gender' : gender, 'dob' : dob}
                        # breakpoint()
                        self.query_handler.insert_data('user', user_data)  
                        print("\nRegistration Successful\n ") 
                        break 
                elif user_confirm == 'n' or user_confirm == 'N':
                    break
            else:
                print("\nPlease fill in all the fields.\n")
            
    def login_user(self):
        '''Login Function'''    
        while True:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            condition = f"email='{email}' and password='{password}'"
            admin_condition = f"{condition} and is_admin='{1}'"
            ad_data = self.admin_data()
            
            admin = self.query_handler.select_data('user', condition=admin_condition)
            if email == ad_data[0] and password == ad_data[1] or admin:
                print("Admin : Login successfully")
                return self.admin_dashboard()
            
            user = self.query_handler.select_data('user', condition=condition)
            if user :
                global login_data
                login_data = user[0]
                print("\nUser : Login success fully\n")
                return True
                break
            else:
                print("\nInvalid email or password. Please try again.\n")
                return False
            
    def foreign_key(self):
        '''save the foreign key data'''
        return login_data[0]

    def admin_dashboard(self):
        '''Admin Dashboard locator'''
        print("ADMIN DASH BOARD")
        self.admin_home()

    def user_actions_menu(self): 
        ''' User Dashboard locator'''
        print("i m user home page")
        self.home()

#  **************************************User home data *************************************
    def home(self):
        '''User home page menu'''
        user_menu_info = '''
        ***************************
        |    Courage Education    |
        ***************************
        | ==> 1 . Courses         |
        |                         |
        | ==> 2.  Admission(data) |
        |                         |
        | ==> 3.  Feedback        |
        |                         |
        | ==> 4.  Blogs           |
        |                         |
        | ==> 5.  About           |
        |                         |
        | ==> 6.  Logout          |
        ***************************
        '''
        # print(f"{user_menu_info}")

        while True:
            print(f"{user_menu_info}")
            user_input = input("Enter the choice :")
            match(user_input):
                case '1':
                    self.show_course_details()
            
                case '2':
                    user_input = input(' enter 1 for admission form \n 2 for admission status : ')
                    if user_input == '1':
                        self.admission_form()
                    elif user_input == '2':
                        self.user_status_data()
                    else:
                        print('Invalid data')
    
                case '3':
                    self.feedback()

                case '4':
                    self.show_blog()

                case '5':
                    self.about()

                case '6':
                    break
                case _ :
                    print("Invalid Input")

#  ****************************************** Admin Home Data **********************************
    def admin_home(self):
        ''' Admin Home Page menu'''
        admin_menu_info = '''
        **************************************
        |          C-E Admin_Panel           |
        **************************************
        | ==> 1 . Courses(add_update)        |
        |                                    |
        | ==> 2.  Admission(data)            |
        |                                    |
        | ==> 3.  Feedback (view)            |
        |                                    |
        | ==> 4.  Blog(data)                 |
        |                                    |
        | ==> 5.  Logout                     |
        **************************************
        '''
        # print(f"{admin_menu_info}")

        while True:
            print(f"{admin_menu_info}")
            admin_input = input("Enter the choice :")
            match(admin_input):
                case '1':
                    admin_input = input(" select option :\n 1. Add new course \n 2. checking the course data \n 3. updating the existing record \n 4. deleting the record:")
                    if admin_input == '1':
                        self.course()
                    elif admin_input == '2':
                        self.show_course_details()
                    elif admin_input == '3':
                        self.update_course()
                    elif admin_input == '4':
                        self.delete_course()
                    else:
                        print("Invalid Input")
                    
                
                case '2':
                    admin_input = input(" 1. Admission record check \n 2. checking the payment and accepting the admission:")
                    if admin_input == '1':
                        self.show_admission_details()
                    elif admin_input == '2':
                        self.admission_status_change()
                    else:
                        print("Invalid Input")

                case '3':
                    self.show_feedback()

                case '4':
                    self.blog()
                
                case '5':
                    break

                case _ :
                    print("Invalid Input")

# ***************************************course table function*****************************
    def course(self):
        '''course data form for inertion method'''
        while True :
            course_name = input("Enter course name: ")
            print(f"Enter course desc [stop = '//']: ")
            course_description = " "
            while True:
                user_desc = input()
                if user_desc == '//':
                    break
                course_description += user_desc + " "

            department = input("Enter department name: ")
            online_availability = input("Enter online available(0 : offline ,1 : online): ")
            print(f"Enter requriment for admission [stop = '//']: ")
            admission_requirements = " "
            while True:
                user_desc = input()
                if user_desc == '//':
                    break
                admission_requirements += user_desc + " "

            course_duration = input("Enter course duration: ")
            course_price = input("Enter the course price : ")

            if course_name and course_description and department and online_availability and admission_requirements and course_duration and course_price:
                error_check = self.validator.course_valid(course_name, online_availability, course_duration)
                if error_check:
                    for errors in error_check:
                        print(errors)
                else:
                    course_data = { 'course_name' : course_name, 'course_description' : course_description, 'department' : department, 'online_availability' : online_availability, 'admission_requirements' :admission_requirements, 'course_duration' : course_duration , 'course_price' : course_price }
                    self.query_handler.insert_data('course', course_data)   
                    break 
            else:
                print("All the field must be filled correctly")
    

    def show_course_details(self):
        '''show course details'''
        data = self.query_handler.select_data('course',columns=['course_name','course_description', 'department', 'online_availability'])
        data2 = self.query_handler.select_data('course', columns=['course_name','admission_requirements', 'course_duration', 'course_price'])
        table_data = [[ 'course_name','course_description', 'department', 'online_availability']] 
        table_data2 = [['course_name','admission_requirements', 'course_duration', 'course_price']]
        table_data.extend(data) 
        table_data2.extend(data2)
        
        table2 = AsciiTable(table_data2)
        table = AsciiTable(table_data)
        print(f"{table.table}\n{table2.table}")

    def update_course(self):
        '''course data update method'''
        print("update_course functionn")
        data = self.query_handler.select_data('course', columns=['course_name'])
        for index,item in enumerate(data,start=1):
            print(f"{index} => {item}")
        course_selection = input("enter course id for update :")
        conditions = f"course_id='{course_selection}'"
        data3 = {'course_id' :course_selection}
        # course_items = self.queryhandler.select_data('course',condition=conditions)
        # if course_items :
        #     for index,item in enumerate(course_items, start=1):
        #         print(f"{index} ==> {item}")
        course_data = self.query_handler.select_data('course',columns=['course_id','course_name','course_description', 'department', 'online_availability'],condition=conditions)
        course_data2 = self.query_handler.select_data('course', columns=['course_name','admission_requirements', 'course_duration', 'course_price'],condition=conditions)
        final_data = self.query_handler.select_data('course',condition=conditions)
        if final_data:
            table_data = [[' course_id', 'course_name','course_description', 'department', 'online_availability']] 
            table_data2 = [['course_name','admission_requirements', 'course_duration', 'course_price']]
            table_data.extend(course_data) 
            table_data2.extend(course_data2)
            table2 = AsciiTable(table_data2)
            table = AsciiTable(table_data)
            print(f"{table.table}\n{table2.table}")
            column_name = input("enter column name for changeing :")
            value = input("enter data for changeing :")
            column = column_name.lower()
            if column in table_data[0] or column in table_data2[0]:
                change_data = {column : value}
                self.query_handler.update_data('course',data=change_data, condition=data3)
                print("changed data successfully")
            else:
                print("some issue occur while changing")
        else:
            print("no such column exits")

    def delete_course(self):
        '''delete data from course tale fuction'''
        print("delete_course_function")
        course_update_data = self.query_handler.select_data('course',columns=['course_id','course_name'])
        table_data = [['course_id','couser_name']] 
        table_data.extend(course_update_data) 
        table = AsciiTable(table_data)
        print(table.table)
        
        while True :
            del_condition = input("enter the data for removing form list :")
            if del_condition == "":
                print("empty data can empty the table:")
                data = input(f"want to delete all data from table [y/n] : ")
                if data == 'y' or data == 'Y':
                    self.query_handler.delete_data('course')
                elif data == 'n' or data == 'N':
                    print("data will not be delete form table")
                    break
            
                    
            else:
                self.query_handler.delete_data('course', condition= {'course_id' : del_condition})
                print("data deleted successfully")
                break           
        
# ********************************************* admission data****************************************
    def admission_form(self):
        ''''admission form'''
        cs_id = ['course_name']
        # us_id = 'user_id'
        # user_id = self.query_handler.get_last_user_id('user',column = us_id)
        select_course_id = self.query_handler.select_data('course', columns = cs_id)
        user_id = self.foreign_key()

        while True:
            print(f" Fill the Admission Form Details .")
            course_type = input("Admission want in [ 1.online , 0.offline ] : ")
            if course_type == '1':
                course_type = 'online'
            elif course_type == '0':
                course_type = 'offline'

            cdata = self.query_handler.select_data('course', columns=['course_id', 'course_name'])
            table_data = [[ 'course_id', 'course_name']] 
            table_data.extend(cdata) 
            table = AsciiTable(table_data)
            print(table.table)
        
            # # course_lst = [value for i,value in enumerate(select_course_id,start=1)]
            course_id = input("\nenter the selected course no.:")
            admission_date = input("enter the admission date [yyyy-mm-dd] : ")
            per_institute = input("enter previous institute/school name : ")
            per_course = input("enter the already achieving degree name : ")
            per_grade = input("enter the grades/cgpa : ")

            # course_data = self.query_handler.select_data('course', columns=['course_id', 'course_name'])
            # user_data = self.query_handler.select_data('user', columns=['user_id', 'user_name'])


            if course_type and admission_date and per_institute and per_course and per_grade :
                if self.validator.admission_valid(admission_date):
                    # course_name = next((course['course_name'] for course in course_data if course['course_id'] == course_id), None)
                    # user_name = next((user['user_name'] for user in user_data if user['user_id'] == user_id), None)
                    # admission_data = {'user_name' : user_name, 'course_name' : course_name, 'course_type': course_type, 'admission_date': admission_date, 'per_institute': per_institute, 'per_course' : per_course, 'per_grade' : per_grade}
                    admission_data = {'user_id' : user_id, 'course_id' : course_id, 'course_type': course_type, 'admission_date': admission_date, 'per_institute': per_institute, 'per_course' : per_course, 'per_grade' : per_grade}
                    try:
                        # user_id = self.query_handler.select_data('user')
                        self.query_handler.insert_data('admission', admission_data)
                        print("\nAdmission details fill successfully\n")
                        return self.pay.payment()
                    except Exception as e:
                        print(f"\nError occurred while inserting admission details: {e}\n")

            else:
                print("\nAll the fields must be filled correctly\n")
    
    def user_status_data(self):
        '''show user its admission status'''
        user_data = self.foreign_key()
        conditions = f"user_id='{user_data}'"
        while True:
            user_id_fetch = self.query_handler.select_data('admission',columns=[ 'user_id', 'course_type', 'admission_date','status'],condition= conditions)
            if user_id_fetch:
                table_data = [[ 'user_id', 'course_type', 'admission_date','status']] 
                table_data.extend(user_id_fetch) 
                table = AsciiTable(table_data)
                print(table.table)
                break
            else:
                print("no such data")
                break
    

#   admin side panel function
    def show_admission_details(self):
        '''display the admission table to admin side '''
        admission_final_data = self.query_handler.select_data('admission')
        table_data = [[ 'admission_id', 'user_id', 'course_id', 'course_type', 'admission_date', 'per_institute', 'per_course' , 'per_grade' ,'status']] 
        table_data.extend(admission_final_data) 
        table = AsciiTable(table_data)
        print(table.table)
       

#  admin side panel function
    # def change_admission_data(self):
    #     '''automatically make changes on the admission status field'''
    #     payment_check = ["admission_id"]
    #     admission_check = ["admission_id"]
    #     # get the admission records id for comparission
    #     payment_record = self.query_handler.select_data('payment',columns = payment_check )
    #     admission_record = self.query_handler.select_data('admission', columns = admission_check)
        
    #     for adrecord in admission_record:
    #         record_ad,status = adrecord
    #         for pyrecord in payment_record:
    #             if record_ad == pyrecord[0]:
    #                 self.query_handler.update_data('admission', data={'status': 'Accepted'}, condition={'admission_id' : record_ad})
    #                 break 
    #             else :
    #                 self.query_handler.update_data('admission', data={'status':'Declined'}, condition={'admission_id' : record_ad})
    
    #     print("after updation admissionn table")
    #     admission_table_data = self.query_handler.select_data('admission', columns=['admission_id', 'status'])
    #     table_data = [[ 'admission_id','status']] 
    #     table_data.extend(admission_table_data) 
    #     table = AsciiTable(table_data)
    #     print(table.table)


    def admission_status_change(self):
        ''''admission status sheck and change by admin'''''

        payment_check = ['admission_id']
        payment_record = self.query_handler.select_data('payment',columns = payment_check )
        print("admission_id and status")
        #  to print particular admission_id information
        while True :
            admission_data = 'admission'
            user_data = 'user'
            course_data = 'course'
            result = self.query_handler.join_data(table1=admission_data, table2=user_data, table3=course_data)
            table_data = [[ 'admission_id', 'username', 'course_name' ,'status']] 
            table_data.extend(result) 
            table = AsciiTable(table_data)
            print(table.table)
            # admission_id_data = self.query_handler.join_data()
            # for index,item in enumerate(admission_id_data,start=1):
            #     print(f"{index} => {item}")
            ad_id = input("enter user_id for view data : ")
            conditions = f"admission_id='{ad_id}'"
            admission_detail = self.query_handler.select_data('admission', condition=conditions)
            table_data = [[ 'admission_id', 'user_id', 'course_id', 'course_type', 'admission_date', 'per_institute', 'per_course' , 'per_grade' ,'status']] 
            table_data.extend(admission_detail) 
            table = AsciiTable(table_data)
            print(table.table)
            #  condition for update that particular user or leave
            admin_input = input("enter want to update status [y/n] : ")
            if admin_input == 'y' or admin_input == 'Y':
                data3 = {'admission_id' : ad_id}
                for pyrecord in payment_record:    
                    if ad_id in pyrecord:
                        self.query_handler.update_data('admission', data={'status': 'Accepted'}, condition=data3 )
                        break
                    else :
                        print("Payment = NULL status declined")
                        self.query_handler.update_data('admission', data={'status':'Declined'}, condition=data3)
                        break
    
            elif admin_input == 'n' or admin_input == 'N':
                    print("status will remain same")
                    break
            else:
                print("Enter Proper data")

            break

            
                    
            # else:
            #     self.queryhandler.delete_data('course', condition= {'course_id' : ad_id})
            #     print("data deleted successfully")
            #     break
   
# /************************************************ feedback ******************************************
    def feedback(self):
        ''' method for storing the feedback data on database'''
        id = 'user_id'
        user_id = self.foreign_key()

        while True:
            print(f" User Feedback ")
            feedback_head = input("Enter subject/heading: ")
            print("Enter the feedback [stop = '//']: ")
            feedback_txt = ""
            while True:
                user_desc = input()
                if user_desc == '//':
                    break
                feedback_txt += user_desc + " "

            feedback_date = datetime.now()

            # connecting data to the database table { insertion query perform }
            if feedback_head and feedback_txt:
                feedback_data = {'user_id': user_id , 'feedback_head': feedback_head, 'feedback_text': feedback_txt, 'feedback_date': feedback_date}
                try:
                    # user_id = self.query_handler.select_data('user')
                    self.query_handler.insert_data('feedback', feedback_data)
                    print("Thanks for the feedback")
                    break
                except Exception as e:
                    print(f"Error occurred while inserting feedback: {e}")
            else:
                print("All the fields must be filled correctly")

    def show_feedback(self):
        ''' display feedback on admin side '''
        feedback_data = self.query_handler.select_data('feedback')
        table_data = [[ 'feedback_id', 'user_id', 'feedback_head', 'feedback_text', 'feedback_date' ]] 
        table_data.extend(feedback_data) 
        table = AsciiTable(table_data)
        print(table.table)
 
#  ********************************************** blog *********************************************
    def blog(self):
        ''' method for storing the blog data on database'''

        while True:
            print(f" User Blog ")
            blog_head = input("Enter subject/heading: ")
            print("Enter the feedback [stop = '//']: ")
            blog_txt = ""
            while True:
                user_desc = input()
                if user_desc == '//':
                    break
                blog_txt += user_desc + " "

            blog_date = datetime.now()

            # connecting data to the database table { insertion query perform }
            if blog_head and blog_txt:
                blog_data = {'blog_head': blog_head, 'blog_text': blog_txt, 'blog_date': blog_date}
                try:
                    # user_id = self.query_handler.select_data('user')
                    self.query_handler.insert_data('blog', blog_data)
                    print("Blog added successfully")
                    break
                except Exception as e:
                    print(f"Error occurred while inserting feedback: {e}")
            else:
                print("All the fields must be filled correctly")

    def show_blog(self):
        ''' display feedback on admin side '''
        blog_data = self.query_handler.select_data('blog')
        table_data = [[ 'blog_id', 'blog_head', 'blog_text', 'blog_date' ]] 
        table_data.extend(blog_data) 
        table = AsciiTable(table_data)
        print(table.table)
 
# ********************************************** Payment *******************************************
    # def payment(self):
    #     ad_id = 'admission_id'
    #     admission_id = self.query_handler.get_last_user_id('admission', column = ad_id)
    #     while True:
    #         print("\nTo get the admission its compulasuary to pay.\n")
    #         try:
    #             card = input("Enter card number [16 digit]:")
    #             amount = int(input("Enter the payment : "))
    #             if len(card) != 16:
    #                 print("\nInvalid card  number : \n")
    
    #             payment_date = datetime.now()
    #             if card == "" or amount == "":
    #                 user_input = input("without payment admission'll declined \nwant to continue :[y\n] : ")
    #                 if user_input == 'y' or user_input == 'Y':
    #                     continue
    #                 elif user_input == 'n' or user_input == 'N':
    #                     break
    #                 else:
    #                     print("Invalid input ")
    #                     break
                    
    #         except :
    #             print("\nInvalid input\n")

    #         if card and amount:
    #                 payment_data = {'admission_id' : admission_id, 'amount': amount, 'payment_date': payment_date }
    #                 try:
    #                     # user_id = self.queryhandler.select_data('user')
    #                     self.query_handler.insert_data('payment', payment_data)
    #                     print("\nPayment Successful\n")

    #                     break
    #                 except Exception as e:
    #                     print(f"\nError occurred while inserting feedback: {e}\n")
    #         else:
    #             print("\nAll the fields must be filled correctly\n")

# ********************************************* About Us ****************************************
    def about(self):
        about_info = '''
        **************************************************************************************************************************
        |                                                  About Us                                                              |
        **************************************************************************************************************************
        | ==> Established with the vision of cultivating courageous leaders, innovators, and critical thinkers.                  |
        |                                                                                                                        |
        | ==> Courage Education offers a wide range of programs and courses designed to inspire and empower students.            |
        |                                                                                                                        |
        | ==> Our curriculum combines academic rigor with practical applications.                                                |
        |                                                                                                                        |
        | ==> ensuring that students are prepared for the challenges and opportunities that lie ahead.                           |
        |                                                                                                                        |
        | ==> Proper guidance.                                                                                                   |
        |                                                                                                                        |
        | ==> Live classes with physical training.                                                                               |
        |                                                                                                                        |
        | ==> Sports, Real world Experience, Extra particular activity etc...                                                    |
        |                                                                                                                        |
        | ==> we prioritize the holistic development of our students.                                                            |
        |                                                                                                                        |  
        | ==> We offer a range of extracurricular activities, clubs, and organizations that cater to a wide variety of interests |
        **************************************************************************************************************************
        '''
        print(f"{about_info}")


if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.run()
    # main_menu.admission_status_change()
   

