from dask.distributed  import LocalCluster,Client  
# Creating local cluster
cluster = LocalCluster()
# Creating client
client = Client(cluster)
# Displaying client dashboard
print(client.dashboard_link)
# shutdown cluster
client.shutdown()
