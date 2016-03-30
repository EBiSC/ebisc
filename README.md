# EBiSC


## Development setup

    virtualenv var/virtualenv
    go ebisc
    pip install -r requirements.txt
    createdb ebisc
    cd ebisc/settings/ ; ln -s develop.py __init__.py ; cd -
    ./manage.py migrate
    ./manage.py initcms
    ./manage.py loaddata var/fixtures/auth.json
    npm install
    bower install

In one shell run `./manage.py runserver` and then in the other `gulp watch`.


## BioSolr / Elasticsearch Ontology Plugin

https://github.com/flaxsearch/BioSolr
https://github.com/flaxsearch/BioSolr/tree/master/swat4ls_demo/elasticsearch

Documentation:

https://github.com/flaxsearch/BioSolr/tree/master/ontology/ontology-annotator/elasticsearch-ontology-annotator

To install the plugin:

    plugin install file:///path/to/ebisc/lib/es-ontology-annotator-es2.2-0.1.zip


Don't forget to restart the Elasticsearch after you installed the plugin.

Annotations work for fields that contain purls (it does not automatically assign purls to free text). You must specify them in the mapping file:

    {
      "cellline": {
        "properties": {

          "name": {
            "type": "string",
            "index": "not_analyzed",
            "fields": {"analyzed": {"type": "string", "index": "analyzed"}}
          },

          "cell_type": {
            "type": "ontology",
            "ontology": {
              "olsBaseURL": "http://www.ebi.ac.uk/ols/beta/api",
              "olsOntology": "efo",
              "includeIndirect": true,
              "includeRelations": true,
              "includeParentPaths": false,
              "includeParentPathLabels": true              
            }
          }
        }
      }
    }

The includeIndirect property indicates whether or not the field should include all ancestors and descendants in the data (indirect parent/child relationships), or just the direct parent and child nodes. If true, sub-fields called ancestor_uris, ancestor_labels, descendant_uris and descendant_labels will be created, as well as the parent/child fields.

The includeRelations property indicates whether or not additional relationships between nodes should be included with the data. If true, relationships such as "has disease location", "participates in", etc., will be included with the annotation data.

The includeParentPaths property indicates whether or not the parent paths from the annotated node to the root should be generated and added to the data. If this is set to true, you can also set the includeParentPathLabels property to add the parent node labels to the parent paths string. These will be added to a sub-field called parent_paths. Note that this property is set to false by default.
