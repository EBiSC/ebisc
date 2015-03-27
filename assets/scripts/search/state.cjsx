Baobab = require 'baobab'

state = {
    filter:
        query: ''
        facets: {}
    celllines: []
    facets: []
}

options =
    shiftReferences: true
    mixins: [React.addons.PureRenderMixin]

module.exports = new Baobab state, options
