import svgwrite
from svgwrite import shapes
from Orbit import Orbit

image_size = 600
image_center = (image_size / 2, image_size / 2)
orbit_stroke_width = 3


def get_orbit_ellipse_simple(perihelion, aphelion, semimajor_axis):
    orbit_center = (image_center[0] + semimajor_axis - perihelion), image_center[1]
    orbit = svgwrite.shapes.Ellipse(orbit_center, (aphelion, perihelion))
    orbit.fill('none')
    orbit.stroke('rgb(190, 190, 190)', orbit_stroke_width)
    return orbit


def get_orbit_ellipse(orbit_object: Orbit):
    perihelion = orbit_object.get_periapsis()
    orbit_center = (image_center[0] + orbit_object.semimajor_axis - perihelion), image_center[1]
    orbit = svgwrite.shapes.Ellipse(orbit_center, (orbit_object.get_apoapsis(), perihelion))
    orbit.fill('none')
    orbit.stroke('rgb(190, 190, 190)', orbit_stroke_width)
    orbit.rotate(orbit_object.longitude_of_the_ascending_node, image_center)
    return orbit


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

    mercury_orbit = Orbit("mercury", 0.205630, 57_909_050, 3.38, 48.331, 29.124, 0)
    print(mercury_orbit)
    mercury_orbit_drawing = get_orbit_ellipse(mercury_orbit)
    svg_doc.add(mercury_orbit_drawing)

    venus_orbit = get_orbit_ellipse_simple(107, 109, 108)
    svg_doc.add(venus_orbit)

    earth_orbit = get_orbit_ellipse_simple(147, 152, 150)
    svg_doc.add(earth_orbit)

    mars_orbit = get_orbit_ellipse_simple(207, 249, 228)
    svg_doc.add(mars_orbit)

    jupiter_orbit = get_orbit_ellipse_simple(740, 817, 779)
    svg_doc.add(jupiter_orbit)

    saturn_orbit = get_orbit_ellipse_simple(1353, 1515, 1434)
    svg_doc.add(saturn_orbit)

    uranus_orbit = get_orbit_ellipse_simple(2741, 3004, 2875)
    svg_doc.add(uranus_orbit)

    neptune_orbit = Orbit("neptune", 0.008678, 4_495_060_000, 6.43, 131.784, 276.336, 0)
    print(neptune_orbit)
    neptune_orbit_drawing = get_orbit_ellipse(neptune_orbit)
    svg_doc.add(neptune_orbit_drawing)

    svg_doc.save()
