Baobab = require 'baobab'
ReactAddons = require 'react/addons'

state = 
    users:
        admin: ['a1', 'a2']
        regular: ['r1', 'r2', 'r3']

options =
    shiftReferences: true
    mixins: [ReactAddons.PureRenderMixin]

module.exports = new Baobab state, options
