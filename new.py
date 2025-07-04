from flask import Flask, request, jsonify, render_template

import mysql.connector

app=Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask is working!"

db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='mydatabase'
)

    
@app.route('/addStudent',methods=['POST'])

def add_student():
    data=request.get_json()
    print("Received data:", data)
    name=data.get('name')
    mark=data.get('mark')
    
    cursor=db.cursor()
    sql_query="INSERT INTO students (name,mark) VALUES(%s,%s)"
    cursor.execute(sql_query,(name,mark))
    db.commit()
    return jsonify({"Message":"Success"}),200

@app.route('/fetchAll',methods=['GET'])

def fetch_all():
    cursor=db.cursor(dictionary=True) 
    cursor.execute("SELECT * FROM students")
    rows=cursor.fetchall()
    cursor.close()
    return jsonify(rows)

@app.route('/fetchbyid/<int:id>',methods=['GET'])
def fetchById(id):
    cursor=db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE ID=%s",(id,))
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)
    
    
@app.route('/update',methods=['PUT'])
def update_data():
    id=request.json.get('id')
    name=request.json.get('name')
    mark=request.json.get('mark')
    cursor=db.cursor()
    query="UPDATE students SET name=%s,mark=%s WHERE id=%s"
    cursor.execute(query,(name,mark,id))
    db.commit()
    cursor.close()
    return jsonify({"message":"Success"}),200

@app.route('/delete/<int:id>',methods=['DELETE'])
def delete_data(id):
    cursor=db.cursor()
    query="DELETE FROM students WHERE id=%s"
    cursor.execute(query,(id,))
    db.commit()
    cursor.close()
    return jsonify({"message":"Deleted"}),200

@app.route('/postList', methods=['POST'])
def post_list():
    if not request.is_json:
        return jsonify({"error": "Invalid Content-Type. Expected application/json"}), 400

    reqData = request.get_json()

    if not isinstance(reqData, list):
        return jsonify({"error": "Expected a list of student records"}), 400

    cursor = db.cursor()
    query = "INSERT INTO students (name, mark) VALUES (%s, %s)"
    for stu in reqData:
        name = stu.get('name')
        mark = stu.get('mark')
        if name is None or mark is None:
            return jsonify({"error": "Missing name or mark in one of the records"}), 400
        cursor.execute(query, (name, mark))
    db.commit()
    cursor.close()
    return jsonify({"message": "Done"}), 200

from flask import render_template

@app.route('/frontend')
def frontend():
    return render_template('index.html')

 


if __name__=="__main__":
    print("connection to db")
    app.run(debug=True)