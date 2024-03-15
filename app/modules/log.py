import datetime

class Log:
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    def __write_log(self, level, message, print_log):
        filename = f'log-{self.current_date}.txt'
        log_entry = f'[{self.timestamp}] [{level.upper()}] {message}'
        with open(filename, 'a') as file:
            file.write(log_entry+'\n')
            
        print(log_entry) if print_log else None

    def info(self, message, print_log = True):
        self.__write_log(self, level='INFO', message=message, print_log=print_log)

    def warning(self, message, print_log = True):
        self.__write_log(self, level='WARNING', message=message, print_log=print_log)

    def error(self, message, print_log = True):
        self.__write_log(self, level='ERROR', message=message, print_log=print_log)