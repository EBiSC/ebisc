React = window.React
State = require '../state'
Actions = require '../actions'

DropdownMultiSelect = require './dropdown-multi-select'

Facets = React.createClass

    mixins: [State.mixin]

    cursors:
        facets: ['filter', 'facets']
        facetTerms: ['facetTerms']

    getItems: (facet) ->
        ({name: term.key, label: "#{term.key} (#{term.doc_count})"} for term in @state.cursors.facetTerms[facet].buckets)

    render: () ->
        <div className="filter-group">
        {
            if _.size(@state.cursors.facetTerms)
                for facet, i in @state.cursors.facets
                    <DropdownMultiSelect key={i} name={facet.name} label={facet.label} items={@getItems(facet.name)} action={_.partial(Actions.setFilterFacetTerm, facet.name)}/>
        }
        </div>

module.exports = Facets
