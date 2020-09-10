
from src.web.becode import TimePeriodsEnum
from dataclasses import dataclass


@dataclass
class AttendanceJson:
    """Create and return the JSON structure to post."""

    period: TimePeriodsEnum
    at_home: bool

    def get_json(self):

        return {
            "operationName": "record_attendance_time",
            "variables": {
                "period": self.period.name,
                "atHome": self.at_home
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "553ae433516c13a97e348d4a48dd0114d1949f791ab21d97bed27030a65e85a8"
                }
            }
        }
