config = {

    fields: [
        {
            name: 'name'
            label: 'Name'
        }
        {
            name: 'donor_disease'
            label: 'Donor disease status'
        }
        {
            name: 'genetic_modification_disease'
            label: 'Genetic modification'
        }
        {
            name: 'donor_sex'
            label: 'Donor sex'
        }
        {
            name: 'donor_age'
            label: 'Donor age'
        }
        {
            name: 'primary_cell_type'
            label: 'Primary cell type'
        }
    ]

    query_fields: [
        'biosamples_id.analyzed'
        'name.analyzed'
        'alternative_names.analyzed'
        'depositor.analyzed'
        'primary_cell_type.analyzed'
        'donor_disease.analyzed'
        'genetic_modification_disease.analyzed'
        'primary_disease_synonyms'
        'disease_associated_phenotypes.analyzed'
        'non_disease_associated_phenotypes.analyzed'
        'donor_sex.analyzed'
        'donor_age.analyzed'
        'all_genes.analyzed'
    ]

    facets: [
        {
            name: 'all_diseases'
            label: 'Disease'
            selectedTerms: {}
        }
        {
            name: 'primary_cell_type'
            label: 'Primary cell type'
            selectedTerms: {}
        }
        {
            name: 'donor_sex'
            label: 'Donor sex'
            selectedTerms: {}
        }
        {
            name: 'donor_age'
            label: 'Donor age'
            selectedTerms: {}
        }
    ]
}

module.exports = config
