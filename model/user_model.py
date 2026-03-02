import mysql.connector
import json
from flask import make_response


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
            res = make_response({"payload":result},200)
            res.headers["Access-Control-Allow-Origin"] = "*"
            return res
        else:
            return make_response({"message":"No data found"},204)
        
    def user_addone_model(self,data):
        self.cursor.execute(f"Insert into users(name,email,phone,role,password) values('{data['name']}','{data['phone']}','{data['email']}','{data['role']}','{data['password']}')")
        return make_response({"message":"User created successfully"},201)
        
    def user_update_model(self,data):
        ##business logic
        ##Query Execution code
        self.cursor.execute(f"Update users set name='{data['name']}' , phone = '{data['phone']}' , email = '{data['email']}' , role='{data['role']}' , password = '{data['password']}' where id = {data['id']}")
        if self.cursor.rowcount > 0:
            return make_response({"message":"User updated successfully"},201)
        else:
            return ({"message":"Nothing to update"},202) 
        
    def user_delete_model(self,id):
        ##business logic
        ##Query Execution code
        print("In delete model")
        self.cursor.execute(f"delete from users where id={id}")
        if self.cursor.rowcount > 0:
            return make_response({"message":"User Deleted Successfully"},200)
        else:
            return make_response({"message":"Nothing to delete"},202)
        
    def user_patch_model(self,data,id):
        query = "Update users set "
        for key in data:
            query = query + f"{key} = '{data[key]}', "
        query = query[:-2]
        query += f" where id = {id}"
        self.cursor.execute(query)
        if self.cursor.rowcount > 0:
            return make_response({"message":"User updated successfully"},201)
        else:
            return make_response({"message":"Nothing to update"},202) 

        ##Update users set col = val , col = val where id = {id}        
        

        