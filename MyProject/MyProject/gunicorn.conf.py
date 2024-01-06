# gunicorn.conf.py

import multiprocessing

bind = "0.0.0.0:8000"  # Use the appropriate host and port
workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() * 2
