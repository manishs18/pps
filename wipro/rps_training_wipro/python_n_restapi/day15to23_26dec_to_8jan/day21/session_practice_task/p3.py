class Logger:
    logCount = 0

    @classmethod
    def log_msg(cls, msg):
        with open("03012025.logs","a") as f:
            cls.logCount+=1
            f.write(f'Log[{cls.logCount}] {msg}\n')

    @staticmethod
    def log_warn(msg):
        with open("03012025.logs","a") as f:
            f.writelines(f'[WARNING]: {msg}\n')


Logger.log_msg("Application Started")
Logger.log_warn("Disk Full")
Logger.log_msg("Application Crashed")
