import cv2
import os

# Inisialisasi kamera
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set lebar video
cam.set(4, 480)  # set tinggi video

# Load pre-trained Haar Cascade classifier for face detection
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Memasukkan informasi pengguna
user_id = input('\n Masukkan ID pengguna dan tekan <Enter> ==>  ')

# Tentukan jumlah wajah yang akan ditangkap
face_samples = 30
count = 0

# Buat direktori dataset jika belum ada
dataset_dir = 'dataset'
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

print("\n [INFO] Memulai pengambilan wajah. Lihat kamera dan tunggu ...")

while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)  # Flip video secara horizontal
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1

        # Simpan gambar wajah yang ditangkap di direktori dataset
        cv2.imwrite(f"{dataset_dir}/User.{user_id}.{count}.jpg", gray[y:y + h, x:x + w])

        cv2.imshow('Wajah', img)

    k = cv2.waitKey(100) & 0xff  # Tekan 'ESC' untuk keluar dari pengambilan gambar
    if k == 27:
        break
    elif count >= face_samples:
        break

# Membersihkan
print("\n [INFO] Keluar dari program dan membersihkan ...")
cam.release()
cv2.destroyAllWindows()
