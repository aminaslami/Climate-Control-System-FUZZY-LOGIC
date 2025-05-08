# Climate Control System FUZZY LOGIC

### Necessary Libraries
  1 - pip install numpy
  
  2 - pip install scikit-fuzzy
  
  3 - pip install control
  
  4 - pip install networkx

  5 - pip install scipy


## Approach

### 1. Define Input and Output Variables:

The input variable is the temperature error, calculated as the difference between the desired temperature and the current temperature.

The output variable is the control signal, which determines the intensity of heating or cooling needed.

### 2. Membership Functions:

The input variable (temperature error) is divided into five fuzzy sets: Negative Big (nb), Negative Small (ns), Zero (ze), Positive Small (ps), and Positive Big (pb).

The output variable (control signal) is divided into five fuzzy sets: Cool High, Cool Low, No Action, Heat Low, and Heat High.

### 3. Fuzzy Rules:

Define rules to map the input fuzzy sets to the output fuzzy sets. For example, if the temperature error is Negative Big (current temperature is much higher than desired), the control signal should be Cool High.

### 4. Control System and Simulation:

Create a fuzzy control system using the defined rules and simulate it to compute the control signal based on the input temperature error.

### 5. User Interaction:

Prompt the user for current and desired temperatures, compute the temperature error, and use the fuzzy control system to determine the appropriate heating or cooling action.


**Output:** 

![image](https://github.com/user-attachments/assets/1712bc7e-b0ed-4c4f-81bf-3d271a3e1a2e)

```<language python>
PS C:\Users\MAA\.spyder-py3>  c:; cd 'c:\Users\MAA\.spyder-py3';   &'c:\Users\MAA\AppData\Local\Programs\Python\Python313\python.exe''c:\Users\MAA\.vscode\extensions\ms-python.debugpy-2025.6.0-win32-x64\bundled\libs\debugpy\launcher' '22971' '--' 'c:\Users\MAA\.spyder-py3\climate-control-  system_fuzzy.py' 

Fuzzy Logic Climate Control System

Enter current temperature and desired temperature to calculate control signal.

Enter current temperature (°C): 20
Enter desired temperature (°C): 10
Temperature error: -10.0°C
Control signal: -0.83
Action: Cooling at 83.3%

Temperature error: -10.0°C
Control signal: -0.83
Action: Cooling at 83.3%

Control signal: -0.83
Action: Cooling at 83.3%

Action: Cooling at 83.3%

Enter current temperature (°C): 15
Enter desired temperature (°C): 10
Enter desired temperature (°C): 10
Temperature error: -5.0°C
Control signal: -0.50
Action: Cooling at 50.0%
Action: Cooling at 50.0%
```

Project Source: https://chatgpt.com/share/681cd02d-eb74-8009-ae08-ecbb558b6ec5
