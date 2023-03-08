import arcade

from main import SCREEN_WIDTH


class GameOverView(arcade.View):
    def __init__(self, score):
        super().__init__()
        self.score = score

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text(f"Факультет кібернетики",
                         SCREEN_WIDTH / 2,
                         400,
                         arcade.color.WHITE,
                         font_size=54,
                         anchor_x="center")
        arcade.draw_text(f"Нижній текст",
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
        img = arcade.load_texture('sprites/jackiechan.jpg')
        arcade.draw_texture_rectangle(500, 750, 1000, 500, img)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        from views.game_view import GameView
        game_view = GameView()
        game_view.window.set_update_rate(1/4)
        game_view.setup()
        self.window.show_view(game_view)