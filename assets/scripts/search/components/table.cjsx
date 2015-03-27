React = window.React
State = require '../state'

Table = React.createClass

    mixins: [State.mixin]

    cursors:
        celllines: ['celllines']

    render: () ->
        <table className="listing">
            <Thead cols={@props.cols} />
            <Tbody cols={@props.cols} data={@state.cursors.celllines} />
        </table>

Thead = React.createClass

    render: () ->
        <thead>
            <tr>
                {(<th key={i}>{ col.label }</th> for col, i in @props.cols)}
            </tr>
        </thead>

Tbody = React.createClass

    render: () ->

        return '' if not @props.data

        <tbody>
        {
            for row in @props.data
                <tr key={row._id}>
                {
                    for col, i in @props.cols
                        <td key={i}>{row._source[col.name]}</td>
                }
                </tr>
        }
        </tbody>

module.exports = Table
