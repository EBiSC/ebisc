Baobab = require 'baobab'
ReactAddons = window.React.addons

state = {
    'query': ''
    'facets': undefined
    'celllines': []
}

options =
    shiftReferences: true
    mixins: [ReactAddons.PureRenderMixin]

module.exports = new Baobab state, options
