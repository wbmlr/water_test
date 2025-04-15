from pydantic import BaseModel



# We have trained the model on the features. In the train_processed.csv, the features appear in a sequence.
# In the data model, we provide the data fields in the same sequence.

class Water(BaseModel):
    ph : float
    Hardness : float
    Solids : float
    Chloramines : float
    Sulfate : float
    Conductivity : float
    Organic_carbon : float
    Trihalomethanes : float
    Turbidity : float