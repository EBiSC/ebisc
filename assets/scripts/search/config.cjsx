
config = {

    fields: [
        {
            name: 'biosamplesid'
            label: 'Biosamples ID'
        }
        {
            name: 'celllinename'
            label: 'Cell line Name'
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
        {
            name: 'celllinenamesynonyms'
            label: 'Cell line name synonims'
        }
    ]

    query_fields: [
        'biosamplesid.analyzed'
        'celllinename.analyzed'
        'depositor.analyzed'
        'celllinecelltype.analyzed'
        'celllineprimarydisease.analyzed'
        'celllinenamesynonyms.analyzed'
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
