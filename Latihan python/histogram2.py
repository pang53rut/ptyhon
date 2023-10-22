import matplotlib.pyplot as plt

data = [53, 30.4, 20.5, 3.4, 17.7, 18.5, 21.7, 35.5, 26.7, 26.8, 28.6, 27.6]

plt.hist(data, bins=6, edgecolor='black')  # Jumlah bins dapat disesuaikan
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.title('Histogram Data')
plt.show()
