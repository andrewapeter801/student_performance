from base import Base
import pymongo
import os
from dotenv import load_dotenv

class ToMongo(Base):
    '''
    Designed as a class to transport the data from our Base class to MongoDB instance.
    Initializes an instance of the inherited class.

    Definded methods are as follows:
    upload_one_by_one: Upload pieces of information to a database one by one over an iterable structure.
    upload_collection: Uploads an entire collection of documents to MongoDB.
    delete_collection: Drops an entire collection of data from the database.
        '''

    def __init__(self):
        # initialize an instance of our inherited class:
        Base.__init__(self)

        # Load in the env variables:
        load_dotenv()
        self.__mongo_url = os.getenv('MONGO_URL')

        # Connect to PyMongo
        self.client = pymongo.MongoClient(self.__mongo_url)

        #Create the database
        self.db = self.client.db

        # create/connect to a collection
        self.cards = self.db.cards

        # set the Dataframe index to the ID column:
        self.df.set_index('id', inplace= True)

    def upload_one_by_one(self):
        ''' 
        Upload all our items in the dataframe to MongoDB
        This method will take longer, but will ensure all our data is corretly uploaded.
        '''
        for i in self.df.index:
            self.cards.insert_one(self.df.loc[i].to_dict())

    def upload_collection(self):
        '''
        UPload entire collection of documents to MongoDB
        BEWARE! This THERE IS A MAXIMUM UPLOAD SIZE!!!
        Limitations are placed on the amount odata that you can upload at one time!
        '''
        self.cards.insert_many([self.df.to_dict()])

    def drop_collection(self):
        self.db.cards.drop()

    def drop_collection_dynamic(self, col_name:str='cards'):
        self.db.drop_collection(col_name)

if __name__ =='__main__':
    c = ToMongo()
    print('Successful Connection to Client Object')
    c.drop_collection_dynamic()
    print('Dropped the Cards Collection')
    c.upload_one_by_one()
    print('Successfully Uploaded all Card Info to MongoDB!')