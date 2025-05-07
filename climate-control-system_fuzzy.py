import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import networkx as nx

# Define the temperature error (desired - current) universe and membership functions
temperature_error = ctrl.Antecedent(np.arange(-10, 10.1, 0.1), 'temperature_error')
control_signal = ctrl.Consequent(np.arange(-1, 1.1, 0.1), 'control_signal')

# Membership functions for temperature_error
temperature_error['nb'] = fuzz.trimf(temperature_error.universe, [-10, -10, -5])  # Negative Big
temperature_error['ns'] = fuzz.trimf(temperature_error.universe, [-10, -5, 0])    # Negative Small
temperature_error['ze'] = fuzz.trimf(temperature_error.universe, [-5, 0, 5])      # Zero
temperature_error['ps'] = fuzz.trimf(temperature_error.universe, [0, 5, 10])      # Positive Small
temperature_error['pb'] = fuzz.trimf(temperature_error.universe, [5, 10, 10])     # Positive Big

# Membership functions for control_signal
control_signal['cool_high'] = fuzz.trimf(control_signal.universe, [-1, -1, -0.5]) # Cool High
control_signal['cool_low'] = fuzz.trimf(control_signal.universe, [-1, -0.5, 0])   # Cool Low
control_signal['no_action'] = fuzz.trimf(control_signal.universe, [-0.5, 0, 0.5]) # No Action
control_signal['heat_low'] = fuzz.trimf(control_signal.universe, [0, 0.5, 1])     # Heat Low
control_signal['heat_high'] = fuzz.trimf(control_signal.universe, [0.5, 1, 1])    # Heat High

# Fuzzy rules
rule1 = ctrl.Rule(temperature_error['nb'], control_signal['cool_high'])  # If error is NB, cool hard
rule2 = ctrl.Rule(temperature_error['ns'], control_signal['cool_low'])   # If error is NS, cool soft
rule3 = ctrl.Rule(temperature_error['ze'], control_signal['no_action'])  # If error is ZE, no action
rule4 = ctrl.Rule(temperature_error['ps'], control_signal['heat_low'])   # If error is PS, heat soft
rule5 = ctrl.Rule(temperature_error['pb'], control_signal['heat_high'])  # If error is PB, heat hard

# Create the control system
climate_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
climate_sim = ctrl.ControlSystemSimulation(climate_ctrl)

def main():
    print("Fuzzy Logic Climate Control System")
    print("Enter current temperature and desired temperature to calculate control signal.")
    
    while True:
        try:
            current_temp = float(input("\nEnter current temperature (°C): "))
            desired_temp = float(input("Enter desired temperature (°C): "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue
        
        error = desired_temp - current_temp
        climate_sim.input['temperature_error'] = error
        
        try:
            climate_sim.compute()
        except Exception as e:
            print(f"Error in computation: {e}. Please check inputs.")
            continue
        
        output = climate_sim.output['control_signal']
        
        # Determine action
        if output > 0:
            action = f"Heating at {output * 100:.1f}%"
        elif output < 0:
            action = f"Cooling at {-output * 100:.1f}%"
        else:
            action = "No action needed."
        
        print(f"Temperature error: {error:.1f}°C")
        print(f"Control signal: {output:.2f}")
        print(f"Action: {action}")

if __name__ == "__main__":
    main()