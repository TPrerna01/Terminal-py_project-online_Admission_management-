import mysql.connector
from mysql.connector import Error

class Database_connection:
    '''DATABASE CONNECTION AND ALL REUSABLE QUERY FUNCTION'''

    def __init__(self):
        '''connection of database '''

        try:
            #  database connection creation 
            self.connection = mysql.connector.connect( host="localhost", user="root", password="123456", database="CourageEducation" )
            self.my_cursor = self.connection.cursor(buffered=True)

            # table creation
            user_table = {'user' : [
                                'user_id INT AUTO_INCREMENT PRIMARY KEY', 
                                'name VARCHAR(255) NOT NULL', 
                                'ph_no VARCHAR(20) NOT NULL',
                                'email VARCHAR(255) NOT NULL', 
                                'password VARCHAR(255) NOT NULL', 
                                'gender ENUM("Male", "Female", "Other") NOT NULL', 
                                'dob DATE NOT NULL',
                                'is_admin BOOLEAN DEFAULT FALSE',
                                'UNIQUE (email)'                    ]}
            self.create_tables(user_table)

            admission_table = { 'admission' : [
                                'admission_id INT AUTO_INCREMENT PRIMARY KEY',
                                'user_id INT',
                                'course_id INT',
                                'course_type ENUM("Online", "Offline") NOT NULL',
                                'admission_date DATE',
                                'per_institute VARCHAR(255) NOT NULL',
                                'per_course VARCHAR(255) NOT NULL',
                                'per_grade VARCHAR(20) NOT NULL',
                                'status ENUM("Pending", "Accepted", "Declined") DEFAULT "Pending"',
                                'FOREIGN KEY (user_id) REFERENCES user(user_id)',
                                'FOREIGN KEY (course_id) REFERENCES course(course_id) '       ]}
            self.create_tables(admission_table)

            course_table = { 'course': [
                                    'course_id INT AUTO_INCREMENT PRIMARY KEY',
                                    'course_name VARCHAR(255) NOT NULL',
                                    'course_description TEXT',
                                    'department VARCHAR(255)',
                                    'online_availability BOOLEAN',
                                    'admission_requirements TEXT',
                                    'course_duration VARCHAR(50)',
                                    'course_price VARCHAR(8)'          
                                    'UNIQUE (course_name)'                 ]}
            self.create_tables(course_table)

            payment_table = {'payment' : [
                                    'payment_id INT AUTO_INCREMENT PRIMARY KEY',
                                    'admission_id INT',
                                    'amount DECIMAL(10, 2)',
                                    'payment_date DATE',
                                    'FOREIGN KEY (admission_id) REFERENCES admission(admission_id)'    ]}
            self.create_tables(payment_table)

            feedback_table = { 'feedback' : [
                                        'feedback_id INT AUTO_INCREMENT PRIMARY KEY',
                                        'user_id INT',
                                        'feedback_head VARCHAR(255) NOT NULL',
                                        'feedback_text TEXT',
                                        'feedback_date DATE',
                                        'FOREIGN KEY (user_id) REFERENCES user(user_id) '         ]}
            self.create_tables(feedback_table)

            blog_table = { 'blog' : [
                                        'blog_id INT AUTO_INCREMENT PRIMARY KEY',
                                        'blog_head VARCHAR(255) NOT NULL',
                                        'blog_text TEXT',
                                        'blog_date DATE',                                  ]}
            self.create_tables(blog_table)

        except Error as e:
            print(f"Database connection error! {e}")

    def execute_query(self, query, data=None):
        '''EXECUTING QUERIES'''
        try:
            if data :
                # breakpoint()
                self.my_cursor.execute(query, data)
            else:
                self.my_cursor.execute(query)
            # breakpoint()
            self.connection.commit()
            

        except Error as e:
            print(f"Error while query Executing: {e}")

    def create_tables(self,table_data):
        '''CREATING TABLE QUERY'''
        try:
            for table_name, columns in table_data.items():
                create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
                self.execute_query(create_table_query)
                

        except Error as e:
            print(f"Error creating tables: {e}")



    # def close_connection(self):
    #     '''Close database connection.'''
    #     if self.connection.is_connected():
    #         self.my_cursor.close()
    #         self.connection.close()
    #         # print("Connection closed")



# # var for running connect_database func
# connection = Database_connection()




