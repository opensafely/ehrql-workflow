from ehrql import Dataset
from ehrql.tables.beta.core import patients

dataset = Dataset()
index_date = "2022-01-01"

dataset.age = patients.age_on(index_date)

dataset.define_population(dataset.age >= 18)
