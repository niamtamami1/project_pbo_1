from models.admin import Admin
from models.pemilik import Pemilik
from models.penyewa import Penyewa
from models.kamar import Kamar
from models.pembayaran import Pembayaran
from dao.kamar_dao_implemetasion import KamarDAOImpl

# 1. Instansiasi Objek Pengguna[cite: 6, 9]
admin = Admin("U01", "Rina", "admin_rina", "pass1", "ADM-01")
pemilik = Pemilik("U02", "Pak Budi", "budi_kos", "pass2", "11223344", "BCA")
penyewa = Penyewa("U03", "Sari", "sari_mhs", "pass3", "081234567", "Mahasiswa")

# Demonstrasi Polimorfisme[cite: 6]
print("--- DAFTAR PENGGUNA SISTEM ---")
for u in [admin, pemilik, penyewa]:
    print(f"{u.nama} -> {u.tampilkan_role()}")
print("-" * 35)

# 2. Alur Penyewaan & Pembayaran (Terjemahan Activity Diagram)[cite: 4]
kamar_a1 = Kamar("K01", "A-01", 1500000, True)

penyewa.login()
if kamar_a1.status_tersedia:
    print(f"Kamar {kamar_a1.nomor_kamar} tersedia. Mengajukan sewa...")
    transaksi = Pembayaran("TRX-001", penyewa, kamar_a1, kamar_a1.harga)
    transaksi.cetak_kuitansi()
    pemilik.login()
    transaksi.verifikasi_pembayaran()
    transaksi.cetak_kuitansi()
else:
    print("Maaf, kamar sudah terisi.")

