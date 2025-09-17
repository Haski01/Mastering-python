# spliting complex task
print(f"{"*"*10} Spliting Complex data {"*"*10}")


def fetch_sales():
    print("Fetching the sales data")


def filter_valid_sales():
    print("Filtering valid sales data")

def summarize_data():
    print("Summarizing sales data")


def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")


generate_report()

# hiding implementation data
print(f"{"*"*10} Hiding implementation data {"*"*10}")

def get_input():
    print("Getting user input")

def validate_input():
    print("Validating the user info")

def save_to_db():
    print("saving to database")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registration complete")


register_user()