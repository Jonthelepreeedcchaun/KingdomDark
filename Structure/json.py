class json_obj:
    def __init__(self):
        self.retrieve()
    def retrieve(self, path = 'Storage/'):
        import os, json
        for this in os.listdir(path):
            if this[-5:] == ".json":
                with open('Storage/' + this, 'r') as f:
                    exec('self.' + this[:-5] + ' = json.load(f)')
    def save(self, attr):
        import json
        if hasattr(self, attr):
            with open('Storage/' + attr + '.json', 'w', encoding = 'utf-8') as f:
                exec('json.dump(self.' + attr + ', f, ensure_ascii = False, indent = 4)')
        else:
            print('Jsondata Error: ' + attr + '.json inaccessable')
