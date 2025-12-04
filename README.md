# Hướng dẫn sử dụng hệ thống chấm điểm

Hệ thống chấm điểm được thiết kế để kiểm tra và đánh giá các bài tập lập trình. Dưới đây là các bước để sử dụng hệ thống:

## 1. Cấu trúc thư mục
Hệ thống yêu cầu cấu trúc thư mục như sau:
- **Input/**: Chứa các file đầu vào cho từng bài tập.
  - Ví dụ: `Input/Tips3/1.in`, `Input/Tips3/2.in`, ...
- **Output/**: Chứa các file đầu ra mong muốn tương ứng với từng bài tập.
  - Ví dụ: `Output/Tips3/1.out`, `Output/Tips3/2.out`, ...
- **grader.py**: File chính để chạy hệ thống chấm điểm.

## 2. Cách chạy hệ thống

1. Chạy muôn trường biên dịch cho Python 3:
   ```bash
   source venv/bin/activate
   ```

2. Mở terminal và điều hướng đến thư mục chứa file `grader.py`:
    Ví dụ:
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
- Mọi thắc mắc hoặc góp ý, vui lòng liên hệ qua email của người quản lý hệ thống.