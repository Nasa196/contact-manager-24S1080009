contacts = []

def add_contact():
    print("\n--- THÊM LIÊN HỆ ---")
    name = input("Nhập tên: ")
    phone = input("Nhập SĐT: ")
    email = input("Nhập Email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("-> Đã thêm thành công!")

def display_contacts():
    print("\n--- DANH BẠ HIỆN TẠI ---")
    if not contacts:
        print("Danh bạ đang trống.")
    else:
        for i, c in enumerate(contacts, 1):
            print(f"{i}. Tên: {c['name']} | SĐT: {c['phone']} | Email: {c['email']}")

def search_contact():
    print("\n--- TÌM KIẾM LIÊN HỆ ---")
    keyword = input("Nhập tên cần tìm: ").lower()
    found = False
    
    for c in contacts:
        if keyword in c['name'].lower():
            print(f"-> TÌM THẤY: Tên: {c['name']} - SĐT: {c['phone']}")
            found = True
            
    if not found:
        print("-> Không tìm thấy ai có tên này.")

if __name__ == "__main__":
    while True:
        print("\n=== QUẢN LÝ DANH BẠ ===")
        print("1. Thêm liên hệ")
        print("2. Hiển thị danh bạ")
        print("3. Tìm kiếm")
        print("4. Thoát")
        
        choice = input("Chọn chức năng (1-4): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Tạm biệt!")
            break
        else:
            print("Chọn sai rồi, chọn lại đi!")