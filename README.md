# Tổng quan về Web Crawler

Dự án này cung cấp cái nhìn tổng quan về việc thu thập dữ liệu từ web (crawler data) bằng Python. Nó bao gồm các ví dụ về cách lấy dữ liệu từ một trang web và lưu trữ thông tin ở các định dạng khác nhau như CSV, JSON hoặc cơ sở dữ liệu quan hệ (MySQL, PostgreSQL). README này nhằm giúp bạn hiểu những kiến thức cơ bản về web crawling và cung cấp mẫu mã cho các dự án của riêng bạn.

## Web Crawling là gì?

Web crawling, hay còn gọi là web scraping, là quá trình tự động truy cập các trang web, đọc nội dung HTML của chúng và thu thập thông tin cụ thể. Kỹ thuật này thường được sử dụng trong các tác vụ như khai thác dữ liệu, so sánh giá cả hoặc thu thập dữ liệu cho các dự án phân tích hoặc học máy.

### Các ứng dụng phổ biến

- Thu thập dữ liệu từ các trang tin tức để phân tích cảm xúc.
- Lấy thông tin sản phẩm từ các trang thương mại điện tử.
- Thu thập dữ liệu mạng xã hội để phân tích xu hướng.
- Trích xuất bài báo khoa học hoặc các bài viết trên blog cho mục đích nghiên cứu.

## Các thư viện thường dùng trong Web Crawling

Để thực hiện web crawling bằng Python, các thư viện sau thường được sử dụng:

1. **`requests`**: Thư viện này được sử dụng để gửi các yêu cầu HTTP đến trang web và nhận nội dung HTML.
2. **`BeautifulSoup`**: Dùng để phân tích cú pháp HTML và XML, giúp dễ dàng trích xuất thông tin từ trang web.
3. **`pandas`**: Một thư viện mạnh mẽ để thao tác và lưu trữ dữ liệu dưới dạng CSV hoặc Excel.
4. **`Selenium`** (tùy chọn): Dùng để crawling các trang web yêu cầu render JavaScript. Selenium tự động hóa các trình duyệt để tải các trang động.

## Cách thiết lập

Trước khi bắt đầu một dự án web scraping, hãy chắc chắn rằng bạn đã cài đặt Python, sau đó cài đặt các thư viện cần thiết.

### Cài đặt

Cài đặt các thư viện Python cần thiết bằng `pip`:

```bash
pip install requests beautifulsoup4 pandas
