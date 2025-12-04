import os
import subprocess
import sys
import glob

class Colors:
    PASS = '\033[92m'
    FAIL = '\033[91m'
    WARN = '\033[93m'
    RESET = '\033[0m'

# Cấu hình đường dẫn
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, 'Input')
OUTPUT_DIR = os.path.join(BASE_DIR, 'Output')
CODE_DIR = os.path.join(BASE_DIR, 'Code')  # <--- Thư mục chứa code của user

def find_script_file(problem_name):
    """
    Tìm file python trong thư mục Code/
    """
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
    with open(input_file, 'r', encoding='utf-8') as f:
        input_data = f.read()

    if not os.path.exists(expected_output_file):
        return False, "Missing .out file", ""

    with open(expected_output_file, 'r', encoding='utf-8') as f:
        expected_output = f.read().strip()

    try:
        process = subprocess.run(
            [sys.executable, script_path],
            input=input_data,
            capture_output=True,
            text=True,
            # Giữ cwd là BASE_DIR để script trong folder Code 
            # vẫn đọc được folder Data ở root (vd: open('Data/tips.json'))
            cwd=BASE_DIR 
        )

        if process.returncode != 0:
            return False, f"Runtime Error: {process.stderr.strip()}", expected_output

        actual_output = process.stdout.strip()

        if actual_output == expected_output:
            return True, actual_output, expected_output
        else:
            return False, actual_output, expected_output
            
    except Exception as e:
        return False, f"System Error: {str(e)}", ""

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

    # Nếu có tham số → chỉ chấm bài đó
    if target_problem:
        # Kiểm tra xem folder bài đó có tồn tại trong Input không
        if os.path.isdir(os.path.join(INPUT_DIR, target_problem)):
             problems = [target_problem]
        else:
             print(f"❌ Không tìm thấy bài '{target_problem}' trong thư mục Input.")
             return
    else:
        # Nếu không → chấm tất cả bài có trong folder Input
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
                print(f"   ❌ Test {test_name}: {Colors.FAIL}FAILED{Colors.RESET}")
                print(f"      Expected: {expected}")
                print(f"      Got     : {actual}")

        print(f"   >> Kết quả: {passed_tests}/{total_tests} test cases.")

if __name__ == "__main__":
    main()