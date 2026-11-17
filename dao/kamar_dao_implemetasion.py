from typing import List, Optional
from contextlib import closing
from dao.kamar_dao import KamarDAO
from models.kamar import Kamar

class KamarDAOImpl(KamarDAO):
    def insert(self, k: Kamar) -> None:
        sql = "INSERT INTO kamar (id_kamar, nomor_kamar, harga, status_tersedia) VALUES (%s, %s, %s, %s)"
        with closing(DatabaseConnection.get_connection()) as conn:
            with closing(conn.cursor()) as cur:
                cur.execute(sql, (k.id_kamar, k.nomor_kamar, k.harga, k.status_tersedia))
                conn.commit()

    def update(self, k: Kamar) -> None:
        sql = "UPDATE kamar SET nomor_kamar=%s, harga=%s, status_tersedia=%s WHERE id_kamar=%s"
        with closing(DatabaseConnection.get_connection()) as conn:
            with closing(conn.cursor()) as cur:
                cur.execute(sql, (k.nomor_kamar, k.harga, k.status_tersedia, k.id_kamar))
                conn.commit()

    def delete(self, id_kamar: str) -> None:
        sql = "DELETE FROM kamar WHERE id_kamar=%s"
        with closing(DatabaseConnection.get_connection()) as conn:
            with closing(conn.cursor()) as cur:
                cur.execute(sql, (id_kamar,))
                conn.commit()

    def find_by_id(self, id_kamar: str) -> Optional[Kamar]:
        sql = "SELECT id_kamar, nomor_kamar, harga, status_tersedia FROM kamar WHERE id_kamar=%s"
        with closing(DatabaseConnection.get_connection()) as conn:
            with closing(conn.cursor()) as cur:
                cur.execute(sql, (id_kamar,))
                row = cur.fetchone()
                if row is None:
                    return None
                return Kamar(row[0], row[1], float(row[2]), bool(row[3]))

    def find_all(self) -> List[Kamar]:
        sql = "SELECT id_kamar, nomor_kamar, harga, status_tersedia FROM kamar"
        with closing(DatabaseConnection.get_connection()) as conn:
            with closing(conn.cursor()) as cur:
                cur.execute(sql)
                return [Kamar(id_k, no_k, float(hrg), bool(sts))
                        for (id_k, no_k, hrg, sts) in cur.fetchall()]