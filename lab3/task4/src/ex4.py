import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from lab3.utils.utils import write_output, read_input, time_memory_tracking


if __name__ == "__main__":
    time_start = time.perf_counter()
    time_memory_tracking(time_start)