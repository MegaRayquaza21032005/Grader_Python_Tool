Dưới đây là nội dung từ các hình ảnh bạn cung cấp, được chuyển đổi sang định dạng Markdown, chia làm 3 bài toán riêng biệt:

-----

# Tips1 (Thống kê theo giới tính và tình trạng hút thuốc)

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
      // ...
    }
  ]
}
```

**Mô tả các trường:**

  * **total\_bill:** tổng số chi
  * **tip:** tiền bo
  * **sex:** giới tính (**Male** hoặc **Female**)
  * **smoker:** hút thuốc hoặc không hút (**Yes** hoặc **No**)
  * **day:** ngày trong tuần
  * **time:** buổi trong ngày
  * **size:** số người có trên bàn ăn

### Yêu cầu:

Đọc từ file json và đưa ra các chỉ số thống kê (**sum**, **avg**, **max**, **min**) về tổng tiền hóa đơn (**total\_bill**) theo yêu cầu đề bài.

**Input:**

  * Dòng đầu đưa vào số bộ test.
  * Lần lượt đưa vào giới tính và trạng thái hút thuốc.

**Output:**

  * Đưa ra 1 dòng gồm các chỉ số thống kê. Các số thập phân lấy **4 chữ số** sau dấu phẩy.

**Ví dụ:**

| Input | Output |
| :--- | :--- |
| 1 | |
| Male No | 1919.7500 19.7912 48.3300 7.5100 |

-----

# Tips3 (Thống kê theo ngày và số người)

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
      // ...
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

### Yêu cầu:

Đọc từ file csv đưa ra giá trị hóa đơn trung bình (**total\_bill**) theo ngày và số người trên bàn ăn.

**Input:**

  * Dòng đầu tiên đưa vào số bộ test.
  * Dòng thứ 2 ghi ngày và số người trên bàn ăn cách nhau **1 khoảng trắng**.

**Output:**

  * Đưa ra giá trị trung bình của tổng hóa đơn (**total\_bill**). Các giá trị thập phân cách nhau bởi **1 khoảng trắng**.
  * Nếu không có dữ liệu phù hợp, in ra **Invalid**.

**Ví dụ:**

| Input | Output |
| :--- | :--- |
| 2 | |
| Sun 2 | 17.5600 |
| Fri 10 | Invalid |

-----

# Flight_year (Thống kê theo năm)

Dữ liệu về chuyến bay được lưu trữ trong tệp **"flights.json"** có cấu trúc từ điển lồng nhau bao gồm:

  * Ngoài cùng là từ điển có khóa là **`flights`**.
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
    // ...
  ]
}
```

Trong đó giá trị của khóa **`year`** là năm thống kê, giá trị của khóa **`month`** là tháng thống kê, giá trị của khóa **`passagers`** là số hành khách chở được tương ứng.

### Yêu cầu:

Đọc dữ liệu từ file JSON và in ra các thông tin thống kê theo năm.

**INPUT:**

  * Dòng đầu là **số bộ Test**.
  * Các dòng tiếp theo, mỗi dòng ghi **số năm** và **chỉ số cần thống kê** (**min**, **max**, **sum**, **avg**).

**OUTPUT:**

  * In ra giá trị tính được. Nếu giá trị là dạng float thì in ra **làm tròn đến 5 chữ số** sau dấu phẩy.
  * Nếu không có dữ liệu phù hợp, in ra **Invalid**.

**Ví dụ:**

| Input | Output |
| :--- | :--- |
| 2 |  |
| 1959 sum | 5140 |
| 1950 avg | 139.66667 |