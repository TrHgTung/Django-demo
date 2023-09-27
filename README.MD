## Mã nguồn web-app quản lý nhập kho sách

@Hoàng-Tùng (TrHgTung) và Neko Team

### Chạy lần đầu (trong cmd):

- Khởi tạo môi trường ảo (virtual env): `python -m venv venv`
- Kích hoạt môi trường ảo: `venv\Scripts\activate.bat`
- Cài đặt Django: `pip install django`
- Khởi tạo project Django, với tên project là mysite: `django-admin startproject mysite`
- Chạy trên cổng 8000 (localhost): `python manage.py runserver 8000`

### Chạy các lần kế tiếp (trong cmd):

- Kích hoạt môi trường ảo: `venv\Scripts\activate.bat`
- Chạy trên cổng 8000 (localhost): `python manage.py runserver`

### Phiên bản:

- Python: 3.10.9
- Django: 4.2.5

### Tạo super-user trong /admin (để quản lý dữ liệu):

- `python manage.py createsuperuser` > Nhập theo hướng dẫn > Ghi nhớ username (uname) và password (pwd) > Truy cập `localhost:<số-port>\admin` > Đăng nhập vào trang admin bằng uname và pwd
