from temperature_operations import TemperatureConverter

if __name__ == "__main__":
    converter = TemperatureConverter()
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. kelvin to celsius")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}C = {converter.celsius_to_fahrenheit(celsius):.2f}F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}F = {converter.fahrenheit_to_celsius(fahrenheit):.2f}C")
    elif choice == '3':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}C = {converter.celsius_to_kelvin(celsius):.2f} K")
    elif choice == '4':
        kelvin = float(input("Enter  temperature in kelvin: "))
        print(f"{kelvin }k = {converter. kelvin_to_celsius(kelvin):.2f} C")
    else:
        print("Invalid choice!")
