import cv2
import numpy


def find_touch_area(delta_list, point, visited_list):
    if point in visited_list:
        return None

    y, x = point
    delta = delta_list[y][x]

    if delta == 0:
        return None

    visited_list.append(point)

    row_count = len(delta_list)
    column_count = len(delta_list[0])

    if x > 0:
        west_point = (y, x - 1)
        find_touch_area(
            delta_list, west_point, visited_list
        )

    if x < column_count - 1:
        east_point = (y, x + 1)
        find_touch_area(
            delta_list, east_point, visited_list
        )

    if y > 0:
        north_point = (y - 1, x)
        find_touch_area(
            delta_list, north_point, visited_list
        )

        if x > 0:
            northwest_point = (y - 1, x - 1)
            find_touch_area(
                delta_list, northwest_point, visited_list
            )

        if x < column_count - 1:
            northeast_point = (y - 1, x + 1)
            find_touch_area(
                delta_list, northeast_point, visited_list
            )
    if y < row_count - 1:
        south_point = (y + 1, x)
        find_touch_area(
            delta_list, south_point, visited_list
        )

        if x > 0:
            southwest_point = (y + 1, x - 1)
            find_touch_area(
                delta_list, southwest_point, visited_list
            )
        if x < column_count - 1:
            southeast_point = (y + 1, x + 1)
            find_touch_area(
                delta_list, southeast_point, visited_list
            )


def touch_area_from_visited(visited_list):
    if not visited_list:
        return None

    area_x1 = visited_list[0][0]
    area_y1 = visited_list[0][1]

    area_x2 = visited_list[0][0]
    area_y2 = visited_list[0][1]

    for x, y in visited_list:
        if x < area_x1:
            area_x1 = x

        if y < area_y1:
            area_y1 = y

        if x > area_x2:
            area_x2 = x

        if y > area_y2:
            area_y2 = y

    return (area_x1, area_y1, area_x2, area_y2)


def touch_area_midpoint(touch_x1, touch_y1, touch_x2, touch_y2):
    area_x = (touch_x1 + touch_x2) // 2
    area_y = (touch_y1 + touch_y2) // 2

    return (area_x, area_y)


def edge_detect(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Dark and light green colors are in a small range
    green_low = numpy.array((40, 100, 60))
    green_high = numpy.array((70, 255, 200))

    # Get all areas in the image that are green-ish
    green_mask = cv2.inRange(hsv_image, green_low, green_high)

    # Light red is on the low end of the spectrum
    # Dark red is closer to the top, so we ignore it
    red_low = numpy.array((0, 200, 200))
    red_high = numpy.array((10, 255, 255))

    # Get all areas in the image that are light red
    red_mask = cv2.inRange(hsv_image, red_low, red_high)


    red_visited_list = set()
    green_visited_list = set()

    red_points = set()
    green_points = set()

    for x in range(0, image.shape[1], 3):
        for y in range(0, image.shape[0], 3):
            point = (y, x)

            if point not in red_visited_list:
                visited_list = []

                find_touch_area(red_mask, (y, x), visited_list)
                area = touch_area_from_visited(visited_list)

                red_visited_list.update(visited_list)

                if area is not None:
                    red_points.add(touch_area_midpoint(*area))

            if point not in green_visited_list:
                visited_list = []

                find_touch_area(green_mask, (y, x), visited_list)
                area = touch_area_from_visited(visited_list)

                red_visited_list.update(visited_list)

                if area is not None:
                    green_points.add(touch_area_midpoint(*area))

    return set(red_points) | set(green_points)


if __name__=="__main__":
    import sys

    infile = sys.argv[1]
    edges = edge_detect(infile)

    print(edges)
