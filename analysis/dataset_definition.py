from ehrql import Dataset, codelist_from_csv
from ehrql.tables.beta.core import patients, clinical_events

# Define codelists
diabetes_codelist = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-dm_cod.csv",
    column="code"
    )

diabetes_resolved_codelist = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-dmres_cod.csv",
    column="code"
    )

# Create dataset
dataset = Dataset()

# Create date_of_birth variable from patients table
dataset.date_of_birth = patients.date_of_birth

# Define study population
dataset.define_population(patients.date_of_birth.is_on_or_before("1999-12-31"))
