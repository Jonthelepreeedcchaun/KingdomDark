class event_obj:
    def __init__(self):
        self.stage = 'brief pause'; self.count = 0; self.init_char_dict = False
    def go(self, screen, oxygen, input, current_taco, tick, jsondata, text, char_dict):
        if self.init_char_dict == False:
            self.scripted_char_list = []; self.rng_char_list = []
            for this in char_dict:
                if char_dict[this] == len(self.scripted_char_list) + 1:
                    self.scripted_char_list.append(this)
                elif char_dict[this] == 'r':
                    self.rng_char_list.append(this)
                else:
                    try:
                        print('Error! Character ' + this.name + ' in char_dict ' + str(char_dict) + ' is incorrectly entered.')
                    except:
                        print('Error! Char_dict ' + str(char_dict) + ' contains non-character objects.')
            self.init_char_dict = True
        if len(self.scripted_char_list) > 0:
            char = self.scripted_char_list[0]
        elif len(self.rng_char_list) > 0:
            char = self.scripted_char_list[0]
        else:
            self.init_char_dict = False
            return True
        info_dict = jsondata.dialogues[char.name]
        if self.stage == 'brief pause':
            self.count += 1
            if self.count == 10:
                self.stage = 'sliding_in'
        if self.stage == 'sliding_in':
            if char.sliding_in(screen, oxygen, 'stand', info_dict['Position'], tick):
                self.stage = 'Talking'
        elif self.stage == 'Talking':
            if not text.browse > text.dialength - 1:
                char.pose(screen, oxygen, 'stand', info_dict['Position'], tick)
                text.box(screen, oxygen, input, info_dict['Dialogues'][info_dict['Dialogue_List'][0]], 2*900/3, 2*750/3, 2*172/3, current_taco, tick)
            else:
                text.reset()
                self.stage = 'sliding_out'
        elif self.stage == 'sliding_out':
            if char.sliding_out(screen, oxygen, 'flipp', info_dict['Position'], tick):
                self.stage = 'brief pause'
                self.count = 0
                if char in self.scripted_char_list:
                    self.scripted_char_list.remove(char)
                elif char in self.rng_char_list:
                    self.rng_char_list.remove(char)
