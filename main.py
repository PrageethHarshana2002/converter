from temperature_operations import TemperatureConverter

if __name__ == "__main__":
    converter = TemperatureConverter()
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")


    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {converter.celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F = {converter.fahrenheit_to_celsius(fahrenheit):.2f}°C")
    elif choice == '3':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {converter.celsius_to_kelvin(celsius):.2f} K")
    else:
        print("Invalid choice!")
