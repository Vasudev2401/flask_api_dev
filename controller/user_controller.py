from app import app
from model.user_model import user_model
from flask import request,send_file
from datetime import datetime

obj = user_model()

@app.route('/user/getall')
def user_getall_controller():
    return obj.user_getall_model()

@app.route('/user/getall/limit/<int:limit>/page/<int:page>')
def user_getall_controller_by_page(limit,page):
    return obj.user_getall_model_by_page(limit,page)

@app.route('/user/addone',methods = ['POST'])
def user_addone_controller():
    return obj.user_addone_model(request.form)

@app.route('/user/update',methods = ['PUT'])
def user_update_controller():
    return obj.user_update_model(request.form)

@app.route('/user/delete/<id>',methods = ['DELETE'])
def user_delete_controller(id):
    return obj.user_delete_model(id)

@app.route('/user/patch/<id>',methods = ['PATCH'])
def user_patch_controller(id):
    return obj.user_patch_model(request.form,id)

@app.route("/user/<id>/upload/avatar",methods = ["PUT"])
def user_upload_avatar_controller(id):
    file = request.files['avatar']
    uniquefilename = str(datetime.now().timestamp()).replace(".","")
    # return "This is user_upload_avatar_controller"
    fileNameSplit = file.filename.split(".")
    ext = fileNameSplit[len(fileNameSplit) - 1]
    finalFilePath = f"uploads/{uniquefilename}.{ext}"
    file.save(finalFilePath)
    return obj.user_upload_avatar_model(id,finalFilePath)

@app.route("/uploads/<filename>")
def user_get_avatar_controller(filename):
    return send_file(f"uploads/{filename}")