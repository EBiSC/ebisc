
config = {

    fields: [
        {
            name: 'biosamplesid'
            label: 'Biosamples ID'
        }
        {
            name: 'celllinename'
            label: 'Name'
        }
        {
            name: 'celllinenamesynonyms'
            label: 'Name synonyms'
        }
        {
            name: 'depositor'
            label: 'Depositor'
        }
        {
            name: 'celllineprimarydisease'
            label: 'Disease'
        }
        {
            name: 'celllinecelltype'
            label: 'Cell type'
        }
    ]

    query_fields: [
        'biosamplesid.analyzed'
        'celllinename.analyzed'
        'celllinenamesynonyms.analyzed'
        'depositor.analyzed'
        'celllinecelltype.analyzed'
        'celllineprimarydisease.analyzed'
    ]

    facets: [
        {
            name: 'celllineprimarydisease'
            label: 'Disease'
            selectedTerms: {}
        }
        {
            name: 'celllinecelltype'
            label: 'Cell line type'
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
