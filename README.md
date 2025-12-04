# Hướng dẫn sử dụng hệ thống chấm điểm

Hệ thống chấm điểm được thiết kế để kiểm tra và đánh giá các bài tập lập trình. Dưới đây là các bước để sử dụng hệ thống:

## 1. Cấu trúc thư mục
Hệ thống yêu cầu cấu trúc thư mục như sau:
- **Description.md**: File mô tả yêu cầu và hướng dẫn cho từng bài tập.
- **Data/**: Chứa các dữ liệu cần thiết cho bài tập (ví dụ: `tips.json`, `titanic.csv`, ...).
- **Input/**: Chứa các file đầu vào cho từng bài tập.
  - Ví dụ: `Input/Tips3/1.in`, `Input/Tips3/2.in`, ...
- **Output/**: Chứa các file đầu ra mong muốn tương ứng với từng bài tập.
  - Ví dụ: `Output/Tips3/1.out`, `Output/Tips3/2.out`, ...
- **grader.py**: File chính để chạy hệ thống chấm điểm.

## 2. Cách chạy hệ thống
1. Chạy môi trường ảo có sẵn trong thư mục `venv`:
   ```bash
   source venv/bin/activate
   ```

2. Mở terminal và điều hướng đến thư mục chứa file `grader.py`:
    - Ví dụ:
        ```bash
        cd /home/ngtukien/Documents/D23CT01_Python/Tools
        ```

3. Chạy lệnh sau để chấm điểm cho một bài tập cụ thể:
   ```bash
   python3 grader.py <Tên_Bài_Tập>
   ```
   - Ví dụ: Để chấm bài tập `Tips3`, chạy lệnh:
        ```bash
        python3 grader.py Tips3
        ```

3. Kết quả sẽ được hiển thị trên terminal, bao gồm số lượng test case đúng và sai.

## 3. Lưu ý
- Đảm bảo các file đầu vào và đầu ra được đặt đúng thư mục và đúng định dạng.
- Đọc kỹ file `Description.md` để hiểu yêu cầu của từng bài tập.
- Nếu có lỗi, kiểm tra lại logic trong bài làm hoặc cấu trúc thư mục.

## 4. Thông tin thêm
- Nên `fork` repository này để lưu trữ và quản lý bài làm của bạn, sau đó `clone` về máy cá nhân để làm việc.
- Nếu có lỗi, hãy mở `pull request` để đóng góp sửa lỗi cho hệ thống.