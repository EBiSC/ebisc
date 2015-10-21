$(document).ready ->
    $('.collapsible-menu-toggle').each (i, el) ->
        button = $(el)
        items = $("##{button.data('target')}")
        button.on 'click', (e) ->
            e.preventDefault()
            items.slideToggle () ->
                items.removeAttr "style" if items.is(':hidden')
