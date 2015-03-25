React = require 'react'
State = require '../state'

Table = React.createClass

    mixins: [State.mixin]

    cursors:
        celllines: ['celllines']

    render: () ->
        <table>
            <thead>
                <tr>
                    <th>Biosamples ID</th>
                    <th>Cell line Name</th>
                    <th>Disease</th>
                    <th>Accepted</th>
                </tr>
            </thead>

            <tbody>{@renderBody(@state.cursors.celllines)}</tbody>
        </table>

    renderBody: (celllines) ->

        return '' if not celllines

        for cellline in celllines
            <tr key={cellline._id}>
                <td>{cellline._source.biosamplesid}</td>
                <td>{cellline._source.celllinename}</td>
                <td>{cellline._source.celllineprimarydisease}</td>
                <td>{cellline._source.celllineaccepted}</td>
            </tr>

module.exports = Table
