"""gaurav"""
import collectable_objects
class Cakes(collectable_objects.Collectables):
    """gaurav"""
    def __init__(self):
        collectable_objects.Collectables.__init__(self)
        self.char = "@"
        self.cake_position = []

    def set_position(self, yawn, xarg):
        """gaurav"""
        self.cake_position.append([yawn, xarg, False])
