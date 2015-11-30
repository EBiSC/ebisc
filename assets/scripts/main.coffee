$(document).ready ->

    $('.collapsible-menu-toggle').each (i, el) ->
        button = $(el)
        items = $("##{button.data('target')}")
        button.on 'click', (e) ->
            e.preventDefault()
            items.slideToggle () ->
                items.removeAttr "style" if items.is(':hidden')

    $('.dropdown-button').on 'click', (event) ->
        dropdownButton = $(@)
        dropdownMenu = dropdownButton.next('.dropdown-menu')
        dropdownMenu.toggleClass 'show-menu'
        $(document).click (e) ->
            if $(e.target).closest(dropdownMenu).length == 0
                dropdownMenu.removeClass 'show-menu'
        event.stopPropagation()
