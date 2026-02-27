import xarray as xr


def load_dataset(path, chunks=None):
    """
    Load satellite dataset with chunking
    """
    ds = xr.open_dataset(
        path,
        chunks=chunks or {
            "time": 50,
            "lat": 500,
            "lon": 500
        }
    )

    return ds