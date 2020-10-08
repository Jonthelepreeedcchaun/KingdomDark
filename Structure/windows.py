def text_objects(text, font, color = (255, 255, 255)):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
def message_display(screen, text, x, y, size, color):
    import pygame as pg
    largeText = pg.font.Font(None, size)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.topleft = (x, y)
    screen.blit(TextSurf, TextRect)
    dimension = largeText.render(text, True, color).get_rect()
    return(TextRect)
class window:
    def __init__(self, jsondata, input, screen, key, UI):
        import pygame as pg, random
        self.X_img = pg.image.load('UI/X.png'); self.move = 0
        self.x_pos = random.randint(100, 1560); self.y_pos = random.randint(100, 680)
        self.x_len = 300; self.y_len = 300
        if self.y_pos < 0:
            self.y_pos = 0
    def draw(self, jsondata, input, screen, key, UI):
        import pygame as pg
        bar = pg.draw.rect(screen, (185, 185, 185), (self.x_pos, self.y_pos, self.x_len, 16))
        box = pg.draw.rect(screen, (115, 115, 115), (self.x_pos, self.y_pos + 16, self.x_len, self.y_len))
        X = screen.blit(self.X_img, (self.x_pos + self.x_len - 14, self.y_pos + 2))
        message_display(screen, key, self.x_pos, self.y_pos, 22, (0, 0, 0))
        if bar.collidepoint(input.mx, input.my): input.mouse_over_list.append('bar')
        if X.collidepoint(input.mx, input.my): input.mouse_over_list.append('X')
        if 'bar' == input.mouse_over and input.t1:
            self.pos_diff = (input.mx - self.x_pos, input.my - self.y_pos)
            self.move = 1
        if self.move and not input.m1:
            delattr(self, 'pos_diff')
            self.move = 0
        if self.move:
            self.x_pos = input.mx - self.pos_diff[0]
            self.y_pos = input.my - self.pos_diff[1]
        if 'X' == input.mouse_over and input.m1:
            self.exit(key, UI)
    def exit(self, key, UI):
        UI.delete_window = key
