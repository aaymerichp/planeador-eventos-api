from geopy.distance import great_circle

class ServiceController():

    @staticmethod
    def get_latlng_bounderies(lat, lng, distance):
        """
        Return min/max lat/lng values for a distance around a latlng.
        :lat:, :lng: the center of the area.
        :distance: in km, the "radius" around the center point.
        :returns: Two corner points of a square that contains the circle,
                  lat_min, lng_min, lat_max, lng_max.+
        """
        gc = great_circle(kilometers=distance)
        p0 = gc.destination((lat, lng), 0)
        p90 = gc.destination((lat, lng), 90)
        p180 = gc.destination((lat, lng), 180)
        p270 = gc.destination((lat, lng), 270)

        ret = p180[0], p270[1], p0[0], p90[1]
        return ret