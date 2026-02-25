import xarray as xr

def load_dataset(path, chunks=None):
    return xr.open_dataset(path, chunks=chunks or {"time":50,"lat":500,"lon":500})