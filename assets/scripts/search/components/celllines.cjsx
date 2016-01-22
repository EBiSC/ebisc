Config = require '../config'
State = require '../state'
Table = require './table'
Actions = require '../actions'

Celllines = React.createClass

    mixins: [State.mixin]

    cursors:
        isLoaded: ['isLoaded']
        celllines: ['celllines']
        orderBy: ['filter', 'orderBy']

    render: () ->

        buildCell = (name, row) ->
            value = row._source[name]

            if name == 'name'
                <a href="./#{value}/">{value}</a>
            else
                value

        buildRow = (row, cols) ->
            (buildCell(col.name, row) for col in cols)

        rows = (buildRow(row, Config.fields) for row in @state.cursors.celllines)

        <div>
        {
            if @state.cursors.isLoaded
                <Table cols={Config.fields} rows={rows} orderBy={@state.cursors.orderBy} onOrderBy={Actions.orderBy} />
        }
        </div>

module.exports = Celllines
