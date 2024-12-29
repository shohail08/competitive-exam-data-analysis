import pandas as pd

# Data for exams, institutes, branches, cutoffs, and fees
data = {
    "Exam": ["JEE", "JEE", "JEE", "JEE", "NEET", "NEET", "NEET", "NEET",
             "CAT", "CAT", "CAT", "CAT", "CLAT", "CLAT", "CLAT", "CLAT"],
    "Institute Name": ["IIT Delhi", "IIT Bombay", "IIT Madras", "IIT Kanpur",
                        "AIIMS Delhi", "AIIMS Jodhpur", "AIIMS Bhopal", "AIIMS Bhubaneswar",
                        "IIM Ahmedabad", "IIM Bangalore", "IIM Calcutta", "IIM Lucknow",
                        "NLU Delhi", "NLU Bangalore", "NLU Hyderabad", "NLU Kolkata"],
    "Branch": ["Computer Science", "Computer Science", "Electrical Engineering", "Mechanical Engineering",
               "MBBS", "MBBS", "BDS", "BDS",
               "MBA", "MBA", "MBA", "MBA",
               "Law", "Law", "Law", "Law"],
    "2023 Cutoff": [93, 67, 450, 800, 720, 715, 700, 690, 99.5, 99.2, 99.0, 98.8, 120, 110, 105, 100],
    "2024 Expected Cutoff": [90, 65, 430, 780, 725, 720, 710, 700, 99.6, 99.3, 99.1, 98.9, 125, 115, 110, 105],
    "Fees (₹/year)": [200000, 200000, 200000, 200000, 6000, 6000, 6000, 6000, 2300000, 2200000, 2250000, 2100000, 120000, 110000, 100000, 95000]
}

# Convert data to a Pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_file = "National_Level_Exam_Insights.xlsx"
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"Spreadsheet '{output_file}' created successfully!")
