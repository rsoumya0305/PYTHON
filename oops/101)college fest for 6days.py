'''make final report
1)day wise actitives
2)no.of teams
3)project_names
4)technology
5)ppt demostartions given
6)winner of day
7)runner up the day
8)best fermorer of day
9)host of the program of day'''

class FinalDayReport:
    def __init__(self, day, activities, num_teams, project_names, technology,
                 ppt_given, winner, runner_up, best_performer, host):
        self.day = day
        self.activities = activities
        self.num_teams = num_teams
        self.project_names = project_names
        self.technology = technology
        self.ppt_given = ppt_given
        self.winner = winner
        self.runner_up = runner_up
        self.best_performer = best_performer
        self.host = host

    def display(self):
        print(f"\n📅 Day {self.day} Report")
        print(f"Activities: {self.activities}")
        print(f"Number of Teams: {self.num_teams}")
        print(f"Project Names: {', '.join(self.project_names)}")
        print(f"Technology Used: {', '.join(self.technology)}")
        print(f"PPT Demonstrations Given: {self.ppt_given}")
        print(f"🏆 Winner of the Day: {self.winner}")
        print(f"🥈 Runner-Up of the Day: {self.runner_up}")
        print(f"🌟 Best Performer of the Day: {self.best_performer}")
        print(f"🎤 Host of the Day: {self.host}")
        print("-" * 50)


# ---------------- Main Program ----------------

# List to store multiple day reports
event_reports = []

# Sample data for Day 1
event_reports.append(FinalDayReport(
    day=1,
    activities="Team introduction, ice-breaker activities, project idea selection",
    num_teams=5,
    project_names=["Smart Garden", "EduBot", "E-Waste Tracker", "HealthMate", "AgriHelp"],
    technology=["Python", "IoT", "AI", "HTML/CSS", "Firebase"],
    ppt_given=5,
    winner="Team EduBot",
    runner_up="Team HealthMate",
    best_performer="Aarav Sharma",
    host="Soumya R"
))

# Sample data for Day 2
event_reports.append(FinalDayReport(
    day=2,
    activities="Prototype building, coding sessions, UI design",
    num_teams=5,
    project_names=["Smart Garden", "EduBot", "E-Waste Tracker", "HealthMate", "AgriHelp"],
    technology=["React", "Node.js", "TensorFlow", "Bootstrap", "MongoDB"],
    ppt_given=5,
    winner="Team Smart Garden",
    runner_up="Team AgriHelp",
    best_performer="Diya Patel",
    host="Rahul N"
))

# Show all reports
for report in event_reports:
    report.display()
