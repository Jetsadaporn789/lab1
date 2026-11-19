from numpy import average


def to_grade(score):
    if score >= 80: return "A"
    elif score >= 70: return "B"
    elif score >= 60: return "C"
    elif score >= 50: return "D"
    return "F"
def average_grade(scores):
    return  sum(scores) / len(scores)

if __name__ == "__main__":
    scores = [85, 78, 92, 67, 54]
    print("Average:", average_grade(scores))

if __name__ == "__main__":
    scores = [85, 78, 92, 67, 54]
    print("Average:", average_grade(scores))
    print("Grades:", to_grade(average(scores)))
    