# Tips3
Tips là dữ liệu về tiền bo (tips) cho nhà hàng bao gồm danh sách các từ điển cho mỗi bàn bao gồm các trường:

```json
{
  "tips": [
    {
      "total_bill": "16.99",
      "tip": "1.01",
      "sex": "Female",
      "smoker": "No",
      "day": "Sun",
      "time": "Dinner",
      "size": "2"
    },
    {
      "total_bill": "10.34",
      "tip": "1.66",
      "sex": "Male",
      "smoker": "No",
      ...
    }
  ]
}
```

**Mô tả các trường:**

  * **total\_bill:** tổng số chi
  * **tip:** tiền bo
  * **sex:** giới tính
  * **smoker:** hút thuốc hoặc không hút
  * **day:** ngày trong tuần
  * **time:** buổi trong ngày
  * **size:** số người có trên bàn ăn

## Yêu cầu:

Đọc từ file csv đưa ra giá trị hóa đơn trung bình (total\_bill) theo ngày và số người trên bàn ăn.

**Input:**

  * Dòng đầu tiên đưa vào số bộ test.
  * Dòng thứ 2 ghi ngày và số người trên bàn ăn cách nhau 1 khoảng trắng.

**Output:**

  * Đưa ra giá trị trung bình của tổng hóa đơn (total\_bill). Các giá trị thập phân cách nhau bởi 1 khoảng trắng.

**Ví dụ:**

| Input | Output |
| :--- | :--- |
| 2<br>Sun 2<br>Fri 10 | 17.5600<br>Invalid |
___
# Flight Year
Dữ liệu về chuyến bay được lưu trữ trong tệp "flights.json" có cấu trúc từ điển lồng nhau bao gồm:

  * Ngoài cùng là từ điển có khóa là `flights`.
  * Giá trị của khóa danh sách các từ điển, mỗi phần tử bao gồm các khóa và giá trị text như hình:

<!-- end list -->

```json
{
  "flights": [
    {
      "year": "1949",
      "month": "January",
      "passengers": "112"
    },
    {
      "year": "1949",
      "month": "February",
      "passengers": "118"
    },
    ...
  ]
}
```

Trong đó giá trị của khóa `year` là năm thống kê, giá trị của khóa `month` là tháng thống kê, giá trị của khóa `passengers` là số hành khách chở được tương ứng.

### Yêu cầu:

Đọc dữ liệu từ file JSON và in ra các thông tin thống kê theo năm.

**INPUT:**

  * Dòng đầu là số bộ Test.
  * Các dòng tiếp theo, mỗi dòng ghi số năm và chỉ số cần thống kê (min, max, sum, avg).

**OUTPUT:**

  * In ra giá trị tính được. Nếu giá trị là dạng float thì in ra làm tròn đến 5 chữ số sau dấu phẩy.

**Ví dụ:**

| Input | Output |
| :--- | :--- |
| 2 |  |
| 1959 sum | 5140 |
| 1950 avg | 139.66667 |