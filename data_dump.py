import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "/config/workspace/agaricus-lepiota.data"
DATABASE_NAME = "mushroom"
COLLECTION_NAME = "mushroom_dataset"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f'Rows and columns: {df.shape}')

    #Convert dataframe to json
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)