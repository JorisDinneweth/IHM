from graphic_objects.label import Label
from graphic_objects.timer import Timer
from graphic_objects.slider_h import SliderH
from graphic_objects.slider_v import SliderV
from games.model import Model
import settings


class FiguresGameM(Model):
    def __init__(self):
        Model.__init__(self)
        self.figures, self.objective, self.solution = [], None, []
        self.available_figures = []
        self.user_entries = []
        self.delete_buttons = []
        self.expected_operations = []
        self.operators = []

        self.input = ""
        self.label = Label((0, 0), "", (0, 0))

        self.draft_slider = SliderH((0, settings.win_height // 1.3), "TIRAGE", settings.win_width * .7)
        self.result_slider = SliderH((self.draft_slider.white_band.get_width(),
                                      settings.win_height // 1.3),
                                     "OBJECTIF", settings.win_width * .3)
        self.slider_v_bottom = SliderV((settings.win_width * .7, settings.win_height // 1.3),
                                       settings.win_height // 1.3)
        self.slider_v_top = SliderV((settings.win_width // 2, 0), settings.win_height // 3)
        self.timer = Timer((settings.win_width - int(Timer.radius * 1.5), int(Timer.radius * 1.5)), 45)
