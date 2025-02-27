import re
import logging
from datetime import datetime
from user_agents import parse  

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class LogParser:
    def __init__(self, file_path="apache_logs.txt"):

        self.file_path = file_path

        self.LOG_PATTERN = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+|-) "(.*?)" "(.*?)"'
    
    # Parses the Apache log file and extracts structured log data

    def parse_log_file(self):

        parsed_logs = []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                for i in file:
                    match = re.match(self.LOG_PATTERN, i)
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
            logging.info("Logs parsed successfully")

        except Exception as e:
            logging.error(f"Error parsing log file: {e}")
        
        return parsed_logs
