from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Package Sorting API",
    description="Sorts packages",
    version="1.0.0",
)

def sort(width: float, height: float, length: float, mass: float) -> str:
    """Sorting logic"""
    bulky = (width * height * length >= 1_000_000) or any(dim >= 150 for dim in (width, height, length))
    heavy = mass >= 20
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

class Package(BaseModel):
    length: float = Field(..., gt=0, description="Length in cm")
    width: float = Field(..., gt=0, description="Width in cm")
    height: float = Field(..., gt=0, description="Height in cm")
    mass: float = Field(..., gt=0, description="Mass in kg")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/sort")
def sort_package(package: Package):
    return {"stack": sort(package.length, package.width, package.height, package.mass)}