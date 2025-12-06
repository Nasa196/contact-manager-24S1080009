contacts = []

def add_contact():
    print("\n--- THÊM LIÊN HỆ MỚI ---")
    name = input("Nhập tên: ")
    phone = input("Nhập số điện thoại: ")
    email = input("Nhập email: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contacts.append(contact)
    print(f"Đã thêm liên hệ '{name}' thành công!")