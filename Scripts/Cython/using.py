import run_python
import run_cython

import datetime
import logging

logging.basicConfig(filename="benchmark.log", level=logging.NOTSET)

iterations = [
    100,
    1000,
    5000,
    10000,
    15000,
    20000,
    25000,
    30000,
]

logging.info('Timestamp, Python, Cython, Iterations')
for iteration in iterations:
    begin = datetime.datetime.now()
    for i in range(iteration):
        run_cython.image_transformation()
    python_d = abs(begin - datetime.datetime.now())

    begin = datetime.datetime.now()
    for i in range(iteration):
        run_python.image_transformation()
    cython_d = abs(begin - datetime.datetime.now())

    msg = '{}, {}, {}, {}'.format(datetime.datetime.now(), python_d, cython_d,
                                  iteration)

    logging.info(msg)

