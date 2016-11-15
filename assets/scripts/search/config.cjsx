config = {

    fields: [
        {
            name: 'name'
            label: 'Name'
        }
        {
            name: 'primary_disease'
            label: 'Disease'
        }
        {
            name: 'primary_cell_type'
            label: 'Primary cell type'
        }
        {
            name: 'donor_sex'
            label: 'Donor sex'
        }
        {
            name: 'depositor'
            label: 'Depositor'
        }
    ]

    query_fields: [
        'biosamples_id.analyzed'
        'name.analyzed'
        'alternative_names.analyzed'
        'depositor.analyzed'
        'primary_cell_type.analyzed'
        'primary_disease.analyzed'
        'primary_disease_synonyms'
        'primary_disease_stage.analyzed'
        'disease_associated_phenotypes.analyzed'
        'non_disease_associated_phenotypes.analyzed'
        'donor_sex.analyzed'
    ]

    facets: [
        {
            name: 'primary_disease'
            label: 'Disease'
            selectedTerms: {}
        }
        {
            name: 'primary_cell_type'
            label: 'Primary cell type'
            selectedTerms: {}
        }
        {
            name: 'donor_sex'
            label: 'Donor sex'
            selectedTerms: {}
        }
        {
            name: 'depositor'
            label: 'Depositor'
            selectedTerms: {}
        }
    ]
}

module.exports = config
