import csv
import openpyxl
from collections import defaultdict

def create_student_scores_csv():
    """Create a CSV file with student scores."""
    data = [
        ["Name", "Subject", "Score"],
        ["Alice", "Math", 85],
        ["Bob", "Math", 90],
        ["Alice", "Science", 95],
        ["Bob", "Science", 80],
        ["Charlie", "Math", 70],
        ["Charlie", "Science", 75],
    ]
    with open("student_scores.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("student_scores.csv file created.")

def analyze_student_data():
    """Analyze student data and write results to an Excel file."""
    student_scores = defaultdict(list)
    subject_scores = defaultdict(list)

    # Read data from CSV file
    with open("student_scores.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["Name"]
            subject = row["Subject"]
            score = float(row["Score"])
            student_scores[name].append(score)
            subject_scores[subject].append(score)

    # Calculate averages
    student_averages = {name: sum(scores) / len(scores) for name, scores in student_scores.items()}
    subject_averages = {subject: sum(scores) / len(scores) for subject, scores in subject_scores.items()}

    # Write results to an Excel file
    workbook = openpyxl.Workbook()

    # Sheet 1: Student Averages
    student_sheet = workbook.active
    student_sheet.title = "Student Averages"
    student_sheet.append(["Name", "Average Score"])
    for name, avg_score in student_averages.items():
        student_sheet.append([name, avg_score])

    # Sheet 2: Subject Averages
    subject_sheet = workbook.create_sheet(title="Subject Averages")
    subject_sheet.append(["Subject", "Average Score"])
    for subject, avg_score in subject_averages.items():
        subject_sheet.append([subject, avg_score])

    workbook.save("results.xlsx")
    print("Analysis complete. Results saved to results.xlsx.")

# Example usage
create_student_scores_csv()  # Create the input CSV file
analyze_student_data()  # Analyze the data and generate the Excel report
