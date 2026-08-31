"""Merged chapters and navigation."""
from .mod_base import CHAPTERS as _BASE
from .mod_hardware import CHAPTERS as _HW
from .mod_protocol import CHAPTERS as _PROTO
from .mod_practice import CHAPTERS as _PRACTICE
from .mod_stm32 import CHAPTERS as _STM32
from .mod_esp32 import CHAPTERS as _ESP32
from .mod_advanced import CHAPTERS as _ADV
from .mod_ios import CHAPTERS as _IOS
from .mod_projects import CHAPTERS as _PROJ
from .mod_scenarios import CHAPTERS as _SCENE
from .mod_exercises import CHAPTERS as _EX
from .mod_interview import CHAPTERS as _INT
from .nav import NAV

CHAPTERS = {}
for _m in (_BASE, _HW, _PROTO, _PRACTICE, _STM32, _ESP32, _ADV, _IOS, _PROJ, _SCENE, _EX, _INT):
    CHAPTERS.update(_m)

TOTAL = len(CHAPTERS)

__all__ = ["NAV", "CHAPTERS", "TOTAL"]
