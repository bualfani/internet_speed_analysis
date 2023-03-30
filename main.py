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

# loop to collect data points
for i in range(num_points):
    download_speed = st.download()/ 1_000_000
    upload_speed = st.upload() / 1_000_000
    current_time = time.strftime("%H:%M:%S", time.localtime())
    times.append(current_time)
    download_speed.append(download_speed)
    upload_speed.append(upload_speed)
    # pause for 5 seconds between datat points
    time.sleep(5)

# plot data
plt.plot(time, download_speed, label="Download Speed (Mbps)")
plt.plot(times, upload_speed, label="Download Speed (Mbps)")
plt.legend()
plt.xlabel('Time')
plt.ylabel("Speed (Mbps)")
plt.title("Internet Speed Test")
plt.show()