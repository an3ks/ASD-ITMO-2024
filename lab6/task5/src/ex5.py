import time
import sys
import os
from lab6.utils.utils import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


def count_votes(queries):
    """
    Подсчет голосов для кандидатов и сортировка по алфавиту
    """
    votes = {}
    for query in queries:
        name, vote_count = query.split()
        vote_count = int(vote_count)
        if name in votes:
            votes[name] += vote_count
        else:
            votes[name] = vote_count
    sorted_candidates = sorted(votes.items())
    results = [f"{name} {count}" for name, count in sorted_candidates]
    return results


if __name__ == "__main__":
    time_start = time.perf_counter()
    queries = read_input_lines("../txtf/input.txt")
    answ = count_votes(queries)
    write_output(answ, "../txtf/output.txt")
    file_name = os.path.basename(__file__)
    printResult(answ, file_name)
    time_memory_tracking(time_start)