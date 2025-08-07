import json
import os

DATA_FILE = "data.json"

# Load data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save data
def save_data(applications):
    with open(DATA_FILE, "w") as f:
        json.dump(applications, f, indent=4)

# Add new job
def add_application():
    company = input("Company Name: ")
    role = input("Role: ")
    status = input("Status (Applied/Interviewing/Rejected/Offered): ")
    app = {"company": company, "role": role, "status": status}
    applications.append(app)
    save_data(applications)
    print("✅ Application added!")

# View jobs
def view_applications():
    if not applications:
        print("No applications found.")
        return
    for i, app in enumerate(applications, 1):
        print(f"{i}. {app['company']} - {app['role']} ({app['status']})")

# Update status
def update_status():
    view_applications()
    try:
        index = int(input("Enter application number to update: ")) - 1
        if 0 <= index < len(applications):
            new_status = input("New Status: ")
            applications[index]["status"] = new_status
            save_data(applications)
            print("✅ Status updated!")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Enter a valid number.")

# Main loop
def main():
    print("=== Job Application Tracker ===")
    while True:
        print("\n1. Add Application")
        print("2. View Applications")
        print("3. Update Status")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_application()
        elif choice == "2":
            view_applications()
        elif choice == "3":
            update_status()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    applications = load_data()
    main()
