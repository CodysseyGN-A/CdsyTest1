import json
import os

DATA_FILE = "attendance.json"


def load_data():
    """저장된 출석 데이터를 불러온다."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_data(data):
    """출석 데이터를 파일에 저장한다."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_attendance(data):
    """날짜와 이름을 입력받아 출석 기록을 추가한다."""
    date = input("날짜를 입력하세요 (예: 2026-11-02): ").strip()
    name = input("이름을 입력하세요: ").strip()

    if not date or not name:
        print("날짜와 이름은 비워둘 수 없습니다.")
        return

    record = {
        "date": date,
        "name": name
    }
    data.append(record)
    save_data(data)
    print("출석이 저장되었습니다.")


def show_attendance(data):
    """저장된 출석 목록을 보여준다."""
    if not data:
        print("출석 기록이 아직 없습니다.")
        return

    print("\n=== 출석 목록 ===")
    for i, record in enumerate(data, start=1):
        print(f"{i}. 날짜: {record['date']} | 이름: {record['name']}")
    print("=================\n")


def main():
    data = load_data()

    while True:
        print("스터디 출석부")
        print("1. 출석 추가")
        print("2. 목록 보기")
        print("3. 종료")

        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "1":
            add_attendance(data)
        elif choice == "2":
            show_attendance(data)
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 1, 2, 3 중에서 골라주세요.")


if __name__ == "__main__":
    main()