class Television:
    """
    Class to create a Television object.
    Television objects have the following attributes:
    minimum channel, maximum channel, minimum volume, maximum volume,
    and television status (on/off = True/False, set in __init__ function).
    """
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        """
        Function to set up a television object.
        Television is set to minimum channel, minimum volume, and off.
        """
        self.__TV_channel = Television.MIN_CHANNEL
        self.__TV_volume = Television.MIN_VOLUME
        self.__TV_status = False

    def power(self) -> None:
        """
        Function which turns the television on or off (on = True, off = False).
        """
        if not self.__TV_status:
            self.__TV_status = True
        else:
            self.__TV_status = False

    def channel_up(self) -> None:
        """
        Function to increment the channel by 1. If the channel is at max channel,
        the channel is changed to the minimum channel.
        """
        if self.__TV_status:
            if self.__TV_channel < Television.MAX_CHANNEL:
                self.__TV_channel += 1
            else:
                self.__TV_channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Function to decrement the channel by 1. If the channel is at min channel,
        the channel is changed to the maximum channel.
        """
        if self.__TV_status:
            if self.__TV_channel > Television.MIN_CHANNEL:
                self.__TV_channel -= 1
            else:
                self.__TV_channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Function to increment the volume by 1. If the channel is at max volume,
        the volume remains unchanged.
        """
        if self.__TV_status:
            if self.__TV_volume < Television.MAX_VOLUME:
                self.__TV_volume += 1

    def volume_down(self) -> None:
        """
        Function to decrement the volume by 1. If the channel is at min volume,
        the volume remains unchanged.
        """
        if self.__TV_status:
            if self.__TV_volume > Television.MIN_VOLUME:
                self.__TV_volume -= 1

    def __str__(self) -> str:
        """
        Function to return television status.
        :return: TV status in on (True or False), Channel, Volume.
        """
        return f'TV status: Is on = {self.__TV_status}, Channel = {self.__TV_channel}, Volume = {self.__TV_volume}'
