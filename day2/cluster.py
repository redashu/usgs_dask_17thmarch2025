from dask.distributed  import LocalCluster,Client  
import dask.array as da

# Creating local cluster with default configuration
#cluster = LocalCluster()
# LocalCluster will create cluster custom config 
cluster = LocalCluster(
    n_workers=2,  # Number of workers to create use your cpu cores count 
    threads_per_worker=2, # number of threads per worker
    memory_limit='2GB' # memory limit per worker you can also use 40% of total memory
)
# Creating client
client = Client(cluster)
# Displaying client dashboard
print(client.dashboard_link)
# using dask array to create array of 1000 elements
arr1 = da.ones((1000,1000),chunks=(100,100))
# performing sum , mean of array elements using dask array
# these oparation transformation in dask array
result1 = arr1.sum()
result2 = arr1.mean()
# using action call to get the result -- compute
# this will trigger the computation
print(result1.compute())
print(result2.compute())

# shutdown cluster
client.shutdown()
