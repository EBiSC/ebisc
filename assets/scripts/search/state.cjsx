Baobab = require 'baobab'
ReactAddons = require 'react/addons'

state = {
    'celllines': undefined
    'facets': undefined
}

options =
    shiftReferences: true
    mixins: [ReactAddons.PureRenderMixin]

module.exports = new Baobab state, options
