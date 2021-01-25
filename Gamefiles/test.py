import threading
def super_print(go):
    while go:
        print('good')
def super_print2(go):
    while go:
        print('and')

go = False

threadname = threading.Thread(super_print(go), (go))
threadname2 = threading.Thread(target = super_print2(go), args = (go))

go = True

threadname2.start()
threadname.start()
