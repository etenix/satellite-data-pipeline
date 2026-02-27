def calc_ndvi(ds, nir_band="nir", red_band="red"):
    """
    Calculate NDVI
    """
    nir = ds[nir_band]
    red = ds[red_band]

    ndvi = (nir - red) / (nir + red)

    return ndvi