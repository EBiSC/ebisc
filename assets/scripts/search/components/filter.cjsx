React = window.React
classNames = require 'classnames'
State = require '../state'

Term = React.createClass

    render: () ->
        <li onClick={@handleClick} className={classNames(selected: @props.item.checked)}>
            <div className="checkbox"></div>
            <label>{_.capitalize(@props.item.name)}</label>
        </li>

    handleClick: (e) ->
        @props.cursor.set('checked', ! @props.cursor.get('checked'))

Facet = React.createClass

    render: () ->
        <div className="dropdown">
            <div className="dropdown-container">
                <div className="dropdown-button">{@props.facet.label}</div>
                <ul className="dropdown-menu checkbox">
                {
                    (<Term key={i} item={item} cursor={@props.cursor.select('items').select(i)} /> for item, i in @props.facet.items)
                }
                </ul>
            </div>
        </div>

Facets = React.createClass

    mixins: [State.mixin]

    cursors:
        facets: ['filter', 'facets']

    render: () ->
        <div className="filter-group">
        {
            (<Facet key={i} facet={facet} cursor={@cursors.facets.select(i)} /> for facet, i in @state.cursors.facets)
        }
        </div>

module.exports = Facets
