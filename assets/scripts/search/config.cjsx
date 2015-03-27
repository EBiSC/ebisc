
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
            name: 'celllineprimarydisease'
            label: 'Disease'
        }
        {
            name: 'celllinecelltype'
            label: 'Cell type'
        }
    ]

    query_fields: [
        'biosamplesid'
        'celllinename'
        'celllinecelltype.analyzed'
        'celllineprimarydisease.analyzed'
    ]

    facets: [
        {
            name: 'celllinecelltype'
            label: 'Cell line type'
        }
        {
            name: 'celllineprimarydisease'
            label: 'Disease'
        }
    ]
}

module.exports = config
