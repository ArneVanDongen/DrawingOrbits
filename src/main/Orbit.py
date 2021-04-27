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


solar_system_orbits = [Orbit("mercury", 0.205630, 57_909_050, 3.38, 48.331, 29.124, 0),
                       Orbit("venus", 0.00677323, 108_209_000, 3.395, 76.68069, 54.884, 0),
                       Orbit("earth", 0.01671022, 149_596_000, 0.00005, -11.26064, 114.20783, 0),
                       Orbit("mars", 0.09341233, 227_923_000, 1.85061, 49.57854, 286.4623, 0),
                       Orbit("jupiter", 0.04839266, 778_570_000, 1.30530, 100.55615, 85.8023, 0),
                       Orbit("saturn", 0.05415060, 1_433_529_000, 2.48446, 113.71504, 21.2831, 0),
                       Orbit("uranus", 0.04716771, 2_872_463_000, 0.76986, 74.22988, -96.73436, 0),
                       Orbit("neptune", 0.008678, 4_495_060_000, 6.43, 131.784, 276.336, 0)]
