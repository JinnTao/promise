# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tqsdk as tq;

from Common import Tao

def init(isGui = False):
    api = tq.TqApi(web_gui= isGui,auth=tq.TqAuth(Tao.ACC,Tao.PWD))
    return api
def show_account(account):
    return



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    api = init(True)
    klines = api.get_kline_serial(Tao.MAIN_SHFE_RB,10)
    while True:
        api.wait_update()
        print(klines) # 200条K线
        api.get_account()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
