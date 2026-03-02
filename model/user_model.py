import mysql.connector
import json


class user_model():
    def __init__(self):
        ##Connection Establishment code
        try:
            self.con = mysql.connector.connect(host='localhost',user="root",password="omega@7314",database='flask_tutorial')
            self.con.autocommit = True
            self.cursor = self.con.cursor(dictionary = True)
            print("Connection Established")
        except:
            print("Some errors")

    def user_getall_model(self):
        ##business logic
        ##Query Execution code
        self.cursor.execute('Select * from users')
        result = self.cursor.fetchall()
        if len(result) > 0:
            # return json.dumps(result)
            return {"payload":result}
        else:
            return {"message":"No data found"}
        
    def user_addone_model(self,data):
        self.cursor.execute(f"Insert into users(name,email,phone,role,password) values('{data['name']}','{data['phone']}','{data['email']}','{data['role']}','{data['password']}')")
        return {"message":"User created successfully"}
        
    def user_update_model(self,data):
        ##business logic
        ##Query Execution code
        self.cursor.execute(f"Update users set name='{data['name']}' , phone = '{data['phone']}' , email = '{data['email']}' , role='{data['role']}' , password = '{data['password']}' where id = {data['id']}")
        if self.cur.rowcount > 0:
            return {"message":"User updated successfully"}
        else:
            return {"message":"Nothing to update"} 
        
    def user_delete_model(self,id):
        ##business logic
        ##Query Execution code
        self.cursor.execute(f"delete from users where id={id}")
        if self.cursor.rowcount > 0:
            return {"message":"User Deleted Successfully"}
        else:
            return {"message":"Nothing to delete"}
        
        

        