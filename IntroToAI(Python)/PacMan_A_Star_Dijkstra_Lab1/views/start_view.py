import arcade


class StartView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def play_song(self):
        self.music = arcade.Sound("soundtrack.mp3")
        self.current_player = self.music.play(1, loop=True, speed=1.0)

    def setup(self):
        self.play_song()

    def on_draw(self):
        from main import SCREEN_WIDTH
        self.clear()
        arcade.draw_text(f"Допоможіть аспіранту випити все пиво",
                         SCREEN_WIDTH / 2,
                         400,
                         arcade.color.WHITE,
                         font_size=24,
                         anchor_x="center")
        arcade.draw_text(f"і не приймати лаби в студентів!",
                         SCREEN_WIDTH / 2,
                         300,
                         arcade.color.WHITE,
                         font_size=24,
                         anchor_x="center")

        arcade.draw_text(f"Клацніть щоб продовжити...",
                         SCREEN_WIDTH / 2,
                         200,
                         arcade.color.WHITE,
                         font_size=24,
                         anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        from views.game_view import GameView
        game_view = GameView()
        game_view.window.set_update_rate(1/4)
        game_view.setup()
        self.window.show_view(game_view)
