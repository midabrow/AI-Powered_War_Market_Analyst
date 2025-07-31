# src/mapping/sector_mapper.py

from typing import Callable


class SectorRule:
    def __init__(self, name: str, condition: Callable[[str, str], bool]):
        self.name = name
        self.condition = condition


class SectorMapper:
    def __init__(self):
        self.rules = [
            SectorRule("energy", lambda title, tag: any(x in title for x in ["oil", "gas", "iran", "saudi"]) or tag == "sanction"),
            SectorRule("defense", lambda title, tag: any(x in title for x in ["ukraine", "russia", "army"]) or tag == "attack"),
            SectorRule("tech", lambda title, tag: any(x in title for x in ["chip", "semiconductor", "china"]) or tag == "supply"),
            SectorRule("finance", lambda title, tag: any(x in title for x in ["inflation", "market"]) or tag == "incident"),
        ]

    def map(self, title: str, tag: str) -> str:
        title = title.lower()
        tag = tag.lower()

        for rule in self.rules:
            if rule.condition(title, tag):
                return rule.name

        return "global"
