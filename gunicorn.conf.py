from multiprocessing import cpu_count

timeout = 1800
bind = "0.0.0.0:5000"
workers = cpu_count()
