import requests
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector
import json

# URL của trang SPOJ PTIT
url = "https://www.spoj.com/PTIT/"

# Gửi yêu cầu GET đến trang web
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    # Phân tích nội dung HTML bằng BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Tìm tất cả các bài tập trên trang
    problems = soup.find_all("tr", class_="problemrow")

    # Danh sách để lưu trữ dữ liệu
    data = []

    # Lặp qua các bài tập và trích xuất thông tin
    for problem in problems:
        title = problem.find("td", class_="text-left").get_text().strip()  # Trích xuất tiêu đề bài tập
        link = "https://www.spoj.com" + problem.find("a")["href"]  # Trích xuất link bài tập
        users_solved = problem.find_all("td")[3].get_text().strip()  # Số lượng người đã giải

        # Thêm dữ liệu vào danh sách
        data.append({
            "Tiêu đề": title,
            "Liên kết": link,
            "Số lượng đã giải": users_solved
        })

    # Chuyển danh sách thành DataFrame để lưu vào các định dạng
    df = pd.DataFrame(data)

    # Lưu dữ liệu vào file CSV
    df.to_csv("spoj_ptit.csv", index=False, encoding="utf-8")
    print("Dữ liệu đã được lưu vào spoj_ptit.csv")

    # Lưu dữ liệu vào file Excel
    df.to_excel("spoj_ptit.xlsx", index=False)
    print("Dữ liệu đã được lưu vào spoj_ptit.xlsx")

    # Lưu dữ liệu vào file JSON
    with open("spoj_ptit.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print("Dữ liệu đã được lưu vào spoj_ptit.json")
else:
    print("Không thể truy cập trang web.")

# Kết nối với cơ sở dữ liệu MySQL
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Tên người dùng MySQL
        password="password",  # Mật khẩu MySQL
        database="web_scraping_db"  # Tên cơ sở dữ liệu
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Tạo bảng nếu chưa tồn tại
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS problems (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                link VARCHAR(255),
                users_solved INT
            )
        """)

        # Chèn dữ liệu vào bảng
        for problem in data:
            cursor.execute("""
                INSERT INTO problems (title, link, users_solved)
                VALUES (%s, %s, %s)
            """, (problem["Tiêu đề"], problem["Liên kết"], problem["Số lượng đã giải"]))

        connection.commit()
        print("Dữ liệu đã được lưu vào cơ sở dữ liệu MySQL.")

except mysql.connector.Error as err:
    print(f"Lỗi kết nối MySQL: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Đã đóng kết nối MySQL.")