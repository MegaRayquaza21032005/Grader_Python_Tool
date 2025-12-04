import os
import subprocess
import sys
import glob

# =================================================================
# 1. Cấu hình & Hằng số
# =================================================================

class Colors:
    """Định nghĩa mã màu ANSI cho output terminal."""
    PASS = '\033[92m'  # Xanh lá
    FAIL = '\033[91m'  # Đỏ
    WARN = '\033[93m'  # Vàng
    RESET = '\033[0m' # Reset về màu mặc định

# Định nghĩa các đường dẫn quan trọng trong cấu trúc thư mục
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, 'Input')
OUTPUT_DIR = os.path.join(BASE_DIR, 'Output')
CODE_DIR = os.path.join(BASE_DIR, 'Code')  # Thư mục chứa bài làm của user

# =================================================================
# 2. Các hàm tiện ích
# =================================================================

def find_script_file(problem_name):
    """
    Tìm file python tương ứng với tên bài trong thư mục Code/.
    Ưu tiên tìm kiếm linh hoạt: [Tên_Bài].py, [tên_bài].py, [tênbài].py
    """
    # Tạo các tên file tiềm năng từ tên thư mục bài toán
    possible_names = [
        f"{problem_name}.py",
        f"{problem_name.lower()}.py",
        f"{problem_name.lower().replace(' ', '').replace('_', '')}.py"
    ]
    
    for name in possible_names:
        # Tìm trong thư mục CODE_DIR
        file_path = os.path.join(CODE_DIR, name) 
        if os.path.exists(file_path):
            return file_path
    return None

def run_test_case(script_path, input_file, expected_output_file):
    """
    Thực thi script của user với input và so sánh output.
    """
    # Đọc input từ file .in
    with open(input_file, 'r', encoding='utf-8') as f:
        input_data = f.read()

    # Kiểm tra file output kỳ vọng (.out)
    if not os.path.exists(expected_output_file):
        return False, "Missing .out file", ""

    # Đọc output kỳ vọng từ file .out (loại bỏ khoảng trắng thừa)
    with open(expected_output_file, 'r', encoding='utf-8') as f:
        expected_output = f.read().strip()

    try:
        # Chạy script của user bằng subprocess
        process = subprocess.run(
            [sys.executable, script_path], # sys.executable đảm bảo dùng đúng interpreter
            input=input_data,
            capture_output=True,
            text=True,
            # CWD là BASE_DIR (thư mục Tools) để script user đọc được Data/
            cwd=BASE_DIR 
        )

        # Xử lý lỗi Runtime (Return code khác 0)
        if process.returncode != 0:
            error_details = process.stderr.strip() if process.stderr else "Unknown error"
            return False, f"Runtime Error: {error_details}", expected_output

        # Lấy output thực tế và loại bỏ khoảng trắng thừa
        actual_output = process.stdout.strip()

        # So sánh output
        if actual_output == expected_output:
            return True, actual_output, expected_output
        else:
            return False, actual_output, expected_output
            
    except Exception as e:
        # Xử lý các lỗi hệ thống hoặc lỗi khác (ví dụ: file không chạy được)
        return False, f"System Error: {str(e)}", ""

# =================================================================
# 3. Hàm Main (Quản lý chấm bài)
# =================================================================

def main():
    print(f"{'='*30} AUTO GRADER {'='*30}")

    # 📌 Kiểm tra xem có tham số tên bài không
    if len(sys.argv) > 1:
        target_problem = sys.argv[1]
    else:
        target_problem = None

    if not os.path.exists(INPUT_DIR):
        print(f"❌ Không tìm thấy thư mục Input tại: {INPUT_DIR}")
        return
    
    if not os.path.exists(CODE_DIR):
        print(f"❌ Không tìm thấy thư mục Code tại: {CODE_DIR}")
        print("   Vui lòng tạo thư mục 'Code' và đặt file bài làm vào đó.")
        return

    # Xác định danh sách các bài toán cần chấm
    if target_problem:
        if os.path.isdir(os.path.join(INPUT_DIR, target_problem)):
             problems = [target_problem]
        else:
             print(f"❌ Không tìm thấy bài '{target_problem}' trong thư mục Input.")
             return
    else:
        problems = [d for d in os.listdir(INPUT_DIR) if os.path.isdir(os.path.join(INPUT_DIR, d))]

    for problem in problems:
        print(f"\n📍 Đang chấm bài: {Colors.WARN}{problem}{Colors.RESET}")

        script_path = find_script_file(problem)
        if not script_path:
            print(f"   ❌ Không tìm thấy file code trong folder Code/")
            print(f"      (Kỳ vọng: {problem}.py, {problem.lower()}.py...)")
            continue

        input_files = sorted(glob.glob(os.path.join(INPUT_DIR, problem, "*.in")))
        if not input_files:
            print("   ⚠️ Không có test case nào.")
            continue

        passed_tests = 0
        total_tests = len(input_files)
        
        for inp_f in input_files:
            filename = os.path.basename(inp_f)
            test_name = os.path.splitext(filename)[0]
            out_f = os.path.join(OUTPUT_DIR, problem, f"{test_name}.out")

            is_pass, actual, expected = run_test_case(script_path, inp_f, out_f)

            if is_pass:
                print(f"   ✅ Test {test_name}: {Colors.PASS}PASSED{Colors.RESET}")
                passed_tests += 1
            else:
                # --- PHẦN ĐÃ ĐƯỢC CHỈNH SỬA ĐỂ CĂN LỀ ĐẸP HƠN ---
                print(f"   ❌ Test {test_name}: {Colors.FAIL}FAILED{Colors.RESET}")
                
                # Căn lề cho Expected Output
                print("      Expected:")
                # Thay thế ký tự xuống dòng bằng ký tự xuống dòng kèm căn lề mới
                formatted_expected = expected.replace('\n', '\n               ') 
                print(f"               {formatted_expected}") 

                # Căn lề cho Actual Output (Got)
                print("      Got     :")
                formatted_actual = actual.replace('\n', '\n               ')
                print(f"               {formatted_actual}")
                # ---------------------------------------------------

        print(f"   >> Tổng kết: {passed_tests}/{total_tests} test cases.")

if __name__ == "__main__":
    main()