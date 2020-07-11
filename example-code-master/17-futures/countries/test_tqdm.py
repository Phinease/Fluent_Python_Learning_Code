import time
import concurrent.futures
from tqdm import tqdm


def f(x):
    time.sleep(0.0001)  # to visualize the progress
    return x**2


def run(f, my_iter):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(tqdm(executor.map(f, my_iter), total=len(my_iter)))
    return results


my_iter = range(100000)
# run(f, my_iter)


def run2(f, my_iter):
    cc = tqdm(total=len(my_iter))
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        l = []
        for i in my_iter:
            res = executor.submit(f, i)
            res.add_done_callback(lambda x: cc.update())
            l.append(res)

run2(f, my_iter)