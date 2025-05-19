# wasteful_app.py

import time

def create_large_list(size):
    """Creates a list of squares."""
    # This will allocate a significant chunk of memory
    return [i*i for i in range(size)]

def concatenate_strings(count):
    """Concatenates strings inefficiently."""
    # String concatenation in a loop like this is notoriously slow
    # and creates many intermediate string objects.
    result = ""
    for i in range(count):
        result += str(i) # Bad practice
    return result

def complex_computation(n):
    """Simulates some CPU-bound work."""
    # This is just to burn CPU cycles.
    total = 0
    for i in range(n):
        total += i
        if i % 1000 == 0: # Add some conditional complexity
            time.sleep(0.00001) # Tiny sleep, mostly CPU work still
    return total

def main_operation():
    print("Starting main operation...")
    list_size = 10**6
    string_count = 10**4
    computation_limit = 10**7

    my_large_list = create_large_list(list_size)
    print(f"Large list created with {len(my_large_list)} elements.")

    # Let's hold onto this memory for a bit
    # In a real app, this might be unintentional

    s = concatenate_strings(string_count)
    print(f"Concatenated string length: {len(s)}")

    result = complex_computation(computation_limit)
    print(f"Computation result: {result}")

    # Explicitly delete to see memory drop if we were tracking it closely
    # del my_large_list
    # del s
    print("Main operation finished.")

if __name__ == "__main__":
    main_operation()