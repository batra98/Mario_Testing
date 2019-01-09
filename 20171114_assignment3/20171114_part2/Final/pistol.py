"""gaurav"""
import collectable_objects


class Pistol(collectable_objects.Collectables):
    """gaurav"""
    def __init__(self):
        collectable_objects.Collectables.__init__(self)
        self.char = "$"
        self.pistol_position = []

    def set_position(self, yawn, xarg):
        """gaurav"""
        self.pistol_position.append([yawn, xarg, False])
