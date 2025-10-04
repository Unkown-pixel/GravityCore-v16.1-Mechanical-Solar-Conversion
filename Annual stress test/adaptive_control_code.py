"""
Adaptive Control System for GravityCore v16.1
Optimizes magnetic field strength based on environmental conditions.
"""

import numpy as np

class AdaptiveControlSystem:
    def __init__(self):
        self.magnetic_strength = 0.5  # Tesla (initial value)
        self.solar_irradiance = 1000  # W/m² (standard test condition)
        self.temperature = 25  # °C

    def adjust_magnetic_field(self):
        """Adjust magnetic field strength based on environmental conditions"""
        # Dynamic adjustment based on solar irradiance and temperature
        if self.solar_irradiance > 800 and self.temperature < 50:
            # High irradiance, low temperature → optimize for rotation
            self.magnetic_strength = 0.7
        elif self.solar_irradiance < 500 and self.temperature > 50:
            # Low irradiance, high temperature → optimize for thermal
            self.magnetic_strength = 0.4
        elif self.temperature > 75:
            # High temperature → reduce magnetic field to prevent thermal runaway
            self.magnetic_strength = 0.3
        else:
            # Default case → maintain optimal balance
            self.magnetic_strength = 0.5

    def get_magnetic_strength(self):
        """Return current magnetic field strength"""
        return self.magnetic_strength

# Example usage
control_system = AdaptiveControlSystem()
control_system.solar_irradiance = 900  # W/m²
control_system.temperature = 40  # °C
control_system.adjust_magnetic_field()
print(f"Optimized Magnetic Strength: {control_system.get_magnetic_strength():.2f} T")
