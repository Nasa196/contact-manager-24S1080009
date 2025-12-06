contacts = []

def add_contact():
    print("\n--- THÊM LIÊN HỆ ---")
    name = input("Nhập tên: ")
    phone = input("Nhập SĐT: ")
    email = input("Nhập Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("-> Đã thêm thành công!")

def display_contacts():
    print("\n--- DANH BẠ HIỆN TẠI ---")
    if not contacts:
        print("Danh bạ đang trống.")
    else:
        for i, c in enumerate(contacts, 1):
            print(f"{i}. Tên: {c['name']} | SĐT: {c['phone']} | Email: {c['email']}")

if __name__ == "__main__":
    while True:
        print("\n1. Thêm | 2. Hiển thị | 3. Thoát")
        choice = input("Chọn: ")
        if choice == '1': add_contact()
        elif choice == '2': display_contacts()
        elif choice == '3': break