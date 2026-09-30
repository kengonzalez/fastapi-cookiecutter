from fastapi import status, HTTPException


class CustomAPIException(HTTPException):
    def __init__(self, status_code: int, detail: str, error_code: str = None):
        super().__init__(status_code=status_code, detail=detail)
        self.error_coode = error_code


class NotFoundError(CustomAPIException):
    def __init__(self, message: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message,
            error_code="NOT_FOUND",
        )


class BadRequestError(CustomAPIException):
    def __init__(self, message: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message,
            error_code="BAD_REQUEST",
        )


class InternalServerError(CustomAPIException):
    def __init__(self, message: str):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=message,
            error_code="INTERNAL_ERROR",
        )
