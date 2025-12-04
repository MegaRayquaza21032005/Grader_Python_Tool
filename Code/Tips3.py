from sys import stdin
import json, os

def main():
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # file_path = os.path.join(BASE_DIR, "..", "Data", "tips.json")
    file_path = "/home/ngtukien/Documents/D23CT01_Python/Tools/Data/tips.json"
    with open(file_path, 'r') as f:
        data = json.load(f)

    list_bills = data['tips']
    input_data = stdin.read().split()
    it = iter(input_data)

    for _ in range(int(next(it))):
        tar_date = next(it)
        tar_size = next(it)
        total = 0.0
        count = 0
        for bill in list_bills:
            json_date = bill['day']
            json_size = str(bill['size'])
            if json_date == tar_date and json_size == tar_size:
                total += float(bill['total_bill'])
                count += 1
        if count > 0:
            avg = total / count
            # print(f"{avg:.4f}")
        else:
            print('Invalid')

if __name__ == "__main__":
    main()
