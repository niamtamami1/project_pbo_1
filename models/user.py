from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, id_user: str, nama: str, username: str, password: str):
        self._id_user = id_user        # Protected attribute
        self._nama = nama
        self._username = username
        self._password = password

    @property
    def id_user(self) -> str:
        return self._id_user

    @property
    def nama(self) -> str:
        return self._nama

    def login(self) -> bool:
        print(f"[{self._username}] {self._nama} berhasil login.")
        return True

    def logout(self) -> None:
        print(f"[{self._username}] {self._nama} telah logout.")

    @abstractmethod
    def tampilkan_role(self) -> str:   # Wajib di-override oleh subclass
        pass