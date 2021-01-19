# Xử lý lưu trữ===================================
from pathlib import Path
import json
Thu_muc_Du_lieu=Path("..\\Du_lieu")
Thu_muc_HTML=Thu_muc_Du_lieu/"HTML"
Thu_muc_Nhan_vien=Thu_muc_Du_lieu/"Nhan_vien"

def Doc_Khung_HTML():
    Chuoi_HTML=""
    Duong_dan=Thu_muc_HTML/"Khung.html"
    Chuoi_HTML=Duong_dan.read_text("utf-8")
    return Chuoi_HTML

def Doc_Danh_sach_Nhan_vien():
    Danh_sach=[]
    for Duong_dan in Thu_muc_Nhan_vien.glob("*.json"):
        Chuoi_JSON=Duong_dan.read_text("utf-8")
        Doi_tuong=json.loads(Chuoi_JSON)
        Danh_sach.append(Doi_tuong)
    return Danh_sach


# Xử lý nghiệp vụ===================================

def Tra_cuu_Nhan_vien(Danh_sach, Chuoi_Tra_cuu):
    Danh_sach_Kq=[]
    Chuoi_Tra_cuu=Chuoi_Tra_cuu.upper()
    for Nhan_vien in Danh_sach:
        Ho_ten=Nhan_vien["Ho_ten"].upper()
        Thoa_Dieu_kien=Chuoi_Tra_cuu in Ho_ten
        if Thoa_Dieu_kien:
            Danh_sach_Kq.append(Nhan_vien)
    return Danh_sach_Kq

def Tao_Chuoi_HTML_Nhap_Chuoi_Tra_cuu_Nhan_vien(Chuoi_Tra_cuu=""):
    Chuoi_HTML=f"""<div style='background-color:gray;margin:10px'>
                    <div class='btn'>
                        <form action='/NHAN_VIEN/Tra_cuu' method='post'>
                            <input name='Th_Chuoi_Tra_cuu' value='{Chuoi_Tra_cuu}' autocomplete='off'/>
                        </form>
                    </div>
                    </div>"""
    return Chuoi_HTML

def Tao_Chuoi_HTML_Danh_sach_Nhan_vien(Danh_sach):
    Chuoi_HTML_Danh_Sach=f"""<div class='row';style='margin:10px'>"""
    for Nhan_vien in Danh_sach:
        Chuoi_Hinh=f"""<img src='/Media/{Nhan_vien['Ma_so']}.png' style='width:60px;height:60px' />"""
        Chuoi_Thong_tin=f"""<div class='btn' style='text-align:left'>
                                Mã số nhân viên:{Nhan_vien['Ma_so']} 
                                <br />Họ và tên:\t {Nhan_vien['Ho_ten']}
                                <br />Giới tính:\t {Nhan_vien['Gioi_tinh']}
                                <br />Đơn vị:\t {Nhan_vien['Don_vi']['Ten']}
                                     
                            </div>""" 
        Chuoi_HTML=f"""<div class='col-md-3' >
                            {Chuoi_Hinh}  {Chuoi_Thong_tin}
                    </div>"""
        Chuoi_HTML_Danh_Sach+=Chuoi_HTML
    return Chuoi_HTML_Danh_Sach
