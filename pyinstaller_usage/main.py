# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
from os.path import dirname, abspath

from easyium import Chrome, StaticElement
import pandas as pd


def create_dataset():
    names = ['Bob2', 'Jessica', 'Mary', 'John', 'Mel']
    births = [968, 155, 77, 578, 973]
    name_map_births = zip(names, births)
    baby_dataset = list(name_map_births)
    return baby_dataset


def get_sub_folder_path(sub_dir_name='data'):
    """
    Create the destination folder if not exists.
    :param sub_dir_name: default is 'data'
    :return: sub folder's absolute path.
    """
    # warnings.warn("Please call another", PendingDeprecationWarning)
    current_dir_name = dirname(__file__)
    abs_path = abspath(current_dir_name)
    sub_folder = os.sep.join([abs_path, sub_dir_name])

    if not os.path.exists(sub_folder):
        os.makedirs(sub_folder)

    return sub_folder


class Column:
    NAMES = "Names"
    BIRTHS = "Births"


class PackClass:
    def __init__(self, name):
        """

        :param name:
        """
        self.name = name
        if __debug__:
            print("When using -O, __debug__ is set to False ")

    def print_hi(self):
        """

        :return:
        """
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {self.name}')  # Press Ctrl+F8 to toggle the breakpoint.
        web_driver = Chrome()
        web_driver.maximize_window()
        web_driver.get("https://www.baidu.com/")
        StaticElement(web_driver, 'id=kw').send_keys(self.name)
        StaticElement(web_driver, 'id=su').click()

        write_df = pd.DataFrame(data=create_dataset(), columns=[Column.NAMES, Column.BIRTHS])
        abs_path = get_sub_folder_path()
        file_path = os.sep.join([abs_path, 'births1888.xlsx'])
        write_df.to_excel(file_path, index=False, header=True)


if __name__ == '__main__':
    assert len(sys.argv) >= 2, "Invalid arguments: should have at least pack name after the python file name!"
    pack_name = sys.argv[1]
    obj = PackClass(pack_name)
    obj.print_hi()

