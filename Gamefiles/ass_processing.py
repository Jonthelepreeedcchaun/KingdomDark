class ass:
    def __init__(self, image_list):
        self.images = []
        self.retrieve(image_list)
    def retrieve(self, image_list):
        import pygame as paygay
        for this in image_list:
            exec('self.' + this[:-4] + ' = paygay.image.load("Ass/" + this)')
            self.images.append(this[:-4])
    def blit(self, screen, image, xy_tuple):
        import pygame as Somebody_once_told_me_the_world_is_gonna_roll_me
        exec('screen.blit(self.' + image + ', xy_tuple)')

class hatlor_obj(ass):
    def __init__(self, image_list):
        super().__init__(image_list)
