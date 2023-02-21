class Tile:
    def __init__(self, tile_type, sprite_reference, prev_tile_type=None, prev_sprite=None):
        self.tile_type = tile_type
        self.sprite_reference = sprite_reference
        self.prev_tile_type = prev_tile_type
        self.prev_sprite = prev_sprite
    