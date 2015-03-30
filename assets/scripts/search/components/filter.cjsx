React = window.React
State = require '../state'
Actions = require '../actions'

DropdownMultiSelect = require './dropdown-multi-select'

Facets = React.createClass

    mixins: [State.mixin]

    cursors:
        facets: ['filter', 'facets']
        facetTerms: ['facetTerms']

    getItems: (facet, selectedTerms) ->

        # Buckets' locations are different for filtered / non-filtered facet aggregations

        if 'buckets' of @state.cursors.facetTerms[facet]
            terms = @state.cursors.facetTerms[facet].buckets
        else
            terms = @state.cursors.facetTerms[facet]['facet'].buckets

        ({name: term.key, label: "#{term.key} (#{term.doc_count})", selected: selectedTerms[term.key]} for term in terms)

    render: () ->
        <div className="filter-group">
        {
            if _.size(@state.cursors.facetTerms)
                for facet, i in @state.cursors.facets
                    selectedTerms = @state.cursors.facets[_.findIndex(@state.cursors.facets, {name: facet.name})].selectedTerms
                    <DropdownMultiSelect key={facet.name} name={facet.name} label={facet.label} items={@getItems(facet.name, selectedTerms)} action={_.partial(Actions.setFilterFacetTerm, facet.name)}/>
        }
        </div>

module.exports = Facets
