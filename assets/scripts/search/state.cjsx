Baobab = require 'baobab'

state = {
    filter:
        query: ''
        facets: []
    facetTerms: {}
    celllines: []
}

options =
    shiftReferences: true
    mixins: [React.addons.PureRenderMixin]

module.exports = new Baobab state, options
