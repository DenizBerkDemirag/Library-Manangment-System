import sqlite3
import os
from typing import Tuple, List

from PyQt5.QtWidgets import QMessageBox


class Veritabani():
    def __init__(self):
        self.dizin = os.path.dirname(os.path.abspath(__file__))
        self.vt_yol = os.path.join(self.dizin, 'Library.db')
    def baglanti_ac(self):
        try:
            self.con = sqlite3.connect(self.vt_yol)
            self.cursor = self.con.cursor()
        except:
            print("Veritabanı baglantı hatası")
    def baglanti_kapat(self):
        self.con.close()

    def kitap_yazdir(self):
        self.baglanti_ac()
        self.cursor.execute("SELECT * FROM kitap ORDER BY kategori_adi")
        veriler = self.cursor.fetchall()
        self.baglanti_kapat()
        return veriler

    def kitap_arama(self, arama):
        self.baglanti_ac()
        self.cursor.execute("SELECT * FROM kitap WHERE kitap_adi LIKE ?",(f"%{arama}%",))
        veriler = self.cursor.fetchall()
        self.baglanti_kapat()
        return veriler

    def kategori_yazdir(self, kategori_adi):
        self.baglanti_ac()
        self.cursor.execute(
            "SELECT * FROM kitap WHERE kategori_adi = ?",
            (kategori_adi,)
        )
        veriler = self.cursor.fetchall()
        self.baglanti_kapat()
        return veriler

    def kategori_arama_yap(self, kategori_adi, arama):
        self.baglanti_ac()
        self.cursor.execute(
            "SELECT * FROM kitap WHERE kategori_adi = ? AND kitap_adi LIKE ?",
            (kategori_adi, f"%{arama}%")
        )
        veriler = self.cursor.fetchall()
        self.baglanti_kapat()
        return veriler

    def kayit_yap(self , kitap_adi,kategori_adi , yazar , yayinlanma , stok):
        self.baglanti_ac()
        self.cursor.execute(
            "INSERT INTO kitap(kitap_adi, kategori_adi, yazar, yayinlanma, var_mı) VALUES(?,?,?,?,?)",(kitap_adi, kategori_adi, yazar, yayinlanma, stok)
        )
        sonuc = self.cursor.rowcount
        self.con.commit()
        self.baglanti_kapat()
        if sonuc > 0:
            return True
        return False

    def guncelleme_yap(self,id,a,b,c,d,e):

        if not all([a, b, c, d, e]):
            QMessageBox.warning(
                self,
                "Eksik Bilgi",
                "Lütfen tüm sütunları doldurunuz."
            )
            return

        self.baglanti_ac()

        self.cursor.execute("UPDATE kitap SET kitap_adi    = ?, kategori_adi = ?,yazar        = ?,yayinlanma   = ?,var_mı       = ? WHERE kitap_id = ?", (a, b, c, d, e, id))

        sonuc = self.cursor.rowcount
        self.con.commit()
        self.baglanti_kapat()

        if sonuc > 0:
            return True
        return False

    def kayit_sil(self,kitap_id):
        self.baglanti_ac()
        self.cursor.execute("DELETE FROM kitap WHERE kitap_id = ?", (kitap_id,))
        sonuc = self.cursor.rowcount
        self.con.commit()
        self.baglanti_kapat()

        if sonuc > 0:
            return True
        return False

    def giris_kontrol(self, kullanici_id, sifre):
        self.baglanti_ac()
        self.cursor.execute(
            """
            SELECT 1
            FROM user
            WHERE user_id = ? COLLATE BINARY
              AND sifre = ? COLLATE BINARY
            LIMIT 1
            """,
            (kullanici_id, sifre)
        )
        row = self.cursor.fetchone()
        self.baglanti_kapat()

        if row:
            return True
        else:
            return False

    def admin_giris_kontrol(self, kullanici_id, sifre):
        self.baglanti_ac()
        self.cursor.execute(
            """
            SELECT 1
            FROM admin
            WHERE admin_id = ? COLLATE BINARY
              AND sifre = ? COLLATE BINARY
            LIMIT 1
            """,
            (kullanici_id, sifre)
        )
        row = self.cursor.fetchone()
        self.baglanti_kapat()

        if row:
            return True
        else:
            return False

    def uye_kayit_yap(self , id , password):
        self.baglanti_ac()
        self.cursor.execute("INSERT INTO user(user_id, sifre) VALUES (?,?)",(id,password))
        sonuc = self.cursor.rowcount
        self.con.commit()
        self.baglanti_kapat()
        if sonuc > 0:
            return True
        return False

    def Id_kontrol(self,id):
        self.baglanti_ac()
        self.cursor.execute("SElECT 1 FROM user WHERE user_id = ? LIMIT 1", (id,))
        row = self.cursor.fetchone()
        self.baglanti_kapat()
        if row:
            return True
        else:
            return False

    def engel_kontrol(self,id):
        self.baglanti_ac()
        self.cursor.execute("select 1 from user where user_id = ? and engel_mi = 1 LIMIT 1", (id,))
        row = self.cursor.fetchone()
        self.baglanti_kapat()
        if row:
            return True
        return False

    def engelle(self,id):
        self.baglanti_ac()
        self.cursor.execute("update user set engel_mi = 1 where user_id = ?",(id,))
        self.con.commit()
        sonuc = self.cursor.rowcount
        self.baglanti_kapat()
        if sonuc>0:
            return True
        return False

    def engel_ac(self,id):
        self.baglanti_ac()
        self.cursor.execute("update user set engel_mi = 0 where user_id = ?",(id,))
        self.con.commit()
        sonuc = self.cursor.rowcount
        self.baglanti_kapat()
        if sonuc>0:
            return True
        return False

    def kullanici_yükle(self):
        self.baglanti_ac()
        self.cursor.execute("SELECT * FROM user")
        veriler = self.cursor.fetchall()
        self.baglanti_kapat()
        return veriler

    def kullanici_sil(self,id):
        self.baglanti_ac()
        self.cursor.execute("DELETE FROM user WHERE user_id = ?", (id,))
        sonuc = self.cursor.rowcount
        self.con.commit()
        self.baglanti_kapat()
        if sonuc > 0:
            return True
        return False

    def kullanici_arama(self,arama):
        self.baglanti_ac()
        self.cursor.execute("select * from user where user_id like ?", (f"%{arama}%",))
        veriler = self.cursor.fetchall()
        self.baglanti_kapat()
        return veriler

    def get_all_masalar(self) -> List[Tuple]:
        self.baglanti_ac()
        self.cursor.execute("""
            SELECT masa_id, dolu_mu, bilgisayarli_mi
            FROM masa
            ORDER BY masa_id
        """)
        veriler = self.cursor.fetchall()
        self.baglanti_kapat()
        return veriler

    def get_dolu_masalar(self) -> List[int]:

        self.baglanti_ac()
        self.cursor.execute("""
            SELECT masa_id
            FROM masa
            WHERE dolu_mu = 1
            ORDER BY masa_id
        """)
        rows = self.cursor.fetchall()
        self.baglanti_kapat()
        return [row[0] for row in rows]

    def update_masa_durumu(self, masa_id: int, dolu_mu: bool):
        self.baglanti_ac()
        self.cursor.execute("""
            UPDATE masa
            SET dolu_mu = ?
            WHERE masa_id = ?
        """, (int(dolu_mu), masa_id))

        self.con.commit()
        self.baglanti_kapat()

    def update_all_masa_durumlari(self, dolu_masalar: List[int]):

        self.baglanti_ac()
        self.cursor.execute("UPDATE masa SET dolu_mu = 0")

        for masa_id in dolu_masalar:
            self.cursor.execute("""
                UPDATE masa
                SET dolu_mu = 1
                WHERE masa_id = ?
            """, (masa_id,))

        self.con.commit()
        self.baglanti_kapat()

    def get_occupancy_counts(self) -> Tuple[int, int]:
        self.baglanti_ac()
        self.cursor.execute("SELECT COUNT(*) FROM masa")
        total = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT COUNT(*) FROM masa WHERE dolu_mu = 1")
        occupied = self.cursor.fetchone()[0]
        self.baglanti_kapat()
        return total, occupied

    def siparis_bilgiler(self,kullanici_id,kitap_id,adress,tarih,tarih_ver,durum):
        self.baglanti_ac()
        self.cursor.execute("""
                            INSERT INTO siparis
                                (user_id, kitap_id, adres, tarih_al, tarih_ver, durum)
                            VALUES (?, ?, ?, ?, ?, ?)
                            """, (kullanici_id, kitap_id, adress, tarih, tarih_ver, durum))
        sonuc = self.cursor.rowcount
        self.con.commit()
        self.baglanti_kapat()
        if sonuc > 0:
            return True
        return False

    def siparis_doldur(self):
        self.baglanti_ac()
        self.cursor.execute("select * from siparis order by tarih_ver asc")
        veriler = self.cursor.fetchall()
        self.baglanti_kapat()
        return veriler

    def siparis_tamamla(self,id_siparis):
        self.baglanti_ac()
        self.cursor.execute(""" UPDATE siparis
                                    SET durum = 'Tamamlandı'
                                    WHERE siparis_id = ?""", (id_siparis,))
        sonuc = self.cursor.rowcount
        self.con.commit()
        self.baglanti_kapat()
        if sonuc > 0:
            return True
        return False

    def siparis_kontrol(self,id_kullanici,id_kitap):
        self.baglanti_ac()
        kullanici_var = self.cursor.execute("select 1 from user where user_id = ?", (id_kullanici,)).fetchone()
        kitap_var = self.cursor.execute("select 1 from kitap where kitap_id = ?", (id_kitap,)).fetchone()
        self.baglanti_kapat()
        if kullanici_var and kitap_var:
            return True
        return False