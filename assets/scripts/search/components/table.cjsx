Table = React.createClass

    render: () ->
        <table className="listing">
            <Thead cols={@props.cols} />
            <Tbody cols={@props.cols} rows={@props.rows} />
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
        <tbody>
        {
            for row, i in @props.rows
                <tr key={i}>{(<td key={i}>{col}</td> for col, i in row)}</tr>
        }
        </tbody>

module.exports = Table
