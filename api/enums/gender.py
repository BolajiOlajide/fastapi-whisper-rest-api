from enum import Enum

from api.constants import MALE, FEMALE


class Gender(str, Enum):
    """
    Gender enum to show the different genders of
    a human.
    """

    MALE = MALE
    FEMALE = FEMALE
