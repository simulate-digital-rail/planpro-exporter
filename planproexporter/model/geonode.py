import uuid


class GeoNode(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.geo_point_uuid = str(uuid.uuid4())
        self.geo_node_uuid = str(uuid.uuid4())

    def get_uuids(self):
        return [self.geo_point_uuid, self.geo_node_uuid]

