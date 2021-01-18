class ass:
    def __init__(self, image_list):
        self.images = []
        self.retrieve(image_list)
        self.starttime = None
        self.name = None
    def retrieve(self, image_list):
        import pygame as paygay
        for this in image_list:
            exec('self.' + this[:-4] + ' = paygay.image.load("Ass/" + this)')
            self.images.append(this[:-4])
    def blit(self, screen, image, xy_tuple):
        exec('screen.blit(self.' + image + ', xy_tuple)')
    def pose(self, screen, pose, xy_tuple, tick):
        exec('screen.blit(self.' + self.name + '_' + pose + str(tick) + ', xy_tuple)')



class hatlor_obj(ass):
    def __init__(self, image_list):
        super().__init__(image_list)
        self.name = "hatlor"
