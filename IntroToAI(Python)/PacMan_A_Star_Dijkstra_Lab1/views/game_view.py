import arcade
import numpy as np

from algos.a_star.a_star import run_a_star
from algos.dijkstra.dijkstra import run_dijkstra
from tile import Tile
from tile_enum import TileEnum
from util import LabyrinthLocation
from views.you_won_view import YouWonView


class GameView(arcade.View):
    """
       Main application class.
       """
    MOVEMENT_SPEED = 50

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Logic
        self.labyrinth = None
        self.score = None
        self.food_counter = None
        self.pacman_location = LabyrinthLocation(-1, -1)
        self.ghosts_locations = None
        # Sprites
        self.pacman = None
        self.walls = None
        self.food_list = None
        self.ghosts = None
        self.pacman_sprite_wrapper = None
        arcade.set_background_color(arcade.csscolor.BLACK)



    def setup(self):
        from pacman import Pacman
        from main import SCREEN_HEIGHT
        """Set up the game here. Call this function to restart the game."""

        self.score = 0
        self.food_counter = 0
        self.labyrinth = []
        self.ghosts_locations = []
        self.pacman_sprite_wrapper = arcade.SpriteList()
        self.walls = arcade.SpriteList()
        self.food_list = arcade.SpriteList()
        self.ghosts = arcade.SpriteList()
        with open("labyrinth.txt") as labyrinth_file:
            for i, line in enumerate(labyrinth_file.readlines()):
                labyrinth_line = []
                for j, tile in enumerate(line):
                    if tile == "*":
                        wall = arcade.Sprite("sprites/wall.png", 50 / 512)
                        wall.center_x = j * 50 + 25
                        wall.center_y = SCREEN_HEIGHT - (i * 50 + 25)
                        self.walls.append(wall)
                        labyrinth_line.append(
                            Tile(
                                tile_type=TileEnum.WALL,
                                sprite_reference=wall
                            )
                        )
                    elif tile == "p":
                        # self.pacman = Pacman("sprites/pacman.png", 50 / 330)
                        self.pacman = Pacman("sprites/fedorus.jpg", 50 / 640)
                        self.pacman.center_x = j * 50 + 25
                        self.pacman.center_y = SCREEN_HEIGHT - (i * 50 + 25)
                        self.pacman_location = LabyrinthLocation(i, j)
                        self.pacman_sprite_wrapper.append(self.pacman)
                        labyrinth_line.append(
                            Tile(
                                tile_type=TileEnum.PACMAN,
                                sprite_reference=self.pacman
                            )
                        )
                    elif tile == "g":
                        # ghost = arcade.Sprite("sprites/red.png", 50 / 512)
                        ghost = arcade.Sprite("sprites/kaneki.jpg", 50 / 500)
                        ghost.center_x = j * 50 + 25
                        ghost.center_y = SCREEN_HEIGHT - (i * 50 + 25)
                        self.ghosts.append(ghost)
                        self.ghosts_locations.append(LabyrinthLocation(i, j))
                        labyrinth_line.append(
                            Tile(
                                tile_type=TileEnum.GHOST,
                                sprite_reference=ghost
                            )
                        )
                    elif tile == "f":
                        food = arcade.Sprite("sprites/beer.png", 50 / 2000)
                        food.center_x = j * 50 + 25
                        food.center_y = SCREEN_HEIGHT - (i * 50 + 25)
                        self.food_list.append(food)
                        labyrinth_line.append(
                            Tile(
                                tile_type=TileEnum.FOOD,
                                sprite_reference=food
                            )
                        )
                        self.food_counter += 1
                    elif tile == " ":
                        labyrinth_line.append(
                            Tile(
                                tile_type=TileEnum.EMPTY,
                                sprite_reference=None
                            )
                        )
                self.labyrinth.append(labyrinth_line)

    def print_labyrinth(self):
        for line in self.labyrinth:
            for tile in line:
                if tile.tile_type == TileEnum.EMPTY:
                    print(" ", end=" ")
                elif tile.tile_type == TileEnum.GHOST:
                    print("G", end=" ")
                elif tile.tile_type == TileEnum.WALL:
                    print("*", end=" ")
                elif tile.tile_type == TileEnum.PACMAN:
                    print("P", end=" ")
                elif tile.tile_type == TileEnum.FOOD:
                    print("F", end=" ")
            print()

    def on_draw(self):
        """Render the screen."""
        self.clear()

        self.pacman_sprite_wrapper.draw()
        self.walls.draw()
        img = arcade.load_texture('sprites/epam.png')
        arcade.draw_texture_rectangle(500, 540, 200, 100, img)
        self.food_list.draw()
        self.ghosts.draw()


    def on_update(self, delta_time):
        """ Movement and game logic """
        from views.game_over_view import GameOverView
        for ghost_location in self.ghosts_locations:
            # result = run_a_star(
            #     ghost_location=ghost_location,
            #     target=self.pacman_location,
            #     labyrinth=self.labyrinth
            # )
            result = run_dijkstra(
                ghost_location=ghost_location,
                target=self.pacman_location,
                labyrinth=self.labyrinth
            )
            ghost_sprite = self.labyrinth[ghost_location.i][ghost_location.j].sprite_reference
            self.labyrinth[ghost_location.i][ghost_location.j] = Tile(
                tile_type=self.labyrinth[ghost_location.i][ghost_location.j].prev_tile_type or TileEnum.EMPTY,
                sprite_reference=self.labyrinth[ghost_location.i][ghost_location.j].prev_sprite or None
            )
            delta_i = result[1].i - ghost_location.i
            delta_j = result[1].j - ghost_location.j
            ghost_location.update_location(delta_i=delta_i, delta_j=delta_j)
            self.labyrinth[ghost_location.i][ghost_location.j] = Tile(
                tile_type=TileEnum.GHOST,
                sprite_reference=ghost_sprite,
                prev_tile_type=self.labyrinth[ghost_location.i][ghost_location.j].tile_type,
                prev_sprite=self.labyrinth[ghost_location.i][ghost_location.j].sprite_reference
            )
            if delta_i > 0:
                ghost_sprite.change_x = 0
                ghost_sprite.change_y = -self.MOVEMENT_SPEED
            elif delta_i < 0:
                ghost_sprite.change_x = 0
                ghost_sprite.change_y = self.MOVEMENT_SPEED
            elif delta_j > 0:
                ghost_sprite.change_x = self.MOVEMENT_SPEED
                ghost_sprite.change_y = 0
            elif delta_j < 0:
                ghost_sprite.change_x = -self.MOVEMENT_SPEED
                ghost_sprite.change_y = 0
            else:
                ghost_sprite.change_x = 0
                ghost_sprite.change_y = 0

        self.ghosts.update()
        # Move the player
        j_index_delta = int(np.sign(self.pacman.change_x))
        i_index_delta = int(np.sign(self.pacman.change_y)) * (-1)
        if self._pacman_will_hit_wall(i_index_delta, j_index_delta):
            self.pacman.change_x = 0
            self.pacman.change_y = 0
        elif self._pacman_will_find_food(i_index_delta, j_index_delta):
            self.score += 1
            self.food_counter -= 1
            self.move_pacman_through_labyrinth(i_index_delta, j_index_delta)
            if self.food_counter == 0:
                self.window.show_view(YouWonView(score=self.score))
        elif self._pacman_will_hit_ghost(i_index_delta, j_index_delta):
            self.window.show_view(GameOverView(score=self.score))
        elif j_index_delta != 0 or i_index_delta != 0:
            self.move_pacman_through_labyrinth(i_index_delta, j_index_delta)

        self.pacman_sprite_wrapper.update()


        self.food_list.update()

        self.print_labyrinth()
        print(self.score)

    def _pacman_will_hit_ghost(self, i_index_delta, j_index_delta):
        return self.labyrinth[self.pacman_location.i][self.pacman_location.j + j_index_delta].tile_type is \
            TileEnum.GHOST \
            or self.labyrinth[self.pacman_location.i + i_index_delta][self.pacman_location.j].tile_type is \
            TileEnum.GHOST

    def _pacman_will_find_food(self, i_index_delta, j_index_delta):
        return self.labyrinth[self.pacman_location.i][self.pacman_location.j + j_index_delta].tile_type is TileEnum.FOOD \
            or self.labyrinth[self.pacman_location.i + i_index_delta][self.pacman_location.j].tile_type is TileEnum.FOOD

    def _pacman_will_hit_wall(self, i_index_delta, j_index_delta):
        return self.labyrinth[self.pacman_location.i][self.pacman_location.j + j_index_delta].tile_type is \
            TileEnum.WALL \
            or self.labyrinth[self.pacman_location.i + i_index_delta][self.pacman_location.j].tile_type is TileEnum.WALL

    def move_pacman_through_labyrinth(self, i_index_delta, j_index_delta):
        self.labyrinth[self.pacman_location.i][self.pacman_location.j] = Tile(
            tile_type=TileEnum.EMPTY,
            sprite_reference=None
        )
        self.pacman_location.update_location(delta_i=i_index_delta, delta_j=j_index_delta)
        if self.labyrinth[self.pacman_location.i][self.pacman_location.j].sprite_reference:
            self.labyrinth[self.pacman_location.i][self.pacman_location.j].sprite_reference.remove_from_sprite_lists()
        self.labyrinth[self.pacman_location.i][self.pacman_location.j] = Tile(
                tile_type=TileEnum.PACMAN,
                sprite_reference=self.pacman
        )


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # If the player presses a key, update the speed
        if key == arcade.key.UP:
            self.pacman.change_x = 0
            self.pacman.change_y = self.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.pacman.change_x = 0
            self.pacman.change_y = -self.MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.pacman.change_x = -self.MOVEMENT_SPEED
            self.pacman.change_y = 0
        elif key == arcade.key.RIGHT:
            self.pacman.change_x = self.MOVEMENT_SPEED
            self.pacman.change_y = 0
