class ticksync_obj:
    def __init__(self):
        self.tick = 1; self.basetime = 0.0
    def update(self, time, speed = 0.13):
        self.keeptime = time - self.basetime
        if self.keeptime > speed:
            self.tick += 1
            if self.tick == 4:
                self.tick = 1
            self.keeptime = 0.0; self.basetime = time
