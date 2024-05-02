from pydantic import BaseModel, validator, field_validator

from course_SolveMe_youtube.infra.global_enums import Statuses
from course_SolveMe_youtube.infra.user_enum import Genders,UserError


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses

    @field_validator("email")
    def check_that_dog_presented_in_email_address(cls,email):
        if "@" in email:
            return email
        else:
            raise ValueError(UserError.WRONG_EMAIL.value)
