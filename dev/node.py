class Node:

    def __init__(self):
        self._pv = None
        self._shield = None
        self._father = None
        self._child = []
        self._user = None

    @property
    def pv(self):
        return self._pv
    
    @pv.setter
    def pv(self, value):
        self._pv = value

    @property
    def shield(self):
        return self._shield

    @shield.setter
    def shield(self, value):
        self._shield = value

    @property
    def father(self):
        return self._father

    @father.setter
    def father(self, value):
        self._father = value

    @property
    def child(self):
        return self._child

    @child.setter
    def child(self, value):
        self._child = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value