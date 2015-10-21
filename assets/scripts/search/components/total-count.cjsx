State = require '../state'

TotalCount = React.createClass

    mixins: [State.mixin]

    cursors:
        isLoaded: ['isLoaded']
        celllines: ['celllines']

    render: () ->
        <div>
        {
            if @state.cursors.isLoaded
                <div>
                    <span className="count">{@state.cursors.celllines.length}</span>
                    <span className="unit">{@state.cursors.celllines.length %% 100 == 1 and 'cell line' or 'cell lines'}</span>
                </div>
        }
        </div>

module.exports = TotalCount
