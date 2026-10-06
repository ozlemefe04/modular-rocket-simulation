import math
from rocket import Rocket
from engines import Solid_Engine, Liquid_Engine
from environment import Environment
from physics import Physics
from simulation import Simulation

engine_choice = input("Choose engine type for tests (solid / liquid): ").lower()

def get_test_setup():
    if engine_choice == "solid":
        engine = Solid_Engine(burn_time=3.5, Isp=200, thrust_peak=1200)
        rocket = Rocket(dry_mass=6.0, fuel_mass=4.0, diameter=0.15, Cd=0.45, engine=engine)
    elif engine_choice == "liquid":
        engine = Liquid_Engine(burn_time=150.0, Isp=300.0, thrust_max=160000.0)
        rocket = Rocket(dry_mass=1500.0, fuel_mass=9500.0, diameter=1.2, Cd=0.2, engine=engine)
    else:
        raise ValueError("Invalid engine type. Please type 'solid' or 'liquid'.")
    
    environment = Environment()
    physics = Physics()
    return rocket, engine, environment, physics

def test_rocket():
    rocket, engine, _, _ = get_test_setup()
    if engine_choice == "solid":
        assert rocket.dry_mass == 6.0
        assert rocket.fuel_mass == 4.0
        assert rocket.diameter == 0.15
        assert rocket.Cd == 0.45
    elif engine_choice == "liquid":
        assert rocket.dry_mass == 1500.0
        assert rocket.fuel_mass == 9500.0
        assert rocket.diameter == 1.2
        assert rocket.Cd == 0.2

    expected_area = math.pi * (rocket.diameter / 2) ** 2
    assert math.isclose(rocket.get_area(), expected_area, rel_tol=1e-5)
    assert rocket.get_mass() == (rocket.dry_mass + rocket.fuel_mass)

def test_engine():
    _, engine, _, _ = get_test_setup()
    if engine_choice == "solid":
        assert engine.burn_time == 3.5
        assert engine.Isp == 200
        assert engine.thrust_peak == 1200
        assert engine.get_thrust(time=1.0) > 0
        assert engine.get_thrust(time=4.0) == 0
    elif engine_choice == "liquid":
        assert engine.burn_time == 150.0
        assert engine.Isp == 300.0
        assert engine.thrust_max == 160000.0
        assert engine.get_thrust(time=10.0, throttle=1) == 160000.0
        assert engine.get_thrust(time=200.0) == 0

def test_environment():
    _, _, environment, _ = get_test_setup()
    assert math.isclose(environment.get_air_density(0), 1.225, rel_tol=1e-5)
    assert environment.get_air_density(2000) < environment.get_air_density(0)
    assert math.isclose(environment.get_gravity(0), 9.81, rel_tol=1e-1)

def test_physics():
    rocket, engine, environment, physics = get_test_setup()
    drag_at_zero = physics.get_drag(h=0, velocity=0, Rocket=rocket, Environment=environment)
    assert drag_at_zero == 0
    drag_moving = physics.get_drag(h=1000, velocity=50, Rocket=rocket, Environment=environment)
    assert drag_moving < 0

def test_simulation():
    rocket, engine, environment, physics = get_test_setup()
    dt = 0.5
    simulation = Simulation(Rocket=rocket, Environment=environment, Physics=physics, dt=dt)
    
    assert simulation.time == 0
    assert simulation.altitude == 0
    assert simulation.velocity == 0

    simulation.update()
    assert simulation.time == dt
    assert simulation.acceleration != 0

if __name__ == "__main__":
    test_rocket()
    test_engine()
    test_environment()
    test_physics()
    test_simulation()
    print("All unit tests passed successfully.")
