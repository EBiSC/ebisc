
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
            name: 'celllineaccepted'
            label: 'Accepted'
        }
    ]
    query_fields: ['biosamplesid', 'celllinename', 'celllineprimarydisease']

}

module.exports = config
