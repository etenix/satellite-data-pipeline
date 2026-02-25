import numpy as np


def remove_noise(ds, threshold=0.01):
    """
    Remove low-value noise
    """
    ds_clean = ds.where(ds > threshold)

    return ds_clean


def normalize(ds):
    """
    Normalize values to [0,1]
    """
    min_val = ds.min()
    max_val = ds.max()

    return (ds - min_val) / (max_val - min_val)