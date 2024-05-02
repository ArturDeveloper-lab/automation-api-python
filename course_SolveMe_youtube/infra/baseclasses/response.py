from _pytest.fixtures import fixture
from jsonschema.validators import validate

from course_SolveMe_youtube.infra.global_enums import GlobalErrorMessages
from course_SolveMe_youtube.infra.json_schemas.posts import POST_SCHEMA


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

        if isinstance(self.response_json, dict) and 'data' in self.response_json:
            self.response_json_new = self.response_json.get("data")
        else:
            # Directly use response_json if it's not a dictionary with 'data' key
            self.response_json_new = self.response_json

    def validate_for_json_validator(self, schema):
        # Use response_json_new which now correctly handles both list and dict
        if isinstance(self.response_json_new, list):
            for item in self.response_json_new:
                validate(item, schema)
        else:
            validate(self.response_json_new, schema)

    def validate_for_pydentic_validator(self, schema):
        if isinstance(self.response_json_new, list):
            for item in self.response_json_new:
                # schema.model_validate(item)
                parsed_object = schema.parse_obj(item)
                self.parsed_object = parsed_object
        else:
            schema.model_validate(self.response_json_new)
        return self

    # def assert_status_code(self, status_code):
    #     if isinstance(status_code, list):
    #         assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
    #     else:
    #         assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
    #     return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def get_parsed_object(self):
        return self.parsed_object

    def __str__(self):
        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Requested url : {self.response.url} \n" \
            f"Response body : {self.response_json} \n"
