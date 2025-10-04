"""
Annual Simulation: GravityCore v16.1 (No Adaptive Control)
365-day simulation with fixed parameters.
"""

import numpy as np
import matplotlib.pyplot as plt

class GravityCoreAnnualSimulator:
    def __init__(self):
        self.days = 365
        self.solar_irradiance = 1000  # W/m² (standard test condition)
        self.ambient_temperature = 25  # °C
        self.material_degradation_rate = 0.0012  # 0.12% per year
        self.thermal_loss_rate = 0.0005  # 0.05% per day
        self.magnetic_strength = 0.5  # Tesla (fixed)
        self.results = []

    def calculate_efficiency(self, day):
        """Calculate efficiency based on day, temperature, and irradiance"""
        # Temperature increases by 0.1°C per day
        temperature = self.ambient_temperature + 0.1 * day
        
        # Material degradation (annual)
        degradation = self.material_degradation_rate * (day / 365)
        
        # Thermal losses
        thermal_loss = self.thermal_loss_rate * day
        
        # Base efficiency (70%)
        base_efficiency = 0.70
        
        # Efficiency calculation
        efficiency = base_efficiency - degradation - thermal_loss
        
        # Cap efficiency at 100%
        if efficiency > 1.0:
            efficiency = 1.0
        elif efficiency < 0.0:
            efficiency = 0.0
            
        return efficiency, temperature

    def run_simulation(self):
        """Run the simulation for 365 days"""
        for day in range(self.days):
            # Update solar irradiance (simulate real-world variation)
            solar_irradiance = np.random.uniform(500, 1000)
            
            # Update temperature (simulate real-world variation)
            temperature = np.random.uniform(25, 75)
            
            # Calculate efficiency and energy output
            efficiency, temp = self.calculate_efficiency(day)
            energy_output = efficiency * solar_irradiance * 0.04
            
            # Store results
            self.results.append({
                'day': day,
                'solar_irradiance': solar_irradiance,
                'temperature': temp,
                'magnetic_strength': self.magnetic_strength,
                'efficiency': efficiency,
                'energy_output': energy_output
            })
        
        return self.results

# Run the simulation
simulator = GravityCoreAnnualSimulator()
results = simulator.run_simulation()

# Extract data for plotting
days = [r['day'] for r in results]
efficiencies = [r['efficiency'] for r in results]
energy_outputs = [r['energy_output'] for r in results]
magnetic_strengths = [r['magnetic_strength'] for r in results]

# Plot results
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.plot(days, efficiencies)
plt.title('Efficiency Over Time')
plt.xlabel('Day')
plt.ylabel('Efficiency')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(days, energy_outputs)
plt.title('Energy Output Over Time')
plt.xlabel('Day')
plt.ylabel('Energy Output (J)')
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(days, magnetic_strengths)
plt.title('Magnetic Field Strength Over Time')
plt.xlabel('Day')
plt.ylabel('Magnetic Strength (T)')
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(days, [r['solar_irradiance'] for r in results], label='Solar Irradiance')
plt.plot(days, [r['temperature'] for r in results], label='Temperature')
plt.title('Environmental Conditions Over Time')
plt.xlabel('Day')
plt.ylabel('Value')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('gravity_core_annual_no_adaptive.png', dpi=300, bbox_inches='tight')
plt.show()

# Print summary
print("=== Annual Simulation (No Adaptive Control) ===")
print(f"Final Efficiency: {results[-1]['efficiency']:.4f}")
print(f"Final Energy Output: {results[-1]['energy_output']:.4f} J")
print(f"Final Magnetic Strength: {results[-1]['magnetic_strength']:.2f} T")
print(f"Final Solar Irradiance: {results[-1]['solar_irradiance']:.2f} W/m²")
print(f"Final Temperature: {results[-1]['temperature']:.2f} °C")
