"""
valve.valve

"""


class Toggle(object):
    def __init__(self, on=False):
        """
        :param on: whether or not the toggle is on. Default is False.
        :type on: bool
        """
        self._on = bool(on)

    def __bool__(self):
        return self.on

    def toggle(self):
        """
        Toggles the state of the switch and returns the new state of the switch.
        I.E. if the switch is off, this will turn it on, vice versa

        :returns: the new state of the switch
        :rtype: bool
        >>> t = Toggle(on=False)
        >>> t.on
        False
        >>> t.toggle()
        True
        >>> t.on
        True
        >>> t.off
        False

        """
        self.on = not self.on
        return self.on

    @property
    def on(self):
        """
        Checks the current state of the toggle.
        When set, it will change the on/off by coarsing a boolean from the provided argument.
        Returns True if the current state (`self._on`) is on else False
        :return: True if the current state (`self._on`) is on else False
        :rtype: bool

        >>> t = Toggle(on=True)
        >>> t.on
        True
        """
        return self._on

    @on.setter
    def on(self, new_on_value):
        self._on = bool(new_on_value)

    @property
    def off(self):
        return not self.on


class Valve(Toggle):
    """
    Provides 'Valve control' functionality to Toggle.
    Allows for valves to be considered 'normally open' or 'normally closed'
    IE when a valve is 'off' (passive) and 'normally open', it is open.
    when a valve is 'on' (active) and 'normally open', it is closed.
    """
    def __init__(self, normally_open=False, *args, **kwargs):
        """
        Defaultly off and normally closed.
        :param normally_open: default is False, IE normally closed
        :type normally_open: bool
        :param args:
        :param kwargs:
        """
        self._normally_open = bool(normally_open)
        super().__init__(*args, **kwargs)

    def __bool__(self):
        return self.is_open

    def close(self):
        """
        Closes the valve
        If the valve is not already closed, `self.toggle` is called.

        :returns: None

        >>> v = Valve(on=True) # on, normally closed
        >>> v.closed
        False
        >>> v.close()
        >>> v.closed
        True
        >>> v.close()
        >>> v.closed #shouldn't change since it's already closed
        True

        """
        if not self.closed:
            self.toggle()

    def open(self):
        """
        Opens the valve
        If the valve is not already open, `self.toggle` is called

        :returns: None

        >>> v = Valve(on=False) #off, normally closed
        >>> v.closed
        True
        >>> v.open()
        >>> v.is_open
        True
        >>> v.closed
        False
        >>> v.open()
        >>> v.closed #shouldn't change since it's already open
        False
        """

        if self.closed:
            self.toggle()

    @property
    def is_open(self):
        # should this be a thing? Maybe just `is_closed` (and/or `closed`) is sufficient
        # if it should be a thing should there also or alternatively be `opened` ?
        return not self.closed

    @property
    def closed(self):
        if self.normally_open:
            return self.on
        return not self.on

    @property
    def is_closed(self):
        return self.closed

    @property
    def normally_open(self):
        return self._normally_open

    @normally_open.setter
    def normally_open(self, new_open_value):
        self._normally_open = bool(new_open_value)

    @property
    def normally_closed(self):
        return not self.normally_open

    @normally_closed.setter
    def normally_closed(self, new_closed_value):
        self._normally_open = not bool(new_closed_value)
