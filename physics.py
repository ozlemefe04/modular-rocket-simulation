from rocket import Rocket
from environment import Environment

class Physics:
      def get_drag(self, h, velocity, Rocket, Environment):
           air_density = Environment.get_air_density(h)
           area = Rocket.get_area()
           Cd= Rocket.Cd
           return - 0.5 * air_density * velocity * abs(velocity) * Cd * area


      def get_fnet (self, h , velocity , mass ,time, Rocket, Environment):
           fnet = Rocket.engine.get_thrust(time) + self.get_drag(h, velocity, Rocket, Environment) - mass*Environment.get_gravity(h)
           return fnet


      def get_acceleration(self, h, velocity, mass, time, Rocket,  Environment):
           return self.get_fnet( h , velocity , mass ,time, Rocket, Environment) / mass

      def get_velocity(self, velocity, acceleration ,dt):
           return velocity + acceleration * dt

      def get_altitude(self, altitude, velocity, dt):
           return altitude + velocity * dt

