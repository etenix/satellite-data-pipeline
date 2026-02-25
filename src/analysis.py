def calc_ndvi(ds, nir="nir", red="red"):
    return (ds[nir] - ds[red]) / (ds[nir] + ds[red])