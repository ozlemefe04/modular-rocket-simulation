import os
from rocket import Rocket
from engines import Solid_Engine, Liquid_Engine
from environment import Environment
from physics import Physics
from simulation import Simulation
 
os.chdir("C:\\Users\\Özlem\\Desktop\\RocketSimulation")

engine_choice = input("Choose engine type (solid / liquid):").lower()
if engine_choice == "solid":
    engine = Solid_Engine(burn_time=3.5, Isp=200, thrust_peak=1200)
    rocket = Rocket(dry_mass=6.0, fuel_mass=4.0, diameter=0.15, Cd=0.45, engine=engine)
    time=60
elif engine_choice == "liquid":
    engine = Liquid_Engine(burn_time=150.0, Isp=300.0, thrust_max=160000.0)
    rocket = Rocket(dry_mass=1500.0, fuel_mass=9500.0, diameter=1.2, Cd=0.2, engine=engine)
    time=400
else:
    raise ValueError("Invalid engine type. Please type 'solid' or 'liquid'.")

environment = Environment()
physics = Physics()
simulation = Simulation(Rocket=rocket,Environment=environment, Physics=physics, dt=0.5)



simulation.run(max_time=time)


with open('simulation_results.txt', 'w') as file:

    file.write("------------------SIMULATION RESULTS------------------\n")
    file.write("Type of engine: " + str(engine_choice) + "\n")
    file.write("Max altitude: " + str(simulation.max_altitude) + "\n")
    file.write("Time of maximum altitude: " + str(simulation.time_altitude) + "\n")
    file.write("Max velocity: " + str(simulation.max_velocity) + "\n")
    file.write("Time of maximum velocity: " + str(simulation.time_velocity) + "\n")
    file.write("Fuel remaining: " + str(simulation.rocket.fuel_mass) + "\n")
    file.write("Total flight time: " + str(simulation.last) + "\n")
    file.write("Maximum acceleration: " + str(simulation.max_acceleration) + "\n")
    file.write("Time of maximum acceleration: " + str(simulation.time_acceleration) + "\n")


print("The simulation results have been written to 'simulation_results.txt")
