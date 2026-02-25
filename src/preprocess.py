def remove_noise(ds, threshold=0.01):
    return ds.where(ds > threshold)

def normalize(ds):
    return (ds - ds.min()) / (ds.max() - ds.min())