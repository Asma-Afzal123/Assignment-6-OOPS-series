# Class definition
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage
temp_in_celsius = 25
temp_in_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_in_celsius)

print(f"{temp_in_celsius}°C is equal to {temp_in_fahrenheit}°F")
