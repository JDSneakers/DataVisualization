from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:52308/AAC' % (username, password)) 
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        try:
            if data is not None:
                read_result = list(self.database.animals.find(data, {"_id": False}))
                return read_result
            else:
                raise Exception("Nothing to read.")
                return False
        except Exception as e:
            print("Exception has occured: ", e)
                      
# Create a method to implement the U in CRUD.
    def update(self, fromData, toData):
        if fromData is not None:
            result = self.database.animals.update(fromData, toData)
            print(result)
        
        else:
            raise Exception("Nothing to update")
            
# Create a method to implement the D in CRUD.
    def delete(self, data, option):
        if data is not None:
# Option 1 is passed to delete only the first matching entry
            if option == 1:
                result = self.database.animals.delete_one(data)
                print(result)
# Option 2 is passed to delete all matching entries            
            if option == 2:
                result = self.database.animals.delete_many(data)
                print(result)
                
        else:
            raise Exception("Nothing to delete")