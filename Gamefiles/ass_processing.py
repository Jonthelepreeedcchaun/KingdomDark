class ass:
    def __init__(self, image_list):
        self.images = []
        self.retrieve(image_list)
        self.starttime = None
        self.name = None
        self.poses = []
    def retrieve(self, image_list, path = 'Ass/'):
        import pygame as paygay
        for this in image_list:
            exec('self.' + this[:-4] + ' = paygay.image.load(path + this)')
            self.images.append(this[:-4])
    def blit(self, screen, image, xy_tuple):
        exec('screen.blit(self.' + image + ', xy_tuple)')
    def pose(self, screen, oxygen, pose, xy_tuple, tick, weight = 1):
        paralax_x, paralax_y = oxygen.paralax_x, oxygen.paralax_y
        exec('screen.blit(self.' + self.name + '_' + pose + str(tick) + ', (xy_tuple[0] + paralax_x/weight, xy_tuple[1] + paralax_y/weight))')

class hatlor_obj(ass):
    def __init__(self, image_list):
        super().__init__(image_list)
        self.name = "hatlor"

class gen_obj(ass):
    def __init__(self, image_list):
        super().__init__(image_list)
        self.name = image_list[0][:-8] # this cuts off the "_be1.png" part of gen objs
