from rocket import Rocket
from environment import Environment
from physics import Physics


class Simulation:
     def __init__(self, Rocket, Environment, dt, Physics):
          self.rocket = Rocket
          self.environment = Environment
          self.dt= dt
          self.physics = Physics
          self.engine = self.rocket.engine

          if not (isinstance(self.dt, (int,float)) and self.dt > 0):
               raise ValueError("Time step must be a positive number.")

          self.time = 0
          self.altitude = 0
          self.velocity = 0
          self.acceleration = 0

     def get_state(self):
        state = self.__dict__.copy()
        state["mass"] = self.rocket.get_mass()
        state.pop('rocket', None)
        state.pop('environment', None) 
        state.pop("physics", None)
        state.pop("engine", None)
        return state

     def update(self):
        self.fuel = self.engine.consume_fuel( self.rocket, self.dt, self.time)
        self.acceleration = self.physics.get_acceleration(self.altitude, self.velocity, self.rocket.get_mass(), self.time, self.rocket, self.environment)
        self.velocity += self.acceleration * self.dt 
        self.altitude+= self.velocity * self.dt
        if self.altitude <0:
            self.altitude=0
            self.velocity=0
        self.time += self.dt 


     def run(self, max_time):
        time_history = []
        altitude_history = []
        velocity_history = []
        acceleration_history = []
        while self.time < max_time and self.altitude >= 0:
            self.update()
            
            time_history.append(self.time)
            altitude_history.append(self.altitude)
            velocity_history.append(self.velocity)
            acceleration_history.append(self.acceleration)

            state=self.get_state()
            state["mass"]= self.rocket.dry_mass + self.rocket.fuel_mass
            if self.time > self.dt and self.altitude==0:
                break
            else:
                print(state)
                print(self.time, self.rocket.fuel_mass, self.rocket.get_mass())

        self.max_altitude = max(altitude_history)
        altitude = altitude_history.index(self.max_altitude)
        self.time_altitude = time_history[altitude]

        self.max_velocity= max(velocity_history)
        velocity = velocity_history.index(self.max_velocity)
        self.time_velocity = time_history[velocity]

        self.max_acceleration= max(acceleration_history)
        acceleration = acceleration_history.index(self.max_acceleration)
        self.time_acceleration = time_history[acceleration]

        self.last=time_history[-1]

    