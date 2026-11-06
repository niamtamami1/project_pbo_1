from .user import User

class Penyewa(User):
    def __init__(self, id_user, nama, email, no_hp, id_kamar):
        super().__init__(id_user, nama, email, no_hp)
        self.id_kamar = id_kamar
        self.status_aktif = True

    def tampilkan_profil(self):
        # Overriding method dari parent class
        return f"Penyewa: {self.nama} | Kamar: {self.id_kamar} | HP: {self.no_hp}"