if __name__ == '__main__':
    import sys
    sys.path.append("../../")

import numpy as np

from pypo.scene.entity import Entity
from pypo.scene.component.color import ColorComponent
from pypo.scene.component.position import PositionComponent

class Registry(object):
    """
    Registry is a container class that handles
    entity created during lifetime of application
    and their associated components.

    Sparse set is used to provide a cache efficient
    implementation.

    __slots__ is not used here to allow flexibility and maintaining in the future.
    Furthermore the memory saved by __slots__ in registry won't provide a huge improvement
    for further applications.

    Numpy is used to reduce memory overhead due to Python internal implementation for object.
    """

    def __init__(self):
        # Reserve list for sparse set

        # TODO: Instead of reserving the whole list, numpy should be used to mimick std::vector behavior
        self._entity_list    = np.full(Entity.MAX_ENTITY_ID, Entity.INVALID)

        self._components     = {}

        # TODO: Entity ID shouldn't be an incremental counter instead ID should
        # be computed over length of the entity list.
        self._entity_id_counter   = 0
        
        # Set of entity id being available due to removal in the sparse set
        self._destroyed = None

    def _get_new_entity_id(self):
        """
        Get a new entity identifier by reusing available
        ones if possible. This allow to save extra memory instead of
        always incrementing internal counter.
        """
        # TODO: Maybe use another method for generating entity ID.
        # I'm not sure this is the most efficient way to handle ID.
        if self._entity_id_counter > Entity.MAX_ENTITY_ID:
            raise AttributeError("Maximum number of entity reached.")

        if self._available_entity_id:
            entity_id = self._available_entity_id.pop()
            return entity_id
            
        entity_id = self._entity_id_counter
        self._entity_id_counter += 1

        return entity_id

    def create_entity(self, *components):
        """
        Creates an entity and add it to internal structures.
        
        If entity can't be created because no ID is available
        for usage then an invalid entity is returned.

        :returns:   entity_id
        :rtype:     Entity
        """
        # Create a new entity and generate a new entity id
        entity = Entity()
        
        try:
            entity.entity_id = self._get_new_entity_id()
        except AttributeError:
            # TODO: Log this exception to a logger, would be beneficial
            # for debugging.
            return entity

        self.add_component(entity, components)

        return entity

    def add_shared_component(self, entity, components = []):
        """
        Adds shared components to a specific entity.

        Shared components are useful to save memory space
        by reusing reference to a list of already existing 
        components.

        MeshComponent for instance can be shared with such a method,
        this would avoid to affect an extra component for
        each entity using same one.
        
        :param      entity:      The entity
        :type       entity:      Entity
        :param      components:  The components
        :type       components:  Array
        """
        pass

    def add_component(self, entity, components = []):
        """
        Adds components to a specific entity.
        
        :param      entity:      The entity
        :type       entity:      Entity
        :param      components:  List of components
        :type       components:  Array
        """
        for component in components:
            component_type = component.__class__.__name__
            
            if component_type not in self._components:
                self._components[component_type] = component

    def remove_component(self, entity, components = []):
        """
        Removes components to a specific entity.
        
        :param      entity:      The entity
        :type       entity:      Entity
        :param      components:  List of components
        :type       components:  Array
        """
        pass

    def destroy_entity(self, entity):
        """
        Destroy entity and remove its presence from internal structures.
        
        :param      entity:  The entity
        :type       entity:  Entity
        """
        pass

if __name__ == '__main__':
    # Demonstrate how to create a entity with few components
    color    = ColorComponent()
    position = PositionComponent()
    
    r        = Registry()
    r.create_entity(color, position)

    import scipy.fft
    import time
    a = np.random.randint(0, 10240, size = (512,512,24,12))
    scipy.fft.fft(a, 24, axis = 2, workers = -1)
    # time.sleep(5)