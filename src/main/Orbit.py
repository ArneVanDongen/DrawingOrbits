class Orbit:

    def __init__(self, name, eccentricity, semimajor_axis, inclination, longitude_of_the_ascending_node,
                 argument_of_periapsis, true_anomaly):
        self.name = name
        self.eccentricity = eccentricity
        self.semimajor_axis = semimajor_axis
        self.inclination = inclination
        self.longitude_of_the_ascending_node = longitude_of_the_ascending_node
        self.argument_of_periapsis = argument_of_periapsis
        self.true_anomaly = true_anomaly

    def get_periapsis(self):
        return self.semimajor_axis * (1 - self.eccentricity)

    def get_apoapsis(self):
        return self.semimajor_axis * (1 + self.eccentricity)

    def __str__(self):
        return "[Orbit of {} - e:{:.1f} a:{:.1f} i:{:.1f} O:{:.1f} w:{:.1f} v:{:.1f}]" \
            .format(self.name,
                    self.eccentricity,
                    self.semimajor_axis,
                    self.inclination,
                    self.longitude_of_the_ascending_node,
                    self.argument_of_periapsis,
                    self.true_anomaly)
