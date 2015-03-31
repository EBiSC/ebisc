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

    clearFilters: () ->
        Actions.initFilter()

    render: () ->

        getSelectedTerms = (facetName) =>
            terms = @state.cursors.facets[_.findIndex(@state.cursors.facets, {name: facetName})].selectedTerms
            _.object(([key, value] for key, value of terms when value == true))

        <span>
            <span>
            {
                if _.size(@state.cursors.facetTerms)
                    <div className="filter-group">
                    {
                        for facet, i in @state.cursors.facets
                            selectedTerms = getSelectedTerms(facet.name)
                            <DropdownMultiSelect key={facet.name} name={facet.name} label={facet.label} hasSelection={_.size(selectedTerms) > 0} items={@getItems(facet.name, selectedTerms)} action={_.partial(Actions.updateFacetTermFilter, facet.name)}/>
                    }
                    </div>
            }
            </span>

            <span>
            {
                if true in (_.size(getSelectedTerms(facet.name)) > 0 for facet in @state.cursors.facets)
                    <div className="clear" onClick={@clearFilters}><span className="glyphicon glyphicon-remove-sign"></span> Clear filters</div>
            }
            </span>
        </span>

module.exports = Facets
