from dbconnect import Database_connection 
    #     self.dbcon = Datab
from mysql.connector import Error

class ExeQueries:
    def __init__(self) :
        self.dbcon = Database_connection()
    # @staticmethod
    # def execute_query(query, data=None):
    #     try:
    #         connection = dbconnect.DatabaseConnection()
    #         connection.execute_query(query, data)
    #         connection.close_connection()

    #     except Error as e:
    #         print(f"Error while query genratig: {e}")


    def insert_data(self, table_name, data, fk = None):
        '''INSERTING DATA ON THE TABLE OF DATABASE'''
        try:
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            values = [str(value) for value in data.values()]

            # if fk_id is not None:
            #     self.select_data(fk_id)
            self.dbcon.execute_query(insert_query,tuple(values))
            # breakpoint()
            # self.dbcon.close_connection()

        except Error as e:
            print(f"Error creating inserting query: {e}")

    def select_data(self, table_name, columns=None,  condition=None):
        '''SELECTING QUERY FOR PRINTING TABLE DATA ON OUTPUT'''
        try:
            if columns :
                select_query = f" SELECT {','.join(columns)} FROM {table_name}"
            else :
                select_query = f"SELECT * FROM {table_name}"

            if condition:
                select_query += f" WHERE {condition}"
            
            self.dbcon.execute_query(select_query)
            result = self.dbcon.my_cursor.fetchall()
            return result
        
        except Error as e:
            print(f"Error creating selecting query: {e}")

    def foreign_key_attach (self):
        pass

    def delete_data(self, table, condition=None):
        try:
            query = f"DELETE FROM {table}"
            if condition:
                query += " WHERE "
                conditions = []
                for key, value in condition.items():
                    conditions.append(f"{key} = '{value}'")
                query += " AND ".join(conditions)
            self.dbcon.execute_query(query)
        except Error as e :
            print(f"error occur while delete query {e}")

    def get_last_user_id(self, table_name, column):
        '''Retrieve the last inserted user_id from the user table'''
        try:
            query = f"SELECT MAX({column}) FROM {table_name} "
            self.dbcon.execute_query(query)
            result = self.dbcon.my_cursor.fetchone()
            # breakpoint()
            if result:
                last_id = result[0]
                return last_id
            else:
                print("no data on the table")
                return None
        except Exception as e:
            print(f"Error fetching last user_id: {e}")

    
    def update_data(self, table_name, data, condition=None):
        try:
            set_clause = ', '.join(f"{column} = %s" for column in data.keys())
            values = tuple(data.values())  
            condition_clause = ' AND '.join(f"{column} = %s" for column in condition.keys())
            condition_values = tuple(condition.values())
            update_query = f"UPDATE {table_name} SET {set_clause} WHERE {condition_clause}"
            query_values = values + condition_values 
            # breakpoint()
            self.dbcon.execute_query(update_query, query_values)
        except Error as e:
            print(f"An error occurred while updating data: {e}")

    
    # def alter_data(self,table_name,data=None):
            
    #     try:
    #         columns = ', '.join(f" {column} = %s" for column in data.keys())
    #         values = tuple(data.values())
    #         alter_query = f" ALTER TABLE {table_name} MODIFY COLUMN {columns}"
    #         self.dbcon.execute_query(alter_query,values)
    #         breakpoint()

    #     except:
    #         print(f"error  occur while alter data ")
            
    def join_data(self,table1, table2, table3):
        try:
                

            query = f""" SELECT {table1}.admission_id, {table2}.name  as user_name, {table3}.course_name, {table1}.status
                    FROM {table1} 
                    INNER JOIN {table2} 
                    ON {table1}.user_id =  {table2}.user_id
                    INNER JOIN {table3} 
                    ON {table1}.course_id = {table3}.course_id
                    ORDER BY admission_id"""
            
            # breakpoint()
            self.dbcon.execute_query(query)
            results = self.dbcon.my_cursor.fetchall()
            return results
        
        except  Error as e:
            print(f"Error occur while join {e}")
                    