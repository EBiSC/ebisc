$(document).ready ->

    $('.dropdown-button').click ->

        dropdownButton = $(@)
        dropdownMenu = dropdownButton.next('.dropdown-menu')

        dropdownMenu.toggleClass 'show-menu'

        $('> li', dropdownMenu).click ->
            dropdownMenu.removeClass 'show-menu'

        $('> li', dropdownMenu).click ->
            dropdownButton.html $('label', @).html()
