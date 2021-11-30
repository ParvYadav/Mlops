# Read the data from the data source
# Save the data in data/raw for the furture process

import os
import pandas
from get_data import get_data,read_params
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_colums = [col.replace(' ','_') for col in df.columns]
    raw_data_path = config['load_data']['raw_dataset_csv']
    df.to_csv(raw_data_path,sep=',',header=new_colums,index=False)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    data = load_and_save(config_path=parsed_args.config)