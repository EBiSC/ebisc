
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
            name: 'celllinecelltype'
            label: 'Cell type'
        }
    ]

    query_fields: [
        'biosamples_id.analyzed'
        'name.analyzed'
        'alternative_names.analyzed'
        'depositor.analyzed'
        'celllinecelltype.analyzed'
        'primary_disease.analyzed'
        'celllineprimarydisease_synonyms'
    ]

    facets: [
        {
            name: 'primary_disease'
            label: 'Disease'
            selectedTerms: {}
        }
        {
            name: 'celllinecelltype'
            label: 'Cell type'
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
