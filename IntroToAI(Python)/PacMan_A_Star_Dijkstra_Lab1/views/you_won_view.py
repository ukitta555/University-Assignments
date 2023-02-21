import arcade


class YouWonView(arcade.View):
    def __init__(self, score):
        super().__init__()
        self.score = score

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        from main import SCREEN_WIDTH
        self.clear()
        """
        Draw "You won!" across the screen.
        """
        arcade.draw_text(f"Ультрахарош",
                         SCREEN_WIDTH / 2,
                         400,
                         arcade.color.WHITE,
                         font_size=54,
                         anchor_x="center")
        arcade.draw_text(f"Тобі лишилося написати 13 лаб до отримання диплому",
                         SCREEN_WIDTH / 2,
                         300,
                         arcade.color.WHITE,
                         font_size=24,
                         anchor_x="center")

        arcade.draw_text(f"Score: {self.score}",
                         SCREEN_WIDTH / 2,
                         200,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")
        img = arcade.load_texture('sprites/shelby.jpg')
        arcade.draw_texture_rectangle(500, 750, 1000, 500, img)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        from views.game_view import GameView
        game_view = GameView()
        game_view.window.set_update_rate(1/4)
        game_view.setup()
        self.window.show_view(game_view)
