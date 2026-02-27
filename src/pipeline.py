from src.loader import load_dataset
from src.preprocess import remove_noise, normalize
from src.analysis import calc_ndvi


def run_pipeline(path):

    ds = load_dataset(path)

    ds_clean = remove_noise(ds)

    ds_norm = normalize(ds_clean)

    ndvi = calc_ndvi(ds_norm)

    return ndvi