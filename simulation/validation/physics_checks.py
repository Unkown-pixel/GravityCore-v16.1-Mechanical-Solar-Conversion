"""
Physics Validation Checks for Gravity Core v16.1

Verifies key physics principles are properly implemented
"""

import numpy as np
from core import MechanicalSystem, PhotoconductiveLayer

def check_venturi_effect():
    """Verify hourglass track creates proper speed increase"""
    mech = MechanicalSystem()
    base_force = 0.1  # N
    
    # Calculate speeds at wide and narrow sections
    wide_speed = mech.speed(base_force)
    narrow_width_ratio = mech.track_width[0] / mech.track_width[2]
    expected_speed = wide_speed * np.sqrt(narrow_width_ratio)
    
    # Simulate narrow section
    narrow_force = base_force * narrow_width_ratio  # Force scales with area
    actual_speed = mech.speed(narrow_force)
    
    # Check if actual matches expected (within 1% tolerance)
    error = abs(actual_speed - expected_speed) / expected_speed
    print(f"Venturi Effect Check: {'PASS' if error < 0.01 else 'FAIL'}")
    print(f"  Expected speed increase: {np.sqrt(narrow_width_ratio):.2f}x")
    print(f"  Actual speed increase: {actual_speed/wide_speed:.2f}x")
    print(f"  Error: {error*100:.2f}%")
    return error < 0.01

def check_photoconductive_response():
    """Verify photoconductive layer responds correctly to light"""
    photo = PhotoconductiveLayer()
    
    # Test resistance at different light levels
    dark_resistance = photo.resistance(0.1)  # Very low light (0.1 W/m²)
    medium_resistance = photo.resistance(50)  # Medium light (50 W/m²)
    bright_resistance = photo.resistance(500)  # Bright light (500 W/m²)
    
    # Check if resistance decreases with light intensity
    resistance_decrease_1 = dark_resistance / medium_resistance
    resistance_decrease_2 = medium_resistance / bright_resistance
    
    print(f"Photoconductive Response Check: {'PASS' if resistance_decrease_1 > 1 and resistance_decrease_2 > 1 else 'FAIL'}")
    print(f"  Dark to medium light: {resistance_decrease_1:.2f}x decrease")
    print(f"  Medium to bright light: {resistance_decrease_2:.2f}x decrease")
    
    # Check if proper layer is active at each light level
    layer_1 = [layer['name'] for layer in photo.layers if layer['range'][0] <= 0.1 <= layer['range'][1]]
    layer_2 = [layer['name'] for layer in photo.layers if layer['range'][0] <= 50 <= layer['range'][1]]
    layer_3 = [layer['name'] for layer in photo.layers if layer['range'][0] <= 500 <= layer['range'][1]]
    
    print(f"  Low light layer: {layer_1[0] if layer_1 else 'NONE'} (should be graphene)")
    print(f"  Medium light layer: {layer_2[0] if layer_2 else 'NONE'} (should be CdTe)")
    print(f"  Bright light layer: {layer_3[0] if layer_3 else 'NONE'} (should be a-Si)")
    
    return (resistance_decrease_1 > 1 and resistance_decrease_2 > 1 and 
            layer_1[0] == 'graphene' and layer_2[0] == 'CdTe' and layer_3[0] == 'a-Si')

def check_energy_conservation():
    """Verify energy is conserved in the simulation"""
    from core import simulate_full_cycle
    
    results = simulate_full_cycle()
    
    # Check if output <= input (energy conservation)
    energy_conserved = results['electrical_output'] <= results['solar_input']
    
    # Check if efficiency <= 100%
    efficiency_valid = results['efficiency'] <= 1.0
    
    print(f"Energy Conservation Check: {'PASS' if energy_conserved and efficiency_valid else 'FAIL'}")
    print(f"  Solar Input: {results['solar_input']:.4f} J")
    print(f"  Electrical Output: {results['electrical_output']:.4f} J")
    print(f"  Efficiency: {results['efficiency']*100:.1f}%")
    
    return energy_conserved and efficiency_valid

if __name__ == "__main__":
    print("="*50)
    print("PHYSICS VALIDATION CHECKS")
    print("="*50)
    
    venturi_pass = check_venturi_effect()
    photo_pass = check_photoconductive_response()
    energy_pass = check_energy_conservation()
    
    print("\n" + "="*50)
    print(f"OVERALL VALIDATION: {'PASS' if venturi_pass and photo_pass and energy_pass else 'FAIL'}")
    print("="*50)
