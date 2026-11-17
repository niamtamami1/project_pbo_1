from models.user import User

class Pemilik(User):
    def __init__(self, id_user: str, nama: str, username: str, password: str, no_rekening: str, nama_bank: str):
        super().__init__(id_user, nama, username, password)
        self.__no_rekening = no_rekening
        self.__nama_bank = nama_bank

    def tampilkan_role(self) -> str:
        return f"Pemilik Kos ({self.__nama_bank} - {self.__no_rekening})"