
config = {

    fields: [
        {
            name: 'biosamples_id'
            label: 'Biosamples ID'
        }
        {
            name: 'name'
            label: 'Name'
        }
        {
            name: 'alternative_names'
            label: 'Alternative names'
        }
        {
            name: 'depositor'
            label: 'Depositor'
        }
        {
            name: 'primary_disease'
            label: 'Disease'
        }
        {
            name: 'primary_cell_type'
            label: 'Primary cell type'
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
            name: 'depositor'
            label: 'Depositor'
            selectedTerms: {}
        }
    ]
}

module.exports = config
