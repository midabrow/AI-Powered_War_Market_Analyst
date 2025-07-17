def map_to_sector(title: str, tag: str) -> str:
    """
    Maps a classified event to an economic sector.
    """

    title = title.lower()
    tag = tag.lower()

    if "oil" in title or "gas" in title or "iran" in title or "saudi" in title or tag == "sanction":
        return "energy"
    if "ukraine" in title or "russia" in title or "army" in title or tag == "attack":
        return "defense"
    if "chip" in title or "semiconductor" in title or "china" in title or tag == "supply":
        return "tech"
    if "inflation" in title or "market" in title or tag == "incident":
        return "finance"

    return "global"
