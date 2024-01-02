from datetime import datetime

# current date and time given timezone
current_time_local = datetime.now()
print(f"Current Local Time: {current_time_local} and {type(current_time_local)}")

# current date and time for specific timezone
colombo_time = datetime.now("Asia/Colombo")
print(f"Colombo Time: {colombo_time}")