React = window.React
classNames = require 'classnames'
Config = require '../config'
State = require '../state'

Facets = React.createClass

    mixins: [State.mixin]

    cursors:
        items: ['facets']
        checked: ['filter', 'facets']

    render: () ->
        <div className="filter-group">
        {
            (<Facet key={i} facet={facet} items={@state.cursors.items[facet.name]} checked={@cursors.checked} /> for facet, i in Config.facets)
        }
        </div>

Facet = React.createClass

    render: () ->
        <div className="dropdown">
            <div className="dropdown-container">
                <div className="dropdown-button">{@props.facet.label}</div>
                <ul className="dropdown-menu checkbox">
                {   
                    if @props.items
                        (<Term key={i} item={item} /> for item, i in @props.items.buckets)
                }
                </ul>
            </div>
        </div>

Term = React.createClass

    render: () ->
        # <li onClick={@handleClick} className={classNames(selected: @state.cursors.item.checked)}>
        <li onClick={@handleClick}>
            <div className="checkbox"></div>
            <label>{_.capitalize(@props.item.key)}</label>
        </li>

    handleClick: (e) ->
        console.log @props.item
        # @props.cursor.set('checked', ! @props.cursor.get('checked'))

module.exports = Facets

