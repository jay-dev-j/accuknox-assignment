import requests
import matplotlib.pyplot as plt

# I got api data from this website https://www.slingacademy.com/
url = "https://api.slingacademy.com/v1/sample-data/files/student-scores.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print("Failed to fetch data")
    exit()

students = data[:20]
names = []
averages = []

for student in students:

    name = student["first_name"] + " " + student["last_name"]

    total = (
        student["math_score"]
        + student["history_score"]
        + student["physics_score"]
        + student["chemistry_score"]
        + student["biology_score"]
        + student["english_score"]
        + student["geography_score"]
    )

    average = total / 7

    names.append(name)
    averages.append(average)

    print(name, "Average = ", round(average, 2))


plt.bar(names, averages)

plt.xlabel("Students")
plt.ylabel("Average Score of student")
plt.title("Students Average Scores")

plt.xticks(rotation=90)

plt.tight_layout()
plt.show()