# Rocket Flight Simulation

An object-oriented rocket flight simulation featuring modular architecture, solid/liquid engine models, atmospheric effects, validation, and unit testing.

## 🚀 Features
- **Modular OOP Architecture:** Separated components for Rocket, Engines, Environment, Physics, and Simulation.
- **Engine Models:** Supports both `Solid_Engine` (thrust curve based on sine wave) and `Liquid_Engine` (throttle-controlled constant thrust).
- **Dynamic Environment:** Atmospheric air density decay and gravity calculations based on current altitude.
- **Robust Validation:** Strict runtime type-checking and value validation using `isinstance` and `ValueError`.
- **Unit Tested:** Built-in validation suite ensuring physical equations and state updates work correctly.

## 📁 Project Structure
```text
├── engines.py          # Abstract base and specific engine implementations
├── rocket.py           # Rocket specifications and mass/area properties
├── environment.py      # Atmosphere and gravity models
├── physics.py          # Drag and net force calculations
├── simulation.py       # Main simulation loop and state history
├── main.py             # CLI application to run simulations
└── test_rocket.py      # Unit tests for verification
```

## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd rocket-flight-simulation
   ```

2. Run the main simulation:
   ```bash
   python main.py
   ```
   *Follow the terminal prompts to select either a **solid** or **liquid** engine scenario. Results will be saved to `simulation_results.txt`.*

3. Run the unit tests:
   ```bash
   python test_rocket.py
   ```

## 📊 Sample Output (`simulation_results.txt`)
```text
------------------SIMULATION RESULTS------------------
Type of engine: solid
Max altitude: 485.23 m
Time of maximum altitude: 10.50 s
Max velocity: 112.45 m/s
...
```

