class UI_obj():
    def __init__(self, jsondata):
        import pygame as pg
        for this in jsondata.UI:
            exec('self.' + this[:-4] + ' = {"img": pg.image.load("UI/" + this), "x_pos": jsondata.UI[this]["x_pos"]}')
        self.toolbar_y_pos = -20
        self.windows = {}
    def draw(self, jsondata, input, screen):
        import pygame as pg; from Structure.windows import window as w
        for this in jsondata.UI:
            exec('self.' + this[:-4] + '_img = screen.blit(self.' + this[:-4] + '["img"], (self.' + this[:-4] + '["x_pos"], self.toolbar_y_pos))')
        if input.my <= 33 and self.toolbar_y_pos < 0:
            self.show()
        elif input.my > 33 and self.toolbar_y_pos > -20:
            self.hide()
        if self.settings_img.collidepoint(input.mx, input.my): input.mouse_over_list.append('settings')
        if 'settings' == input.mouse_over and input.t1:
            if not 'Settings' in self.windows:
                self.windows.update({'Settings': None})
            else:
                del self.windows['Settings']
        for this in self.windows:
            if self.windows[this] == None:
                self.windows[this] = w(jsondata, input, screen, this, self)
            else:
                self.windows[this].draw(jsondata, input, screen, this, self)
        if hasattr(self, 'delete_window'):
            del self.windows[self.delete_window]
            delattr(self, 'delete_window')
    def show(self):
        if self.toolbar_y_pos < 0:
            self.toolbar_y_pos += 1
    def hide(self):
        if self.toolbar_y_pos > -20:
            self.toolbar_y_pos -= 1
