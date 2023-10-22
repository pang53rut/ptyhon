# Impor pustaka yang dibutuhkan
import time
import psutil
import plotly.graph_objects as go

# Buat variabel untuk menyimpan data bandwidth
bandwidth_data = {"time": [], "upload": [], "download": []}

# Buat fungsi untuk mengubah byte menjadi megabit
def convert_to_mbit(value):
    return value / 1024 / 1024 * 8

# Buat fungsi untuk mengirim data bandwidth ke plotly
def send_data():
    # Buat objek grafik garis dengan data bandwidth
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=bandwidth_data["time"], y=bandwidth_data["upload"], mode="lines", name="Upload"))
    fig.add_trace(go.Scatter(x=bandwidth_data["time"], y=bandwidth_data["download"], mode="lines", name="Download"))

    # Atur judul dan label sumbu grafik
    fig.update_layout(title="Bandwidth Monitor", xaxis_title="Time", yaxis_title="Speed (Mbps)")

    # Tampilkan grafik di browser
    fig.show()

# Tentukan interval waktu dalam detik
interval = 1

# Tentukan durasi pengukuran dalam detik
duration = 10

# Tentukan waktu mulai pengukuran
start_time = time.time()

# Ulangi pengukuran selama durasi yang ditentukan
while time.time() - start_time < duration:
    # Dapatkan jumlah byte yang dikirim dan diterima pada waktu sekarang
    net1 = psutil.net_io_counters()

    # Tunggu selama interval waktu
    time.sleep(interval)

    # Dapatkan jumlah byte yang dikirim dan diterima pada waktu berikutnya
    net2 = psutil.net_io_counters()

    # Hitung kecepatan upload dan download dalam megabit per detik
    upload = convert_to_mbit(net2.bytes_sent - net1.bytes_sent) / interval
    download = convert_to_mbit(net2.bytes_recv - net1.bytes_recv) / interval

    # Cetak kecepatan upload dan download di konsol
    print(f"Upload: {upload:.2f} Mbps, Download: {download:.2f} Mbps")

    # Simpan data bandwidth ke variabel
    bandwidth_data["time"].append(time.strftime("%H:%M:%S"))
    bandwidth_data["upload"].append(upload)
    bandwidth_data["download"].append(download)

# Kirim data bandwidth ke plotly untuk divisualisasikan
send_data()