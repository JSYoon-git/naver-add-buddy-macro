import random
import time


def delay_function(max_delay):
    random_second0 = random.choice(range(0, max_delay))
    random_second1 = random.choice(list(t * 0.1 for t in range(0, 10)))
    random_second2 = random.choice(list(t * 0.01 for t in range(0, 10)))
    random_second3 = random.choice(list(t * 0.001 for t in range(0, 10)))
    random_second4 = random.choice(list(t * 0.0001 for t in range(0, 10)))
    random_delay = (
        random_second0
        + random_second1
        + random_second2
        + random_second3
        + random_second4
    )
    time.sleep(random_delay)
    print(random_delay)


