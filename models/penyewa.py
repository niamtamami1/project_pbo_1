from models.user import User

class Penyewa(User):
    def __init__(self, id_user: str, nama: str, username: str, password: str, kontak_darurat: str, pekerjaan: str):
        super().__init__(id_user, nama, username, password)
        self.__kontak_darurat = kontak_darurat
        self.__pekerjaan = pekerjaan

    def tampilkan_role(self) -> str:
        return f"Penyewa Kos ({self.__pekerjaan})"