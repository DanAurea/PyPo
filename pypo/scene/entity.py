# TODO: Entity as an object add an unwanted overhead, entity should be an "abstract" type
# that is simply an encoded integer. 

class Entity(object):
    """
    Entities are related to collection of components and define 
    in an indirect way objects that can be found in a world.
    """
    __slots__ = [ "entity_id", "version"]

    N_BIT_ID      = 24
    N_BIT_VERSION = 8

    MAX_ENTITY_ID = (2 ** N_BIT_ID) - 1
    MAX_VERSION   = (2 ** N_BIT_VERSION) - 1

    INVALID       = MAX_ENTITY_ID

    def __init__(self, entity_id = INVALID, version = 0):
        self.entity_id = entity_id
        self.version   = version

    def get_entity_id_version(self):
        return (self.entity_id, self.version)

    def get_entity_id(self):
        return self.entity_id

    def get_version(self):
        return version

    def __repr__(self):
        s = '''
            ID      : {}
            Version : {}
            '''.format  (
                            self.entity_id,
                            self.version,
                        )

        return s