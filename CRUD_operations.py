import pymongo

#connecting python with mongodb
client=pymongo.MongoClient("mongodb://localhost:27017/")
client.list_database_names()

#Creating a database
db_name = client ["Telephone_Directory"]

#Creating a collection into the database
collection_name=db_name["user_info"]
db_name.list_collection_names()

#json file with info
info = [{
 "First Name": "Rajesh",
 "Last Name": "kulkarni",
 "phone No ": 9665043563,
 "city": "Aurangabad"
},
 {
 "Name": "Arjun",
 "Last Name": "Deshmukh",
 "phone No ": 9865042053,
 "city": "Mumbai"
},
 {
 "Name": "Nikita",
 "Last Name": "Deshpande",
 "phone No ": 9965842021,
 "city": "Hyderabad"
},
 {
 "Name": "Rohit",
 "Last Name": "Shetty",
 "phone No ": 9663442921,
 "city": "Chennai"
},
 {
 "Name": "Rita",
 "Last Name": "john",
 "phone No ": 9863463929,
 "city": "Delhi"
}
]
#inserting json file into the collection
collection_name.insert_many(info)

#Query to find records
print(collection_name.find_one({"Name": "Rohit"}))

#Modify records
query=collection_name.find_one({"Name": "Nikita"})
update={'$set':{"city": "Pune"}}
collection_name.update_one(query,update)

#delete records
collection_name.delete_one({"phone No ": 9865042053})