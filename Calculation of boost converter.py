# Calculation of boost converter.py

Vin = float(input("Enter input voltage (V): "))
Vout = float(input("Enter desired output voltage (V): "))
Pout = float(input("Enter output power (W): "))
f = float(input("Enter switching frequency (Hz): "))
efficiency = float(input("Enter efficiency (%): "))

# Convert efficiency to decimal
eta = efficiency / 100

# Duty cycle
D = 1 - (Vin / Vout)

# Output current
Iout = Pout / Vout

# Input current
Iin = Pout / (Vin * eta)

# Input power
Pin = Pout / eta

print("\n--- Boost Converter Calculations ---")
print(f"Duty Cycle = {D * 100:.2f} %")
print(f"Output Current = {Iout:.4f} A")
print(f"Input Current = {Iin:.4f} A")
print(f"Input Power = {Pin:.2f} W")
