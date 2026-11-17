from models.user import User

class Admin(User):
    def __init__(self, id_user: str, nama: str, username: str, password: str, kode_admin: str):
        super().__init__(id_user, nama, username, password)
        self.__kode_admin = kode_admin

    def tampilkan_role(self) -> str:
        return f"Admin Sistem (Kode: {self.__kode_admin})"