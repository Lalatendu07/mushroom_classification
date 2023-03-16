import pandas as pd
from mushroom_clf.config import mongo_client
from mushroom_clf.logger import logging
from mushroom_clf.exception import MushroomException
import os,sys

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    Description: This function return collection as dataframe
    ==========================================================
    Params:
    database_name: database name
    collection_name: collection name
    ==========================================================
    return Pandas dataframe of a collection
    """
    try:
        logging.info(f"Reading data from database: {database_name} and {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info("Found dataset")
        if "_id" in df.columns:
            logging.info("Dropping column: _id")
            df=df.drop("_id",axis=1)
        logging.info(f"Rows and columns in df: {df.shape}")
        return df    

    except Exception as e:
        raise MushroomException(e, sys) from e    