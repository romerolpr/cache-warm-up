import requests, time

class Fetch:
    start_time: float = time.time()
    time_spent: float
    
    def __init__(self) -> None:
        self.time_spent = 0
    
    def set_time_spent(self):
        end_time = time.time()
        time_spent_in_ms = (end_time - self.start_time) * 1000
        self.time_spent = time_spent_in_ms
    
    def request(self, url):
        try:
            response = requests.get(url)
            self.set_time_spent(self)
            return response
        except requests.RequestException as e:
            print("Error fetching headers:", e)
    