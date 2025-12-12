from predictor import cek_video_populer




def main():
try:
views_input = int(input("Masukkan jumlah views: "))
likes_input = int(input("Masukkan jumlah likes: "))


hasil = cek_video_populer(views_input, likes_input)


print("\n============================")
print("HASIL PREDIKSI VIDEO")
print("============================")
print(f"Views : {views_input}")
print(f"Likes : {likes_input}")
print(f"Kategori Video : {hasil}")
print("============================\n")


except ValueError:
print("Input tidak valid. Masukkan angka saja.")
except FileNotFoundError as e:
print(e)




if __name__ == "__main__":
main()
