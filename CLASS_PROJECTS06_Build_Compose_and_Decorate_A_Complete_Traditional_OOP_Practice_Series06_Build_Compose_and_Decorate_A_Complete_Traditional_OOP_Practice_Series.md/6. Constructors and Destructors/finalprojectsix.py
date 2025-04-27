class Logger:
    def __init__(self):
        print("Logger object created!")

    def __del__(self):
        print("Logger object destroyed!")

# Example usage
log1 = Logger()

# Manually delete the object
del log1
