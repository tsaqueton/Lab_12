import pytest
from classes import *


class Test:
    """
    class for testing functions in classes.py
    """

    def setup_method(self):
        """
        method sets up tests by creating television objects t1 and t2.
        """
        self.t1 = Television()
        self.t2 = Television()

    def teardown_method(self):
        """
        method that tears down by deleting television objects t1 and t2.
        """
        del self.t1
        del self.t2

    def test_init(self):
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        assert self.t2.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

    def test_power(self):
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.t1.power()
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

    def test_channel_up(self):
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.t1.channel_up()
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.t1.power()

        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        assert self.t1.channel_up() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'
        assert self.t1.channel_up() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'
        assert self.t1.channel_up() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'
        assert self.t1.channel_up() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        assert self.t1.channel_up() is None
        assert self.t1.channel_up() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'

    def test_channel_down(self):
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        assert self.t1.channel_down() is None
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        assert self.t1.power() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        assert self.t1.channel_down() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'
        assert self.t1.channel_down() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'
        assert self.t1.channel_down() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'
        assert self.t1.channel_down() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        assert self.t1.channel_down() is None
        assert self.t1.channel_down() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'

    def test_volume_up(self):
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        assert self.t1.volume_up() is None
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        assert self.t1.power() is None
        assert self.t1.volume_up() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'
        assert self.t1.power() is None
        assert self.t1.volume_up() is None
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 1'
        assert self.t1.power() is None
        assert self.t1.volume_up() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'
        assert self.t1.volume_up() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'
        assert self.t1.volume_up() is None
        assert self.t1.volume_up() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        assert self.t1.power() is None
        assert self.t1.volume_up() is None
        assert self.t1.volume_up() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'
        assert self.t1.power() is None
        assert self.t1.volume_down() is None
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 2'
        assert self.t1.power() is None
        assert self.t1.volume_down() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'
        assert self.t1.power() is None
        assert self.t1.volume_down() is None
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 1'
        assert self.t1.power() is None
        assert self.t1.volume_down() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        assert self.t1.volume_down() is None
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'


# pip install pytest
# pytest test_file.py
# pytest test_file.py -v
# pytest test_file.py::test_function
