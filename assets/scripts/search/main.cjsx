React = require 'react'

state = require './state'

addAdmin = (name) ->
    state.select('users', 'admin').push(name)

addRegular = (name) ->
    state.select('users', 'regular').push(name)

MyComponent = React.createClass

    mixins: [state.mixin]
    cursors:
        admin: ['users', 'admin']
        regular: ['users', 'regular']

    renderUser: (user, i) ->
        <span key={i}>{user} </span>

    handleClick: () ->
        addAdmin 'a' + (@state.cursors.admin.length + 1).toString()
        addRegular 'r' + (@state.cursors.regular.length + 1).toString()

    render: () ->
        <div>
            <div>Admin: {@state.cursors.admin.map(@renderUser)}</div>
            <div>Regular: {@state.cursors.regular.map(@renderUser)}</div>
            <button onClick={@handleClick}>Click</button>
        </div>

React.render <MyComponent />, document.getElementById('content')
