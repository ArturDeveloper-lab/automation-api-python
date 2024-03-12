from pydantic import BaseModel, validator, field_validator, Field


class Post(BaseModel):
    # id: int = Field(ls=2) # that say id field check if this less than 2
    id: int
    title: str

    # @field_validator("id")
    # def check_that_id_is_less_than_two(cls, v):
    #     if v > 2:
    #         raise ValueError("id is not less than two")
    #     else:
    #         return v
