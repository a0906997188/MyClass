from dataclasses import dataclass


@dataclass(frozen=True)
class CourseWeek:
    week: int
    topic: str
    note: str = ""


course_schedule = [
    CourseWeek(1, "課程介紹 (introduction)"),
    CourseWeek(2, "資料結構應用 (data structure application)"),
    CourseWeek(3, "陣列與串列 (array & list)"),
    CourseWeek(4, "陣列與串列 (array & list)"),
    CourseWeek(5, "堆疊及運算表示法 (stack & expression representation)"),
    CourseWeek(6, "堆疊及運算表示法 (stack & expression representation)"),
    CourseWeek(7, "資料結構程式實作 (data structure implementation)"),
    CourseWeek(8, "期中學習評量", "midterm"),
    CourseWeek(9, "雜湊函數 (hash function)"),
    CourseWeek(10, "佇列 (queue)"),
    CourseWeek(11, "圖學介紹 (intro. to graph theory)"),
    CourseWeek(12, "二元樹 (binary tree)"),
    CourseWeek(13, "二元樹 (binary tree)"),
    CourseWeek(14, "二元樹搜尋及拜訪 (binary search & traversal)"),
    CourseWeek(15, "生成樹 (spanning tree)"),
    CourseWeek(16, "期末學習評量", "final exam"),
    CourseWeek(17, "多元學習週 - AI 及 SDGs 訓練", "Diverse Learning: AI and SDGs Training"),
    CourseWeek(18, "多元學習週 - AI 及 SDGs 訓練", "Diverse Learning: AI and SDGs Training"),
]


if __name__ == "__main__":
    # Render the schedule as a simple text table when executed directly.
    for entry in course_schedule:
        note = f" | {entry.note}" if entry.note else ""
        print(f"Week {entry.week:>2}: {entry.topic}{note}")
