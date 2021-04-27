import svgwrite
from svgwrite import shapes
from svgwrite.params import Parameter

from Orbit import Orbit
from Orbit import solar_system_orbits

image_size = 600
image_center = (image_size / 2, image_size / 2)
orbit_stroke_width = 3
scale = 1 / 1_000_000


def get_orbit_ellipse_simple(perihelion, aphelion, semimajor_axis):
    orbit_center = (image_center[0] + semimajor_axis - perihelion), image_center[1]
    orbit = svgwrite.shapes.Ellipse(orbit_center, (aphelion, perihelion))
    orbit.fill('none')
    orbit.stroke('rgb(190, 190, 190)', orbit_stroke_width)
    return orbit


def get_orbit_ellipse(orbit_object: Orbit):
    orbit_center = ((image_center[0] + (orbit_object.semimajor_axis - orbit_object.get_periapsis()) * scale),
                    image_center[1])

    # Semimajor axis and eccentricity
    orbit_ellipse = svgwrite.shapes.Ellipse((0, 0),
                                            (orbit_object.get_apoapsis() * scale, orbit_object.get_periapsis() * scale))

    # longitude of the ascending node
    orbit_ellipse.rotate(orbit_object.longitude_of_the_ascending_node, image_center)

    # replacing to the center
    orbit_ellipse.translate(orbit_center[0], orbit_center[1])

    # inclination
    inclination_scale = 1 - abs(orbit_object.inclination) / 90
    print("Scaling x by {} due to inclination of {}".format(inclination_scale, orbit_object.inclination))
    orbit_ellipse.scale(inclination_scale, 1)

    # graphics
    orbit_ellipse.fill('none')
    orbit_ellipse.stroke('rgb(190, 190, 190)', orbit_stroke_width, opacity=0.6)
    return orbit_ellipse


if __name__ == '__main__':
    # this will work with svgwrite
    svg_doc = svgwrite.Drawing(filename="../../output/scribble.svg",
                               size=(image_size, image_size))
    svg_doc.add(svg_doc.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='rgb(50,50,50)'))

    diameter_sun = 1.4
    drawn_radius_sun = diameter_sun / 2 * 25
    sun_shape = svgwrite.shapes.Ellipse(image_center, (drawn_radius_sun, drawn_radius_sun))
    sun_shape.fill('yellow')
    svg_doc.add(sun_shape)

    for solar_orbit in solar_system_orbits:
        print(solar_orbit)
        orbit_drawing = get_orbit_ellipse(solar_orbit)
        svg_doc.add(orbit_drawing)

    svg_doc.save()
