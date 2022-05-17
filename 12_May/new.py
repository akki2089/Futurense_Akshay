from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:test@akkifuturense.jvfqr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.get_database('Student.db')
records = db.Student_records

records.count_documents({})

new_student = {
 "name":"Akki",
 "roll_number":"18BCS4174",
 "phone_num":"8107784417"
 }

records.insert_one(new_student)