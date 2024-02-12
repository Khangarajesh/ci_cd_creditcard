import pathlib
from pathlib import Path
import sys
import yaml
import joblib
import pandas as pd 

from sklearn.ensemble import RandomForestClassifier

def train_model(train_features, target,n_estimators,max_depth,seed):
    model = RandomForestClassifier(n_estimators = n_estimators, max_depth = max_depth, random_state = seed)
    model.fit(train_features, target)
    return model

def save_model(model,output_path):
    joblib.dump(model, output_path + '/model.joblib')


def main():
    
    file_path = pathlib.Path(__file__)
    home_dir = file_path.parent.parent.parent
    param_file = home_dir.as_posix() + '/params.yaml'
    params = yaml.safe_load(open(param_file))['train_model']
    data_path = home_dir.as_posix() + '/data'
    output_path = home_dir.as_posix() + '/models'
    pathlib.Path(output_path).mkdir(parents = True, exist_ok = True)
    
    target = 'Class'
    train_features = pd.read_csv(data_path + '/processed/train.csv')
    x = train_features.drop(target, axis = 1)
    y = train_features[target]
    
    #train the model
    trained_model = train_model(x,y,params['n_estimators'],params['max_depth'], params['seed'])
    #save the model
    save_model(trained_model,output_path)
    
    
if __name__ == "__main__":
    main()
    