class Kamar:
    def __init__(self, id_kamar: str, nomor_kamar: str, harga: float, status_tersedia: bool = True):
        self.__id_kamar = id_kamar            # Private attribute[cite: 4, 6]
        self.__nomor_kamar = nomor_kamar
        self.__harga = harga
        self.__status_tersedia = status_tersedia

    @property
    def id_kamar(self) -> str:
        return self.__id_kamar

    @property
    def nomor_kamar(self) -> str:
        return self.__nomor_kamar

    @property
    def harga(self) -> float:
        return self.__harga

    @harga.setter
    def harga(self, nilai_baru: float) -> None:
        if nilai_baru > 0:
            self.__harga = nilai_baru
        else:
            raise ValueError("Harga kamar harus lebih dari 0!")

    @property
    def status_tersedia(self) -> bool:
        return self.__status_tersedia

    def set_status(self, status: bool) -> None:
        self.__status_tersedia = status