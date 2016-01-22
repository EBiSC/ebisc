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

    $('.js-accordion-trigger').bind 'click', (event) ->
        $(this).parent().find('.content').slideToggle('fast')
        $(this).parent().toggleClass('is-expanded')
        event.preventDefault()

    $('.accordion-tabs-minimal').each (index) ->
        location = window.location.hash.substr(1)
        if location.length and $(this).children('li[data-section="' + location + '"]').length
            active = $(this).children('li[data-section="' + location + '"]')
        else
            active = $(this).children('li').first()
        active.children('a').addClass('is-active').next().addClass('is-open').show()
        return

    $('.accordion-tabs-minimal').on 'click', 'li > a.tab-link', (event) ->
        if !$(this).hasClass('is-active')
          event.preventDefault()
          accordionTabs = $(this).closest('.accordion-tabs-minimal')
          accordionTabs.find('.is-open').removeClass('is-open').hide()
          $(this).next().toggleClass('is-open').toggle()
          accordionTabs.find('.is-active').removeClass 'is-active'
          $(this).addClass 'is-active'
        else
          event.preventDefault()
        if $(this).parent().data('section').length
            window.location.hash = $(this).parent().data('section')
        return
