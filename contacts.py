phonebook = []

def main():
    while True:
        print("\n--- DANH BẠ ĐIỆN THOẠI ---")
        print("1. Thêm liên hệ")
        print("2. Xem danh bạ")
        print("3. Tìm kiếm")
        print("4. Thoát")
        
        choice = input("Chọn chức năng: ")
        
        if choice == '4':
            print("Tạm biệt!")
            break
        else:
            print("Chức năng đang phát triển...")

if __name__ == "__main__":
    main()