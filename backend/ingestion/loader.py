import dask.bag as db
from dask.bag import read_text

def load_logs(file_path):
    bag = db.read_text(file_path)
    return bag


    # ground1ct() > convert data
    # dask.bag is from send dask data into dask dataframe by filtering and mapping
    
    