import pathlib
from pathlib import Path
import sys
import pandas as pd 
from sklearn.model_selection import train_test_split
import yaml

#import yaml

def load_data(data_path):
    '''This functionn will read the data'''
    df = pd.read_csv(data_path)
    return df 

def tra_tes_split(df,test_split,seed):
    '''This function will split the data into training and testing'''
    train_df, test_df = train_test_split(df, test_size = test_split, random_state = seed)
    return train_df, test_df

def save_data(train, test, output_path):
    pathlib.Path(output_path).mkdir(parents = True, exist_ok = True) #this will convert output_path to path object so that it can use all the methodes of Path.
    #We can see we are using mkdir to create directory. if any of the directory is missing in a path then it will get created automatically 
    # by passing parent = True parameter  and by passing exist_ok = True u can avoid error due to already exist directory
    train.to_csv(output_path + '/train.csv', index = False)
    test.to_csv(output_path + '/test.csv', index = False)


def main():
    #---------------------------- setting up the file path ------------------------------------------
    #This gives the path of current directory i.e in our case this code will give the path of make_dataset.py
    #i.e c:\Mlops\creditcard_project\creditcard_rajesh\creditcard_repository\src\data\make_dataset.py
    file_path = pathlib.Path(__file__)

    #here 1st parent will bring you back at data folder 2nd parent will bring you in src folder and 
    # #3rd parent will bring you in main project folder i.e creditcard_repository
    home_dir = file_path.parent.parent.parent # now you are at c:\Mlops\creditcard_project\creditcard_rajesh\creditcard_repository

    #as_posix replaces  '\' with '/' so that python read the path 
    print(home_dir.as_posix()) 

    #Using following syntax you can go inside any folder in home directory
    params_file = home_dir.as_posix() + '/params.yaml'
    #following will open params.yaml file and will read the content inside of it
    params = yaml.safe_load(open(params_file))["make_dataset"]
    

    #this will give us a path of our main dataset
    data_path = home_dir.as_posix() + '/data/raw/creditcard.csv'

    #this will give us a path to store our processed data 
    output_path = home_dir.as_posix() + '/data/processed'
   #---------------------------------------- calling functions with dynamic parameters -----------------------------------------------------    
   
    data = load_data(data_path)  #take the data_path dynamically 
    train_data, test_data = tra_tes_split(data, params['test_split'], params['seed']) #takes the data,test_split and seed dynamically
    save_data(train_data, test_data, output_path) #takes train_data, test_data and output_path dynamically
    

if __name__ == "__main__":
    main()
