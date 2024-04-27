from fastapi import HTTPException


class MessageBody:
    error_code: int
    error_message: str

    def __init__(self, error_code, error_message):
        self.error_code = error_code
        self.error_message


def get_error_message_response(status: int, error_code: int, error_message: str):
    # status.HTTP_422_UNPROCESSABLE_ENTITY
    return HTTPException(
        status_code=status,
        detail=error_message)


def get_success_message_reponse(error_message: str):
    return HTTPException(
        status_code=200,
        detail=error_message)
