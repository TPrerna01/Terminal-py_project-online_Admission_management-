from query import ExeQueries as queryhandler
import re
from datetime import datetime

class  validation:
    ''' validation/condition of the data in table '''
    # validation registration

    def register(self, name, ph_no, email, password, dob):
        '''signup validation function'''
        name_condition = re.match(r'^[a-zA-Z\s]+$', name)
        phone_condition = re.match(r"^\d{10}$", ph_no)
        # mail = (queryhandler.select_data('user', f"email='{email}'"))
        email_condition = (re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email ) )
        pswd_condition =  (len(password) >= 8) and re.search(r'[\da-zA-Z!@#$%^&*()_+=\-[\]{};:\'",.<>?]', password)
        dob_condition = re.match(r'^\d{4}-\d{2}-\d{2}$',dob)

        con_group = [name_condition, phone_condition, email_condition, pswd_condition, dob_condition]
        val_error = ["Invalid name", "Invalid phone number", "Invalid email-id", "Invalid password type or length" ,"Invalid DOB"]
                                
        errors = []
        for i, data in enumerate(con_group):
            if not data:
                errors.append(f" {val_error[i]}")

        if errors:
            return errors
        else:
            # Perform registration process
            return []
        

    def course_valid(self, name, online_ava, cou_dur):
        '''course data validation func '''
        name_condition = re.match(r'^[a-zA-Z\s]+$', name)
        cou_dur_condition = (r'^[a-zA-Z0-9.-]',cou_dur)

        course_group = [name_condition, cou_dur_condition ]
        val_error = ["Invalid name", "Invalid data entry"]
                                
        errors = []
        for i, data in enumerate(course_group):
            if not data:
                errors.append(f" {val_error[i]}")

        if errors:
            return errors
        else:
            # Perform registration process
            return []
        
    def admission_valid(self,date):
        '''admission validation function'''
        date_condition = re.match(r'^\d{4}-\d{2}-\d{2}$',date) and datetime.strftime(date, "%Y%m%d")
        if not date_condition:
            print(f"Invalid date")
            return False
        else :
            return True
        

        

# ex = validation()        
# ex.register(name= 'asd', ph_no= '9898959692',email= 'netra@gmail.com', password= '123456253',)


    

