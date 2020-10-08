class synth_obj():
    def __init__(self, jsondata):
        pass
        self.arg = 0
        self.list_of_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']; self.octave = 4; self.count = 0
    def play(self, jsondata, input, mode = None, keyboard_set = None):
        import mingus
        from mingus.midi import fluidsynth
        if not keyboard_set == None:
            if not keyboard_set in jsondata.keyboard_sets:
                jsondata.keyboard_sets.update({keyboard_set: {}})
            key_press = None
            for this in input.keydict:
                if input.keydict[this] and not this in jsondata.keyboard_sets[keyboard_set]:
                    key_press = this
            if not key_press == None:
                note_var = self.list_of_notes[self.count] + '-' + str(self.octave)
                jsondata.keyboard_sets[keyboard_set].update({key_press: note_var}); fluidsynth.play_Note(mingus.containers.Note(note_var))
                jsondata.save('keyboard_sets')
                self.count += 1
                if self.count == 12:
                    self.count = 0
                    self.octave += 1
        elif not mode == None:
            for this in jsondata.keyboard_sets[mode]:
                exec('self.arg = input.' + this + '_t')
                if self.arg:
                    fluidsynth.play_Note(mingus.containers.Note(jsondata.keyboard_sets[mode][this]))
