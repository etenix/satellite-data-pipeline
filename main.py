from dask.distributed import Client
from src.pipeline import run_pipeline

def main():
    client = Client()
    result = run_pipeline("data/sample.nc")
    output = result.compute()
    output.to_netcdf("output.nc")

if __name__ == "__main__":
    main()