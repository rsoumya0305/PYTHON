'''write a report of 15 days of
1.day
2.topics covered
3.effeiency(rate of efficincy& grip on topics larent on large on scale of 5)
4.no.of que solved
5.no.of hacker rank solved
6.ratings acheived on hackerrank for particular dat
7)certifications completted(including name)
8)duration of class
9)rate the session on scale of 5 
 worst
 bad
 avg
 good
 super'''


class DailyReport:
    def __init__(self, day, topics, efficiency, questions_solved,
                 hacker_rank_solved, hacker_rank_rating, certification,
                 duration, session_rating):
        self.day = day
        self.topics = topics
        self.efficiency = efficiency  # Out of 5
        self.questions_solved = questions_solved
        self.hacker_rank_solved = hacker_rank_solved
        self.hacker_rank_rating = hacker_rank_rating
        self.certification = certification
        self.duration = duration  # In hours
        self.session_rating = session_rating  # worst, bad, avg, good, super

    def display(self):
        print(f"Day: {self.day}")
        print(f"Topics Covered: {self.topics}")
        print(f"Efficiency (out of 5): {self.efficiency}")
        print(f"Questions Solved: {self.questions_solved}")
        print(f"HackerRank Questions Solved: {self.hacker_rank_solved}")
        print(f"HackerRank Rating: {self.hacker_rank_rating}")
        print(f"Certifications Completed: {self.certification}")
        print(f"Class Duration (hours): {self.duration}")
        print(f"Session Rating: {self.session_rating}")
        print("-" * 40)


# ---------------- Main Program ----------------

# Create a list to store 15 daily reports
report_list = []

# Manually add reports here (example for 3 days, you can add up to 15)
report_list.append(DailyReport(1, "Python Basics", 4.5, 10, 5, 1400, "None", 2, "good"))
report_list.append(DailyReport(2, "OOP Concepts", 5, 12, 6, 1450, "Python OOP - NPTEL", 2.5, "super"))
report_list.append(DailyReport(3, "Functions & Recursion", 4, 8, 4, 1480, "None", 2, "good"))
# Add up to 15 days like above

# Display all reports
for report in report_list:
    report.display()

