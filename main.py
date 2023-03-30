import speedtest
import matplotlib.pyplot as plt
import time

# create speedtest client
st = speedtest.Speedtest()

# empty list to store data
times = []
upload_speed = []
download_speed = []

# number of data points to collect
num_points = 10