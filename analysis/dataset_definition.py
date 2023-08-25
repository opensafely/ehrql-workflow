from ehrql import Dataset, codelist_from_csv
from ehrql.tables.beta.core import patients, clinical_events

# Define codelists
diabetes_codelist = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-dm_cod.csv", column="code"
)

diabetes_resolved_codelist = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-dmres_cod.csv", column="code"
)

index_date = "2020-03-31"


# Create dataset
dataset = Dataset()

prior_clinical_events = clinical_events.where(
    clinical_events.date.is_on_or_before(index_date)
)

latest_diabetes_event = (
    prior_clinical_events.where(
        prior_clinical_events.snomedct_code.is_in(diabetes_codelist)
    )
    .sort_by(prior_clinical_events.date)
    .last_for_patient()
)

latest_diabetes_resolved_event = (
    prior_clinical_events.where(
        prior_clinical_events.snomedct_code.is_in(diabetes_resolved_codelist)
    )
    .sort_by(prior_clinical_events.date)
    .last_for_patient()
)

# Create date_of_birth variable from patients table
dataset.age = patients.age_on(index_date)
dataset.has_diabetes = latest_diabetes_resolved_event.date < latest_diabetes_event.date

# Define study population
dataset.define_population((dataset.age > 18) & dataset.has_diabetes)
