Baobab = require 'baobab'
ReactAddons = window.React.addons

state = {
    filter:
        query: ''
        facets: [
            {
                name: 'celllineaccepted'
                label: 'Accepted'
                items: [
                    {name: 'pending', checked: false}
                    {name: 'accepted', checked: false}
                    {name: 'rejected', checked: false}
                ]
            }
            {
                name: 'celllineprimarydisease'
                label: 'Disease'
                items: [
                    {name: 'Control', checked: false}
                ]
            }
        ]
    celllines: []
}

options =
    shiftReferences: true
    mixins: [ReactAddons.PureRenderMixin]

module.exports = new Baobab state, options
