from abc import ABC, abstractmethod
from contextlib import closing
from typing import List, Optional

from models.kamar import Kamar
from util.database_conection import DatabaseConnection

class KamarDAO(ABC):
    @abstractmethod
    def insert(self, k: Kamar) -> None: pass

    @abstractmethod
    def update(self, k: Kamar) -> None: pass

    @abstractmethod
    def delete(self, id_kamar: str) -> None: pass

    @abstractmethod
    def find_by_id(self, id_kamar: str) -> Optional[Kamar]: pass

    @abstractmethod
    def find_all(self) -> List[Kamar]: pass


