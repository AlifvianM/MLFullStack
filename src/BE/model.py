from pydantic import BaseModel

class InputData(BaseModel):
    sepal_length : float
    petal_length : float
    sepal_width : float
    petal_width : float

    def get_json(self):
        return {
            "sepal_length":self.sepal_length,
            "petal_length":self.petal_length,
            "sepal_width":self.sepal_width,
            "petal_width":self.petal_width
        }