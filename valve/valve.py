class Toggle(object):
    def __init__(self, on=False):
        self._on = bool(on)

    def __bool__(self):
        return self.on

    def toggle(self):
        self.on = not self.on

    @property
    def on(self):
        return self._on

    @on.setter
    def on(self, new_on_value):
        self._on = bool(new_on_value)

    @property
    def off(self):
        return not self.on


class Valve(Toggle):
    def __init__(self, normally_open=False, *args, **kwargs):
        self._normally_open = bool(normally_open)
        super().__init__(*args, **kwargs)

    def close(self):
        if self.is_open:
            self.toggle()
        # should an error be raised if already closed?
        # maybe a `slient` flag?

    def open(self):
        if self.closed:
            self.toggle()
        # should an error be raised if already open?
        # maybe a `silent` flag?

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


v = Valve() #off, normally closed

print(v.closed == True)