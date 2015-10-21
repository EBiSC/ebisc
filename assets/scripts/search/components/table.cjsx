Table = React.createClass

    render: () ->
        <table className="listing">
            <Thead cols={@props.cols} orderBy={@props.orderBy} onOrderBy={@props.onOrderBy} />
            <Tbody cols={@props.cols} rows={@props.rows} />
        </table>

Thead = React.createClass

    render: () ->
        <thead>
            <tr>{(<Th key={col.name} col={col} orderBy={@props.orderBy} onOrderBy={@props.onOrderBy} /> for col in @props.cols)}</tr>
        </thead>

    renderTh: (col, i) ->


Th = React.createClass

    render: () ->
        if @props.orderBy != null and @props.col.name == @props.orderBy.field
            <th onClick={@handleOnClick} className="order-by #{@props.orderBy.direction}"><span className="sort">{@props.col.label}</span></th>
        else
            <th onClick={@handleOnClick}><span className="sort">{@props.col.label}</span></th>

    handleOnClick: () ->
        if @props.orderBy != null and @props.orderBy.field == @props.col.name
            if @props.orderBy.direction == 'asc'
                @props.onOrderBy(field: @props.col.name, direction: 'desc')
            else
                @props.onOrderBy(null)
        else
            @props.onOrderBy(field: @props.col.name, direction: 'asc')


Tbody = React.createClass

    render: () ->
        <tbody>
        {
            for row, i in @props.rows
                <tr key={i}>{(<td key={i}>{col}</td> for col, i in row)}</tr>
        }
        </tbody>

module.exports = Table
