Baobab = require 'baobab'
ReactAddons = window.React.addons

state = {
    filter:
        query: ''
        facets: [
            {
                name: 'celllinecelltype'
                label: 'Cell line type'
                items: [
                    {name: 'Dermal Fibroblasts'}
                    {name: 'Foreskin Keratinocytes'}
                    {name: 'Unknown'}
                ]
            }
            {
                name: 'celllineprimarydisease'
                label: 'Disease'
                items: [
                    {name: 'Control'}
                    {name: 'Long QT Syndrome-3'}
                ]
            }
        ]
    celllines: []
}

options =
    shiftReferences: true
    mixins: [ReactAddons.PureRenderMixin]

module.exports = new Baobab state, options
