
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
}

module.exports = config
