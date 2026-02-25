from .loader import load_dataset
from .preprocess import remove_noise, normalize
from .analysis import calc_ndvi

def run_pipeline(path):
    ds = load_dataset(path)
    ds = normalize(remove_noise(ds))
    return calc_ndvi(ds)