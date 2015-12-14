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

    $('.accordion-tabs-minimal').each (index) ->
        $(this).children('li').first().children('a').addClass('is-active').next().addClass('is-open').show()
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
        return

    do (jQuery) ->
      jQuery.mark = jump: (options) ->
        defaults = selector: 'a.scroll-on-page-link'
        if typeof options == 'string'
          defaults.selector = options
        options = jQuery.extend(defaults, options)
        jQuery(options.selector).click (e) ->
          jumpobj = jQuery(this)
          target = jumpobj.attr('href')
          thespeed = 1000
          offset = jQuery(target).offset().top
          jQuery('html,body').animate { scrollTop: offset }, thespeed, 'swing'
          e.preventDefault()
          return
      return
    jQuery ->
      jQuery.mark.jump()
      return
