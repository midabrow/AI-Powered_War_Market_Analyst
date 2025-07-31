from fastapi import APIRouter
from pydantic import BaseModel, Field
from src.mapping.sector_mapper import SectorMapper

router = APIRouter()

class MappingRequest(BaseModel):
    title: str = Field(..., description="Title of the news article")
    tag: str = Field(..., description="Tag to map to a sector", example="defense")

@router.post("/map_sector")
def map_sector_route(req: MappingRequest) -> dict:
    mapper = SectorMapper()
    map_to_sector = mapper.map(req.title, req.tag)
    return {"sector": map_to_sector}
