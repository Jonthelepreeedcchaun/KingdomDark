from Gamefiles.ass_processing import ass; import os

class mouse_obj(ass):
    def __init__(self, image_list = os.listdir('Ass/Cursor/'), path = 'Ass/Cursor/'):
        super().__init__(image_list, path)
        self.x, self.y = 0, 0
        self.rect_list = []
    def curse(self, screen, input, tick, speed = 3):
        self.x += (input.mx - self.x)/speed
        self.y += (input.my - self.y)/speed
        self.blit(screen, 'cursor' + str(tick), (input.mx, input.my))
    def rect_intake(self, screen, input):
        self.rect_over = None
        if len(self.rect_list) > 0:
            self.rect_over = self.rect_list[0]
        self.rect_list = []
        if self.rect_over != None:
            self.blit(screen, 'asterisk', (input.mx, input.my))
