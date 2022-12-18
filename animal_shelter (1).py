from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username,password):
        # Initializing the MongoClient.  
        self.client = MongoClient('mongodb://%s:%s@localhost:46648' % ("accUser", 1234))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            return True# data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read_all(self, data):
        cursor = self.database.animals.find(data, {'_id':False} )
        
        return cursor
    
    def read(self,data):
        return self.database.animals.find_one(data)
    
# Create method to implement the U in CRUD.
    def update(self, data, new_data):
        if self.database.animals.count(data):
            print("Data exists")
            self.database.animals.update(data, new_data)
   
        else:
            raise Exception("Data not found")
            
# Create method to implement the D in CRUD.
    def delete(self, deleteData):
        
        if data is not None:
            delete_result = self.database.animals.delete(deleteData)
            result = "Documents deleted: " + json.dumps(delete_result.delete_count)
            return result
        
        else:
            raise Exception("No records found")
            
            
            