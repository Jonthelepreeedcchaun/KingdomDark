class ass:
    def __init__(self, image_list, path = 'Ass/', name = None):
        self.images = {}
        self.retrieve(image_list, path)
        self.starttime = None
        self.name = name
        self.poses = []
    def retrieve(self, image_list, path):
        import pygame as paygay
        for this in image_list:
            self.images[this[:-4]] = paygay.image.load(path + this)
    def blit(self, screen, image, xy_tuple):
        screen.blit(self.images[image], xy_tuple)
    def pose(self, screen, oxygen, pose, xy_tuple, tick, weight = 1, crop = None):
        paralax_x, paralax_y = oxygen.paralax_x, oxygen.paralax_y
        image = self.images[self.name + '_' + pose + str(tick)]
        pos = (xy_tuple[0] + paralax_x/weight, xy_tuple[1] + paralax_y/weight)
        if crop == None:
            screen.blit(image, pos)
        else:
            screen.blit(image, pos, crop)

class hatlor_obj(ass):
    def __init__(self, image_list):
        super().__init__(image_list)
        self.name = "hatlor"

class curtain_obj(ass):
    def __init__(self, image_list):
        super().__init__(image_list)
        self.name = "curtain"
    def waiting(self, screen, oxygen, input, pose, xy_tuple, tick, weight = 1.5):
        self.pose(screen, oxygen, pose, xy_tuple, tick, weight)
        rect = self.images['curtain_wait3'].get_rect(topleft = xy_tuple)
        return(rect)

class person_obj(ass):
    def __init__(self, image_list):
        super().__init__(image_list)
        self.name = image_list[0][:-11]
        self.orientation = 'left'
        self.x_move = 4000
    def sliding_in(self, screen, oxygen, pose, xy_tuple, tick, speed = 1.06, speedst = 10):
        self.x_move /= speed
        self.pose(screen, oxygen, pose, (xy_tuple[0] + self.x_move - speedst, xy_tuple[1]), tick)
        if self.x_move < speedst:
            self.x_move = speedst
            return True
        else:
            return False
    def sliding_out(self, screen, oxygen, pose, xy_tuple, tick, speed = 1.06, speedst = 4000):
        self.x_move *= speed
        self.pose(screen, oxygen, pose, (xy_tuple[0] + self.x_move, xy_tuple[1]), tick)
        if self.x_move >= speedst:
            self.x_move = 4000
            return True
        else:
            return False

class gen_obj(ass):
    def __init__(self, image_list):
        super().__init__(image_list)
        self.name = image_list[0][:-8] # this cuts off the "_be1.png" part of gen_objs
