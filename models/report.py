import os


class Report:
    def __init__(self, levels: [] = []):
        self._id = os.urandom(7).hex()
        self._levels = levels

    @property
    def levels(self):
        return self._levels

    @property
    def id(self):
        return self._id

    @levels.setter
    def levels(self, new_levels):
        self._levels = new_levels

    def add(self, level):
        self._levels.append(level)

    def remove(self, level):
        self._levels.remove(level)

    def __repr__(self):
        return f"Report(id: {self._id}, levels: {self._levels})"
