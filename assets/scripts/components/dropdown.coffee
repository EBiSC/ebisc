$(document).ready ->

    $('.dropdown-button').click (event) ->

        dropdownButton = $(@)
        dropdownMenu = dropdownButton.next('.dropdown-menu')

        dropdownMenu.toggleClass 'show-menu'

        $(document).click (e) ->
            if $(e.target).closest(dropdownMenu).length == 0
                dropdownMenu.removeClass 'show-menu'

        event.stopPropagation()
