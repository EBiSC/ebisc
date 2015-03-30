Config = require '../config'
State = require '../state'
Table = require './table'

Celllines = React.createClass

    mixins: [State.mixin]

    cursors:
        celllines: ['celllines']

    render: () ->

        buildCell = (name, row) ->
            value = row._source[name]

            if name == 'biosamplesid'
                <a href="./#{value}/">{value}</a>           
            else
                value

        buildRow = (row, cols) ->
            (buildCell(col.name, row) for col in cols)

        rows = (buildRow(row, Config.fields) for row in @state.cursors.celllines)

        <Table cols={Config.fields} rows={rows} />

module.exports = Celllines        
