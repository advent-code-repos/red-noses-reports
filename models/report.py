import os
from models.policy import Policy


class Report:
    def __init__(self, levels: [] = [], report_policy: Policy = Policy.NONE):
        self._id = os.urandom(7).hex()
        self._levels = levels
        self._report_policy = report_policy

    @property
    def levels(self):
        return self._levels

    @property
    def id(self):
        return self._id

    @property
    def report_policy(self):
        return self._report_policy

    @levels.setter
    def levels(self, new_levels):
        self._levels = new_levels

    @levels.setter
    def policy(self, new_policy):
        self._policy = new_policy

    def add(self, level):
        self._levels.append(level)

    def remove(self, level):
        self._levels.remove(level)

    def __repr__(self):
        return (
            f"Report(id: {self._id}, "
            f"levels: {self._levels}, report_policy: {self._report_policy})"
        )
