import matplotlib.pyplot as plt

data = [35, 58, 61, 63, 65, 66, 68, 69, 70, 70, 72, 72, 73, 74, 75, 76, 76, 77, 78, 79, 83, 83, 84, 86, 87, 91]

plt.hist(data, bins=10, edgecolor='black')  # Jumlah bins dapat disesuaikan
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.title('Histogram Data')
plt.show()