def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(screen, text, x, y, size, color):
    import pygame as pg
    largeText = pg.font.Font(None, size)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = (x, y)
    screen.blit(TextSurf, TextRect)
    dimension = largeText.render(text, True, color).get_rect()
    return(TextRect)

class text_box:
    def __init__(self):
        self.clear()
    def clear(self):
        self.linedict = None
    def RnD(self, screen, input, text, x, y, x_len, time, speed = 1, size = 40, color = (255, 255, 255)):
        if self.linedict == None:
            self.render(screen, text, x, y, x_len, size, color)
            self.timestart = time; self.timelist = []; self.line = 0; self.word = "arbitrary string :)"
            self.donewriting = False
            self.display(screen, input, x, y, time, speed, size, color)
        else:
            self.display(screen, input, x, y, time, speed, size, color)
    def render(self, screen, text, x, y, x_len, size, color):
        wordlist = []; word = ""
        for this in text:
            if this != " ":
                word += this
            else:
                word += " "
                wordlist.append(word); word = ""
        wordlist.append(word)
        linedict = {}; word = ""; line = 0 # note to self: the variable word is not a word, but the line of words being displayed
        for thing in wordlist:
            word += thing
            local_x = message_display(screen, word, x, y, size, color).right
            if (local_x - x) >= x_len:
                word = word[:-len(thing)] # this is madness
                linedict[word] = line
                line += 1; word = thing
        linedict[word] = line
        self.linedict = linedict # {"im mr worldwide": 0, "star thats so cool": 1}
        self.linelist = []
        for this in self.linedict:
            self.linelist.append(this)
    def display(self, screen, input, x, y, time, speed, size, color):
        localtime = time - self.timestart
        if not int(int(localtime * 10)/speed) in self.timelist:
            self.timelist.append(int(int(localtime * 10)/speed))
            try:
                self.word = self.linelist[self.line]
                self.writing_line = self.word[: -(len(self.word) - len(self.timelist))]
            except:
                self.line += 1
                self.donewriting = True
            if len(self.word) == len(self.timelist) and len(self.linelist) > self.line:
                self.timelist = []; self.line += 1
        for this in self.linedict:
            if self.line > self.linedict[this]:
                message_display(screen, this, x, y + self.linedict[this] * size, size, color)
        if not self.donewriting:
            message_display(screen, self.writing_line, x, y + self.line * size, size, color)
        if input.t1:
            if self.donewriting:
                self.clear()
            else:
                self.line += 1
