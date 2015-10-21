Baobab = require 'baobab'

state = {
    filter:
        query: ''
        facets: []
        orderBy: null
    facetTerms: {}
    celllines: []
    isLoaded: false
}

options =
    shiftReferences: true
    mixins: [React.addons.PureRenderMixin]

module.exports = new Baobab state, options
