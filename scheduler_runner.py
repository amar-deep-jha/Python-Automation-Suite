# Scheduler runner script
import schedule, time, os

def run_all():
    print("\n🕐 Running all automation tasks...")
    os.system("python file_organizer.py")
    os.system("python web_scraper.py")
    os.system("python email_automation.py")
    print("✅ All tasks done!\n")

schedule.every(1).minutes.do(run_all)  # change timing as needed
print("Scheduler started... press Ctrl+C to exit.")
while True:
    schedule.run_pending()
    time.sleep(5)
