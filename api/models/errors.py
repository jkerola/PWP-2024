class ApiException(Exception):
    message: str

    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

    def to_json(self) -> dict:
        return {"error": self.message}
