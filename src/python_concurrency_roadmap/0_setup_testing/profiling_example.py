import time

# YOU MUST DECORATE THE FUNCTIONS YOU WANT TO PROFILE
from memory_profiler import profile

@profile
def create_large_list(size):
    """Creates a list of squares."""
    # This will allocate a significant chunk of memory
    data = [i*i for i in range(size)] # Line of interest
    return data

@profile
def concatenate_strings(count):
    """Concatenates strings inefficiently."""
    result = "" # Line of interest
    for i in range(count):
        result += str(i) # Line of interest (repeatedly)
    return result

def complex_computation(n): # Not profiling this one with memory-profiler for demo
    """Simulates some CPU-bound work."""
    total = 0
    for i in range(n):
        total += i
        if i % 1000 == 0:
            time.sleep(0.00001)
    return total

# @profile # You can also profile the main calling function
def main_operation_mem_profile():
    print("Starting main operation (memory-profiler)...")
    list_size = 10**5 # Reduced for faster memory-profiler output
    string_count = 10**3 # Reduced for faster memory-profiler output
    computation_limit = 10**6 # Reduced

    my_large_list = create_large_list(list_size)
    print(f"Large list created with {len(my_large_list)} elements.")

    s = concatenate_strings(string_count)
    print(f"Concatenated string length: {len(s)}")

    result = complex_computation(computation_limit)
    print(f"Computation result: {result}")
    print("Main operation finished.")

if __name__ == "__main__":
    main_operation_mem_profile()