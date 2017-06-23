import pymongo

client = pymongo.MongoClient()
db = client['vaibhav']

i = db.test.insert_one({})

print i.inserted_id

ins = db.test.insert_many({
    "_id": i.inserted_id,
        {
            "name": "Vaibhav",
            "url": "randomusik.tk"
        }
    })

print ins.inserted_id