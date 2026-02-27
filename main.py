from dask.distributed import Client
from src.pipeline import run_pipeline


def main():

    client = Client()  # start local cluster

    print(client)

    result = run_pipeline("data/sample.nc")

    # Trigger computation
    output = result.compute()

    output.to_netcdf("output/result.nc")


if __name__ == "__main__":
    main()