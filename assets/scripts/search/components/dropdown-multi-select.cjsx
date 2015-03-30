classNames = require 'classnames'

DropdownMultiSelect = React.createClass

    getInitialState: () ->
        showMenu: false

    showMenu: () ->
        @setState showMenu: true
        window.addEventListener('click', @hideMenu, true)

    hideMenu: (e) ->

        if e.target == $('.dropdown-button', @getDOMNode())[0]

            e.stopPropagation()

            @setState showMenu: false
            window.removeEventListener('click', @hideMenu, true)

        else if not $(@getDOMNode()).has($(e.target)).length

            @setState showMenu: false
            window.removeEventListener('click', @hideMenu, true)

    componentWillUnmount: () ->
        window.removeEventListener('click', @hideMenu, true)

    render: () ->
        <div className="dropdown">
            <div className="dropdown-container">
                <div className="dropdown-button" onClick={@showMenu}>{@props.label}</div>
                <ul className={classNames('dropdown-menu': true, 'checkbox': true, 'show-menu': @state.showMenu)}>
                {(<Item key={item.name} item={item} action=@props.action /> for item in @props.items)}
                </ul>
            </div>
        </div>

Item = React.createClass

    handleOnClick: () ->
        @setState selected: not @state.selected
        @props.action(@props.item.name, not @state.selected)

    getInitialState: () ->
        selected: false

    render: () ->
        <li onClick={@handleOnClick} className={classNames(selected: @state.selected)}>
            <div className="checkbox"></div>
            <label>{_.capitalize(@props.item.label)}</label>
        </li>

module.exports = DropdownMultiSelect
