def clear():
    import os
    if os.name == 'nt': _ = os.system('cls')
    else: _ = os.system('clear')

def check_dict(jsondata, character):
    dict = jsondata.dialogues[character]
    checkdict = {"Immutable_Dialogue_List": [], "Dialogue_List": [], "Position": [1500, 650], "Dialogues": {}}
    if not dict.keys() == checkdict.keys():
        print("The dialogues dictionary for " + character + " is incomplete:")
        print("    Current keys - " + str(dict.keys())[11:len(str(dict.keys()))  - 1])
        print("    Correct keys - " + str(checkdict.keys())[11:len(str(checkdict.keys())) - 1])
        answer = input('Would you like the current keys overwritten with the correct keys? (y/n) \n')
        if answer == 'y':
            empty = []
            for this in dict.keys():
                if not this in checkdict.keys():
                    empty.append(this)
            for this in empty:
                del dict[this]
            for this in checkdict.keys():
                if not this in dict.keys():
                    dict.update({this: checkdict[this]})
            jsondata.dialogues[character] = dict; jsondata.save('dialogues')
            input('\nDictionary overwritten successfully. (Enter)')
            clear()
        elif answer == 'n':
            raise Exception('\nTo fix the dictionary without overwriting, go to Storage/dialogues.json and find the key/value pair.')
        else:
            write_mode(jsondata)

def position_access(jsondata, character):
    clear()
    value = jsondata.dialogues[character]['Position']
    print('The x-position is ' + str(value[0]))
    print('The y-position is ' + str(value[1]))
    answer = input('To change one of these values, specify which. (x/y)\n')
    if answer == 'x': number = 0
    elif answer == 'y': number = 1
    else:
        access_character_attributes(jsondata, character)
    jsondata.dialogues[character]['Position'][number] = int(input('Enter the new value.\n'))
    jsondata.save('dialogues')
    clear()
    input('Value saved successfully. Returning to access menu. (Enter)')
    access_character_attributes(jsondata, character)

def write_dialogue(jsondata, character, dialogue, scroll):
    clear()
    dialogue_dict = jsondata.dialogues[character]['Dialogues'][dialogue]
    print(dialogue_dict[str(scroll)]['Char'] + ': ' + dialogue_dict[str(scroll)]['Message'])
    print('Dialogue piece (' + str(scroll + 1) + '/' + str(len(dialogue_dict)) + ')')
    answer = input()
    try:
        answer = int(answer)
        clear()
        if answer > 0 and answer <= len(dialogue_dict): scroll = answer - 1
        write_dialogue(jsondata, character, dialogue, scroll)
    except:
        if answer == 'next':
            clear()
            if scroll < len(dialogue_dict) - 1: scroll += 1
            write_dialogue(jsondata, character, dialogue, scroll)
        elif answer == 'prev':
            clear()
            if scroll > 0: scroll -= 1
            write_dialogue(jsondata, character, dialogue, scroll)
        elif answer == 'edit':
            clear()
            print('Type "hatlor/' + character + ': dialogue", as seen below.')
            print(dialogue_dict[str(scroll)]['Char'] + ': ' + dialogue_dict[str(scroll)]['Message'])
            print('Dialogue piece (' + str(scroll + 1) + '/' + str(len(dialogue_dict)) + ')\n')
            speaker, new_dialogue = input('').split(': ')
            jsondata.dialogues[character]['Dialogues'][dialogue][str(scroll)]['Char'] = speaker
            jsondata.dialogues[character]['Dialogues'][dialogue][str(scroll)]['Message'] = new_dialogue
            jsondata.save('dialogues')
            clear()
            input('Dialogue saved successfully. Returning to edit menu. (Enter)')
            write_dialogue(jsondata, character, dialogue, scroll)
        elif answer == 'add_next':
            piece = str(dialogue_dict[str(scroll)]['Char']) + ': ' + str(dialogue_dict[str(scroll)]['Message'])
            scroll += 1; splint_dict = {}
            if scroll in dialogue_dict:
                for this in dialogue_dict:
                    if int(this) >= scroll:
                        splint_dict[str(int(this) + 1)] = dialogue_dict[this]
                        if int(this) == scroll:
                            dialogue_dict[this] = {'Char': 'hatlor', 'Message': 'This dialogue (' + dialogue + ') is incomplete.'}
                for this in splint_dict:
                    dialogue_dict[this] = splint_dict[this]
            else:
                dialogue_dict[str(scroll)] = {'Char': 'hatlor', 'Message': 'This dialogue (' + dialogue + ') is incomplete.'}
            clear()
            print('Type "hatlor/' + character + ': dialogue", as seen below.')
            print(piece)
            print('Dialogue piece (' + str(scroll + 1) + '/' + str(len(dialogue_dict)) + ')\n')
            speaker, new_dialogue = input('').split(': ')
            jsondata.dialogues[character]['Dialogues'][dialogue] = dialogue_dict
            jsondata.dialogues[character]['Dialogues'][dialogue][str(scroll)]['Char'] = speaker
            jsondata.dialogues[character]['Dialogues'][dialogue][str(scroll)]['Message'] = new_dialogue
            jsondata.save('dialogues')
            clear()
            input('Dialogue saved successfully. Returning to edit menu. (Enter)')
            write_dialogue(jsondata, character, dialogue, scroll)
        elif answer == 'add_prev':
            piece = str(dialogue_dict[str(scroll)]['Char']) + ': ' + str(dialogue_dict[str(scroll)]['Message'])
            splint_dict = {}
            for this in dialogue_dict:
                if int(this) >= scroll:
                    splint_dict[str(int(this) + 1)] = dialogue_dict[this]
                    if int(this) == scroll:
                        dialogue_dict[this] = {'Char': 'hatlor', 'Message': 'This dialogue (' + dialogue + ') is incomplete.'}
            for this in splint_dict:
                dialogue_dict[this] = splint_dict[this]
            clear()
            print('Type "hatlor/' + character + ': dialogue", as seen below.')
            print(piece)
            print('Dialogue piece (' + str(scroll + 1) + '/' + str(len(dialogue_dict)) + ')\n')
            speaker, new_dialogue = input('').split(': ')
            jsondata.dialogues[character]['Dialogues'][dialogue] = dialogue_dict
            jsondata.dialogues[character]['Dialogues'][dialogue][str(scroll)]['Char'] = speaker
            jsondata.dialogues[character]['Dialogues'][dialogue][str(scroll)]['Message'] = new_dialogue
            jsondata.save('dialogues')
            clear()
            input('Dialogue saved successfully. Returning to edit menu. (Enter)')
            write_dialogue(jsondata, character, dialogue, scroll)
        elif answer == 'del':
            clear()
            if not scroll == 0:
                answer = input('Are you certain you want to delete this piece of dialogue? (y/n)\n')
                clear()
                if answer == 'y':
                    del dialogue_dict[str(scroll)]
                    shift_dict = {}
                    for this in dialogue_dict:
                        if int(this) > scroll:
                            shift_dict.update({this: dialogue_dict[this]})
                    for this in shift_dict:
                        dialogue_dict.update({str(int(this) - 1): shift_dict[this]})
                        del dialogue_dict[this]
                    jsondata.dialogues[character]['Dialogues'][dialogue] = dialogue_dict
                    jsondata.save('dialogues')
                    print('Dialogue piece deleted successfully.')
                else:
                    pass
                print('Returning to dialogue edit menu.')
                input('(Enter)\n')
                write_dialogue(jsondata, character, dialogue, scroll - 1)
            else:
                print('You cannot delete the first piece of dialogue.')
                print('To replace this piece of dialogue, use edit.')
                print('Returning to dialogue edit menu.')
                input('(Enter)\n')
                write_dialogue(jsondata, character, dialogue, scroll)
        else:
            write_dialogue_instruction(jsondata, character, dialogue, scroll)

def write_dialogue_instruction(jsondata, character, dialogue, scroll = 0):
    clear()
    print('Instruction: ')
    print('Type next to advance to the next piece of dialogue.')
    print('Type prev to go backwards.')
    print('You can also type a number to reach that number in the dialogue.')
    print('Type edit to edit the current piece of dialogue.')
    print('To create a new piece of dialogue ahead of the current, type add_next.')
    print('To create one before, type add_prev.')
    answer = input('(Enter)\n')
    if answer != 'back':
        write_dialogue(jsondata, character, dialogue, scroll)
    else:
        edit(jsondata, character)

def edit(jsondata, character):
    clear()
    save_list = jsondata.dialogues[character]['Dialogue_List']
    immu_list = jsondata.dialogues[character]['Immutable_Dialogue_List']
    if len(immu_list) > 0:
        print('The dialogues for ' + character + ' are:')
        for this in immu_list:
            print('\n    ' + this)
        answer = input('\nType the dialogue you want to edit.\n')
        if answer in immu_list:
            write_dialogue_instruction(jsondata, character, answer)
        else:
            dialogue_access(jsondata, character)
    else:
        input(character + 'has no dialogues; press (Enter) to go and create one.\n')
        create(jsondata, character)

def create(jsondata, character):
    clear()
    save_list = jsondata.dialogues[character]['Dialogue_List']
    immu_list = jsondata.dialogues[character]['Immutable_Dialogue_List']
    if len(immu_list) > 0:
        print('The dialogues for ' + character + ' are:')
        for this in immu_list:
            print('\n    ' + this)
    else:
        print('There are currently no dialogues for ' + character + '.')
    answer = input('\nType the name of the dialogue you want to create.\n')
    if not answer in immu_list:
        jsondata.dialogues[character]['Dialogue_List'].append(answer)
        jsondata.dialogues[character]['Immutable_Dialogue_List'].append(answer)
        jsondata.dialogues[character]['Dialogues'].update({answer: {"0": {"Char": "hatlor", "Message": "This message in " + answer + " is to be overwritten."}}})
        jsondata.save('dialogues')
        clear()
        print('New dialogue entered in the dictionary for ' + character + '.')
        input('Press (Enter) to go on and edit it.\n')
        write_dialogue_instruction(jsondata, character, answer)
    else:
        print('This dialogue already exists.')
        input('Press (Enter) to go back to the dialogue creation screen.\n')
        create(jsondata, character)

def delete(jsondata, character):
    clear()
    save_list = jsondata.dialogues[character]['Dialogue_List']
    immu_list = jsondata.dialogues[character]['Immutable_Dialogue_List']
    if len(immu_list) > 1:
        print('The dialogues for ' + character + ' are:')
        for this in immu_list:
            print('\n    ' + this)
        print('\nWhich one would you like to delete?')
        answer = input('')
        if answer in immu_list:
            clear()
            dialogue = answer
            answer = input('Are you ABSOLUTELY sure you want to delete this? (y/n)')
            if answer == 'y':
                jsondata.dialogues[character]['Dialogue_List'].remove(dialogue)
                jsondata.dialogues[character]['Immutable_Dialogue_List'].remove(dialogue)
                del jsondata.dialogues[character]['Dialogues'][dialogue]
            else:
                dialogue_access(jsondata, character)
        else:
            dialogue_access(jsondata, character)
    else:
        print('There are currently no dialogues for ' + character)
        input('Press (Enter) to go back to the dialogue access screen.\n')
        dialogue_access(jsondata, character)

def dialogue_access(jsondata, character):
    clear()
    answer = input('Type an action. (edit/create/delete)\n')
    if answer in ['edit', 'create', 'delete']:
        exec(answer + '(jsondata, character)')
    else:
        access_character_attributes(jsondata, character)

def access_character_attributes(jsondata, character):
    clear()
    dict = jsondata.dialogues[character]
    check_dict(jsondata, character)
    print('Type one of the following access keys:')
    for this in ['position', 'dialogue']:
        print('\n    ' + this.lower())
    answer = input('\n')
    if answer in ['position', 'dialogue']:
        exec(answer + '_access(jsondata, character)')
    else:
        write_mode(jsondata)

def write_mode(jsondata):
    clear()
    print('-- WRITE MODE -- \n')
    print('Type "back" to go back a screen.\n')
    print('The current characters with dialogue are:')
    for this in jsondata.dialogues:
        print('\n    ' + this)
    character = input('\nEnter the character you want to access: \n')
    if character in jsondata.dialogues:
        access_character_attributes(jsondata, character)
    if not character in jsondata.dialogues:
        clear()
        print('Character not in dialogues dictionary.')
        answer = input('Do you want to add ' + character + ' to the dialogue dictionary? (y/n) \n')
        if answer == 'y':
            jsondata.dialogues.update({character: {"Position": [1500, 650], "Immutable_Dialogue_List": [], "Dialogue_List": [], "Dialogues": {}}})
            clear()
            input('Default position assigned.\nPress (Enter) to proceed to creating the first dialogue for this character.\n')
            create(jsondata, character)
        else:
            write_mode(jsondata)
