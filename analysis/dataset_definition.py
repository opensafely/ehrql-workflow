from ehrql import Dataset, codelist_from_csv
from ehrql.tables.beta.core import patients

diabetes_codelist = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-dm_cod.csv", column="code"
)

diabetes_resolved_codelist = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-dmres_cod.csv", column="code"
)

index_date = "2020-03-31"

dataset = Dataset()

dataset.age = patients.age_on(index_date)

dataset.define_population((dataset.age > 18))
