from ehrql import Dataset
from ehrql.tables.beta.core import patients

# Create dataset
dataset = Dataset()

# Create date_of_birth variable from patients table
dataset.date_of_birth = patients.date_of_birth

# Define study population
dataset.define_population(patients.date_of_birth.is_on_or_before("1999-12-31"))
