ReactCSSTransitionGroup = React.addons.CSSTransitionGroup

State = require '../state'
Actions = require '../actions'
DropdownMultiSelect = require './dropdown-multi-select'

Facets = React.createClass

    mixins: [State.mixin]

    cursors:
        facets: ['filter', 'facets']
        facetTerms: ['facetTerms']

    render: () ->

        <span>
            <span>
            {
                if _.size(@state.cursors.facetTerms)
                    <div className="filter-group">
                    {
                        for facet, i in @state.cursors.facets
                            selectedTerms = @getSelectedTerms(facet.name)
                            <div key={facet.name} className="filter">
                                <DropdownMultiSelect name={facet.name} label={facet.label} hasSelection={selectedTerms.length > 0} items={@getFacetTerms(facet.name, selectedTerms)} action={_.partial(Actions.updateFacetTermFilter, facet.name)} />
                                <SelectedTerms facet={facet} terms={selectedTerms} />
                            </div>
                    }
                    </div>
            }
            </span>
            <span>
            {
                if _.size(@state.cursors.facetTerms) and true in (@getSelectedTerms(facet.name).length > 0 for facet in @state.cursors.facets)
                    <div className="clear-all-filters" onClick={@clearFilters}><span className="glyphicon glyphicon-remove-sign"></span> Clear all filters</div>
            }
            </span>
        </span>

    clearFilters: () ->
        Actions.initFilter()

    getSelectedTerms: (facet) ->
        terms = @state.cursors.facets[_.findIndex(@state.cursors.facets, {name: facet})].selectedTerms
        (key for key, value of terms when value == true).sort()

    getFacetTerms: (facet, selectedTerms) ->

        # Buckets' locations are different for filtered / non-filtered facet aggregations

        if 'buckets' of @state.cursors.facetTerms[facet]
            terms = @state.cursors.facetTerms[facet].buckets
        else
            terms = @state.cursors.facetTerms[facet]['facet'].buckets

        ({name: term.key, label: "#{term.key} (#{term.doc_count})", selected: term.key in selectedTerms} for term in terms)

SelectedTerms = React.createClass

    render: () ->
        <ul className="selected-terms">
            <ReactCSSTransitionGroup transitionName="transition-opacity">
            {(<li key={term} className="term"><span className="remove glyphicon glyphicon-remove-sign" onClick={@createHandleOnRemove(term)}></span> {term}</li> for term in @props.terms)}
            </ReactCSSTransitionGroup>
        </ul>

    createHandleOnRemove: (term) ->
        () =>
            Actions.updateFacetTermFilter(@props.facet.name, term, false)

module.exports = Facets
