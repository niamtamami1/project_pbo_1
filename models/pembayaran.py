from datetime import date
from models.penyewa import Penyewa
from models.kamar import Kamar

class Pembayaran:
    def __init__(self, id_pembayaran: str, penyewa: Penyewa, kamar: Kamar, jumlah: float):
        self.__id_pembayaran = id_pembayaran
        self.__tgl_bayar = date.today()
        self.__penyewa = penyewa
        self.__kamar = kamar
        self.__jumlah = jumlah
        self.__status_verifikasi = False

    def verifikasi_pembayaran(self) -> None:
        self.__status_verifikasi = True
        self.__kamar.set_status(False)  # Ubah status kamar jadi terisi

    def cetak_kuitansi(self) -> None:
        status = "LUNAS / TERVERIFIKASI" if self.__status_verifikasi else "MENUNGGU VERIFIKASI"
        print("\n=== KUITANSI PEMBAYARAN KOS ===")
        print(f"ID Transaksi : {self.__id_pembayaran}")
        print(f"Tanggal      : {self.__tgl_bayar}")
        print(f"Penyewa      : {self.__penyewa.nama}")
        print(f"Kamar        : {self.__kamar.nomor_kamar}")
        print(f"Total Bayar  : Rp {self.__jumlah:,.0f}")
        print(f"Status       : {status}")
        print("===============================\n")