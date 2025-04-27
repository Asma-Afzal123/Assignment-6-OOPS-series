class Countdown:
    def __init__(self, start):
        self.start = start  # Starting point

    def __iter__(self):
        self.current = self.start  # Initializing current to start
        return self  # Return the iterator object (self)

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop when countdown reaches 0
        self.current -= 1  # Decrease the current value
        return self.current  # Return the current value

# Example usage:
countdown = Countdown(5)  # Start countdown from 5
for number in countdown:
    print(number)  # Print numbers while iterating
