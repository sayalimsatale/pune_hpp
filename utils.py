import config
import pickle
  
def load_model():
   with open(config.MODEL_PATH,'rb') as f:
     return pickle.load(f)
   
def load_data():
   return pd.read_csv(config.DATA_FILE)

     