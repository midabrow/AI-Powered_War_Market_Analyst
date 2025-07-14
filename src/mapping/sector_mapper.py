# src/mapping/sector_mapper.py

# from typing import Optional

# class SectorMapper:
#     def __init__(self):
#         self.keyword_to_sector = {
#             "missile": "defense",
#             "drone": "defense",
#             "sanction": "finance",
#             "oil": "energy",
#             "gas": "energy",
#             "inflation": "finance",
#             "stock": "finance",
#             "AI": "technology",
#             "cyber": "technology",
#             "wheat": "agriculture",
#             "grain": "agriculture",
#             "military": "defense",
#             "tank": "defense",
#             "explosion": "defense",
#             "nuclear": "energy",
#             "internet": "technology",
#             "export": "trade",
#             "import": "trade",
#             "currency": "finance",
#         }



#     def map_to_sector(self, text: str) -> Optional[str]:
#         text = text.lower()
#         for keyword, sector in self.keyword_to_sector.items():
#             if keyword in text:
#                 return sector
#         return "other"



from typing import List

class SectorMapper:
    """
    Maps a given event (title + content) to a market sector.
    """
    def __init__(self):
        self.mapping = {
            "oil": ["oil", "gas", "OPEC", "barrel", "crude"],
            "defense": ["missile", "strike", "drone", "military", "army", "weapon"],
            "tech": ["chip", "semiconductor", "AI", "cyber", "data", "cloud"],
            "finance": ["bank", "interest rate", "inflation", "Fed", "ECB"],
            "shipping": ["port", "canal", "logistics", "cargo", "shipping"],
            "energy": ["power", "nuclear", "reactor", "energy grid", "renewable"]
        }

    def map_to_sector(self, text: str) -> List[str]:
        """
        Returns a list of relevant sectors based on keyword matching.
        """
        text_lower = text.lower()
        matched_sectors = [sector for sector, keywords in self.mapping.items()
                           if any(keyword in text_lower for keyword in keywords)]
        return matched_sectors or ["other"]
