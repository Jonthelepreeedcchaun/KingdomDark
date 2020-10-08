class input_object:
    def __init__(self, jsondata):
        import pygame as pg
        self.keydict = {}
        for this in ['mx', 'my', 'm1', 'm2', 'm3', 't1', 't2', 't3', 't1_v', 't2_v', 't3_v']:
            exec('self.' + this + ' = 0')
        self.mouse_over_list = []
        self.mouse_over = None
        for this in jsondata.keys:
            exec('self.' + jsondata.keys[this] + ' = 0')
            exec('self.' + jsondata.keys[this] + '_t = 0')
            self.keydict.update({jsondata.keys[this]: 0})
        self.intkeys = []
        for this in jsondata.keys:
            self.intkeys.append(int(this))
        self.screenlist = [(0, 0), pg.FULLSCREEN]; self.screenlist_v = [(69, 420), pg.RESIZABLE]
    def update(self, jsondata, screen):
        import pygame as pg
        if not self.screenlist == self.screenlist_v: screen = pg.display.set_mode(*self.screenlist)
        self.screenlist_v = self.screenlist
        if len(self.mouse_over_list) > 1:
            while len(self.mouse_over_list) > 1:
                self.mouse_over_list.remove(self.mouse_over_list[0])
            self.mouse_over = self.mouse_over_list[0]
        if len(self.mouse_over_list) == 0:
            self.mouse_over = None
        self.mx, self.my = pg.mouse.get_pos()
        self.m1, self.m3, self.m2 = pg.mouse.get_pressed()
        for this in ['t1', 't2', 't3']:
            exec('self.' + this + ' = 0')
        if self.m1 and not self.t1_v: self.t1 = 1; self.t1_v = 1
        if not self.m1: self.t1_v = 0
        if self.m3 and not self.t3_v: self.t3 = 1; self.t3_v = 1
        if not self.m3: self.t3_v = 0
        if self.m2 and not self.t2_v: self.t2 = 1; self.t2_v = 1
        if not self.m2: self.t2_v = 0
        for this in jsondata.keys:
            exec('self.' + jsondata.keys[this] + '_t = 0')
        for this in pg.event.get():
            if this.type == pg.KEYDOWN:
                if this.key in self.intkeys:
                    exec('self.' + jsondata.keys[str(this.key)] + ' = 1')
                    exec('self.' + jsondata.keys[str(this.key)] + '_t = 1')
                    self.keydict.update({jsondata.keys[str(this.key)]: 1})
            if this.type == pg.KEYUP:
                if this.key in self.intkeys:
                    exec('self.' + jsondata.keys[str(this.key)] + ' = 0')
                    self.keydict.update({jsondata.keys[str(this.key)]: 0})
            if this.type == pg.VIDEORESIZE:
                if not self.screenlist[1] == pg.FULLSCREEN: screen = pg.display.set_mode((this.w, this.h), pg.RESIZABLE)
        if self.F11_t:
            if self.screenlist[1] == pg.FULLSCREEN: self.screenlist = [(900, 600), pg.RESIZABLE]
            elif self.screenlist[1] == pg.RESIZABLE: self.screenlist = [(1920, 1080), pg.FULLSCREEN]
