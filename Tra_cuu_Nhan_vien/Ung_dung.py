from XL_3L import *

from flask import Flask, request


Ung_dung=Flask(__name__, static_url_path="/Media", static_folder="..\\Media")
# Khai báo biến toàn cục
Khung_HTML=Doc_Khung_HTML()
Danh_sach_Nhan_vien=Doc_Danh_sach_Nhan_vien()
@Ung_dung.route("/")
def XL_Khoi_dong():
    Chuoi_HTML=Tao_Chuoi_HTML_Nhap_Chuoi_Tra_cuu_Nhan_vien()+Tao_Chuoi_HTML_Danh_sach_Nhan_vien(Danh_sach_Nhan_vien)
    Chuoi_HTML=Khung_HTML.replace("Chuoi_HTML", Chuoi_HTML)
    return Chuoi_HTML

@Ung_dung.route("/NHAN_VIEN/Tra_cuu", methods=["POST"])
def XL_Tra_cuu_Nhan_vien():
    Chuoi_Tra_cuu=request.form.get("Th_Chuoi_Tra_cuu")
    Danh_sach_Nhan_vien_Xem=Tra_cuu_Nhan_vien(Danh_sach_Nhan_vien,Chuoi_Tra_cuu)
    Chuoi_HTML=Tao_Chuoi_HTML_Nhap_Chuoi_Tra_cuu_Nhan_vien(Chuoi_Tra_cuu)+Tao_Chuoi_HTML_Danh_sach_Nhan_vien(Danh_sach_Nhan_vien_Xem)
    Chuoi_HTML=Khung_HTML.replace("Chuoi_HTML",Chuoi_HTML)
    return Chuoi_HTML
