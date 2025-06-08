from datetime import date
from pydantic import BaseModel, ConfigDict


class AnimalCreate(BaseModel):
    animal_type: str
    name: str
    birth_date: date
    breed : str
    photo_url : str

class AnimalResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    animal_type: str
    name: str
    birth_date: date
    breed : str
    photo_url : str

    @property
    def age(self) -> int:
        today = date.today()
        age = today.year - self.birth_date.year

        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age = age - 1
        return age

    def model_dump(self, *args, **kwargs):
        data = super().model_dump(*args, **kwargs)
        data['age'] = self.age
        return data