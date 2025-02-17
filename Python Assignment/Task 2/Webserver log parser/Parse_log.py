import re
from datetime import datetime
from user_agents import parse  

LOG_PATTERN = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+|-) "(.*?)" "(.*?)"'

def parse_log_file(file_path="apache_logs.txt"):
    parsed_logs = []
    with open(file_path, "r", encoding="utf-8") as file:
        for i in file:
            match = re.match(LOG_PATTERN, i)
            if match:
                ip, timestamp, request, status, _, _, user_agent = match.groups()
                
                method, url, _ = request.split(" ")

                ua = parse(user_agent)

                parsed_logs.append({
                    "ip": ip,
                    "timestamp": datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S %z"),
                    "method": method,
                    "url": url,
                    "status": int(status),
                    "os": ua.os.family,      
                    "browser": ua.browser.family,  
                    "agent": user_agent         
                })
    
    print("Logs Parsed Succesfully")
    return parsed_logs

if __name__ == "__main__":
    logs = parse_log_file()


