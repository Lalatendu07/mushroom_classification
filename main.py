from mushroom_clf.pipeline.batch_prediction import batch_prediction

file_path="/config/workspace/agaricus-lepiota.data"

if __name__ == "__main__":
     try:
         batch_prediction(input_file_path=file_path)
     except Exception as e :
          print(e)

