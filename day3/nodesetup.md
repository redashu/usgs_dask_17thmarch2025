# Setting Up a Dask Cluster on a Single Machine

A Dask cluster can be set up on a single machine to utilize multiple CPU cores and manage memory efficiently. Here’s how you can configure it with optimal CPU and memory settings.

## 1. Install Dask

Ensure you have Dask installed:

```bash
pip install dask distributed
```

For advanced usage (like NumPy-based arrays), install additional dependencies:

```bash
pip install dask[complete]
```

## 2. Start a Dask Cluster on a Single Machine

Dask provides multiple ways to start a cluster. The best approach for a single machine is using the `LocalCluster`.

### Method 1: Using Python (`LocalCluster`)

```python
from dask.distributed import Client, LocalCluster

# Create a Local Cluster with custom configurations
cluster = LocalCluster(
    n_workers=4,        # Number of worker processes (adjust based on CPU cores)
    threads_per_worker=2,  # Threads per worker (adjust for parallelism)
    memory_limit='4GB',  # Limit memory per worker (e.g., '4GB' or '50%')
    processes=True       # Set to False if using shared memory (useful for numpy)
)

client = Client(cluster)  # Connect to the cluster
print(client)  # See cluster info
```

**Best Use Case:** Optimizes CPU and memory utilization for a single machine.

### Method 2: Using CLI

Run the following in your terminal:

```bash
dask scheduler  # Starts the scheduler
dask worker localhost:8786 --nprocs 4 --nthreads 2 --memory-limit 4GB  # Starts workers
```

**Adjustments:**

- `--nprocs 4` → Number of worker processes
- `--nthreads 2` → Number of threads per worker
- `--memory-limit 4GB` → Memory allocated per worker

## 3. Adjust CPU and Memory Settings

| Setting             | Description                                | Recommended Value               |
|---------------------|--------------------------------------------|----------------------------------|
| `n_workers`         | Number of worker processes                | `# of CPU cores - 1`            |
| `threads_per_worker`| Number of threads per worker              | `1` for CPU-intensive, `>1` for IO-bound tasks |
| `memory_limit`      | Maximum memory per worker                 | `'4GB'` or `'50%'`              |
| `processes`         | Whether to use separate processes or threads | `True` for separate memory, `False` for shared memory |

## 4. Using Dask Arrays to Process Data

Dask Arrays work like NumPy, but they split data into chunks and process them in parallel.

### Example 1: Create a Large Dask Array

```python
import dask.array as da

# Create a large random array (10,000 x 10,000) split into (1000x1000) chunks
x = da.random.random((10000, 10000), chunks=(1000, 1000))
print(x)  # Lazy evaluated
```

### Example 2: Perform Parallel Computation

```python
# Compute mean across the entire array (parallel execution)
mean_value = x.mean().compute()
print(mean_value)
```

### Example 3: Save and Load Large Arrays Efficiently

```python
# Save array to disk
da.to_zarr(x, 'large_array.zarr')

# Load from disk
x_loaded = da.from_zarr('large_array.zarr')
```

## 5. Monitoring Dask Performance

To monitor Dask’s performance:

```python
client.dashboard_link  # Open the web UI for monitoring
```

Alternatively, start the dashboard manually:

```bash
dask scheduler --dashboard-address :8787
```

Then open [http://localhost:8787](http://localhost:8787) in your browser.

---

## Final Thoughts

✅ Use `LocalCluster` to maximize CPU and memory usage.  
✅ Adjust `n_workers`, `threads_per_worker`, and `memory_limit` for performance.  
✅ Use Dask Arrays for parallel processing of large numerical datasets.  
✅ Monitor performance using the Dask dashboard.