# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import dirtyfields.dirtyfields
import django.contrib.postgres.fields
import ebisc.celllines.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10, verbose_name='Age range')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Age range',
                'verbose_name_plural': 'Age ranges',
            },
        ),
        migrations.CreateModel(
            name='BatchCultureConditions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('culture_medium', models.CharField(max_length=100, null=True, verbose_name='Medium', blank=True)),
                ('passage_method', models.CharField(max_length=100, null=True, verbose_name='Passage method', blank=True)),
                ('matrix', models.CharField(max_length=100, null=True, verbose_name='Matrix', blank=True)),
                ('o2_concentration', models.CharField(max_length=12, null=True, verbose_name='O2 Concentration', blank=True)),
                ('co2_concentration', models.CharField(max_length=12, null=True, verbose_name='CO2 Concentration', blank=True)),
                ('temperature', models.CharField(max_length=12, null=True, verbose_name='Temperature', blank=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Batch culture conditions',
                'verbose_name_plural': 'Batch culture conditions',
            },
        ),
        migrations.CreateModel(
            name='Cellline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accepted', models.CharField(default=b'pending', max_length=10, verbose_name='Cell line accepted', choices=[(b'pending', 'Pending'), (b'accepted', 'Accepted'), (b'rejected', 'Rejected')])),
                ('name', models.CharField(unique=True, max_length=15, verbose_name='Cell line name')),
                ('alternative_names', models.CharField(max_length=500, null=True, verbose_name='Cell line alternative names', blank=True)),
                ('biosamples_id', models.CharField(unique=True, max_length=12, verbose_name='Biosamples ID')),
                ('hescreg_id', models.CharField(max_length=10, unique=True, null=True, verbose_name='hESCreg ID', blank=True)),
                ('ecacc_id', models.CharField(max_length=10, unique=True, null=True, verbose_name='ECACC ID', blank=True)),
                ('primary_disease_diagnosis', models.CharField(max_length=12, null=True, verbose_name='Disease diagnosis', blank=True)),
                ('primary_disease_stage', models.CharField(max_length=100, null=True, verbose_name='Disease stage', blank=True)),
                ('disease_associated_phenotypes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), null=True, verbose_name='Disease associated phenotypes', size=None)),
                ('affected_status', models.CharField(max_length=12, null=True, verbose_name='Affected status', blank=True)),
                ('family_history', models.CharField(max_length=500, null=True, verbose_name='Family history', blank=True)),
                ('medical_history', models.CharField(max_length=500, null=True, verbose_name='Medical history', blank=True)),
                ('clinical_information', models.CharField(max_length=500, null=True, verbose_name='Clinical information', blank=True)),
            ],
            options={
                'ordering': ['biosamples_id'],
                'verbose_name': 'Cell line',
                'verbose_name_plural': 'Cell lines',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CelllineAliquot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('biosamples_id', models.CharField(unique=True, max_length=12, verbose_name='Biosamples ID')),
            ],
            options={
                'ordering': ['biosamples_id'],
                'verbose_name': 'Cell line aliquot',
                'verbose_name_plural': 'Cell line aliquotes',
            },
        ),
        migrations.CreateModel(
            name='CelllineBatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('biosamples_id', models.CharField(unique=True, max_length=12, verbose_name='Biosamples ID')),
                ('batch_id', models.CharField(max_length=12, verbose_name='Batch ID')),
                ('vials_at_roslin', models.IntegerField(null=True, verbose_name='Vials at Central facility', blank=True)),
                ('vials_shipped_to_ecacc', models.IntegerField(null=True, verbose_name='Vials shipped to ECACC', blank=True)),
                ('vials_shipped_to_fraunhoffer', models.IntegerField(null=True, verbose_name='Vials shipped to Fraunhoffer', blank=True)),
                ('certificate_of_analysis', models.FileField(upload_to=ebisc.celllines.models.upload_to, null=True, verbose_name='Certificate of analysis', blank=True)),
                ('certificate_of_analysis_md5', models.CharField(max_length=100, null=True, verbose_name='Certificate of analysis md5', blank=True)),
                ('cell_line', models.ForeignKey(related_name='batches', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['biosamples_id'],
                'verbose_name': 'Cell line batch',
                'verbose_name_plural': 'Cell line batches',
            },
        ),
        migrations.CreateModel(
            name='CelllineBatchImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_file', models.FileField(upload_to=ebisc.celllines.models.upload_to, verbose_name='Image file')),
                ('image_md5', models.CharField(max_length=100, verbose_name='Image file md5')),
                ('magnification', models.CharField(max_length=10, null=True, verbose_name='Magnification', blank=True)),
                ('time_point', models.CharField(max_length=100, null=True, verbose_name='Time point', blank=True)),
                ('batch', models.ForeignKey(related_name='images', verbose_name='Cell line Batch images', to='celllines.CelllineBatch')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line batch image',
                'verbose_name_plural': 'Cell line batch images',
            },
        ),
        migrations.CreateModel(
            name='CelllineCharacterization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('certificate_of_analysis_passage_number', models.CharField(max_length=10, null=True, verbose_name='Certificate of analysis passage number', blank=True)),
                ('screening_hiv1', models.CharField(blank=True, max_length=20, null=True, verbose_name='Hiv1 screening', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not_done', 'Not done')])),
                ('screening_hiv2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Hiv2 screening', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not_done', 'Not done')])),
                ('screening_hepatitis_b', models.CharField(blank=True, max_length=20, null=True, verbose_name='Hepatitis b', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not_done', 'Not done')])),
                ('screening_hepatitis_c', models.CharField(blank=True, max_length=20, null=True, verbose_name='Hepatitis c', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not_done', 'Not done')])),
                ('screening_mycoplasma', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mycoplasma', choices=[(b'positive', 'Positive'), (b'negative', 'Negative'), (b'not_done', 'Not done')])),
                ('cell_line', models.OneToOneField(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': ['cell_line'],
                'verbose_name': 'Cell line characterization',
                'verbose_name_plural': 'Cell line characterizations',
            },
        ),
        migrations.CreateModel(
            name='CelllineCultureConditions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('surface_coating', models.CharField(max_length=100, null=True, verbose_name='Surface coating', blank=True)),
                ('feeder_cell_type', models.CharField(max_length=45, null=True, verbose_name='Feeder cell type', blank=True)),
                ('feeder_cell_id', models.CharField(max_length=45, null=True, verbose_name='Feeder cell id', blank=True)),
                ('passage_method', models.CharField(max_length=100, null=True, verbose_name='Passage method', blank=True)),
                ('enzymatically', models.CharField(max_length=45, null=True, verbose_name='Enzymatically', blank=True)),
                ('enzyme_free', models.CharField(max_length=45, null=True, verbose_name='Enzyme free', blank=True)),
                ('o2_concentration', models.IntegerField(null=True, verbose_name='O2 concentration', blank=True)),
                ('co2_concentration', models.IntegerField(null=True, verbose_name='Co2 concentration', blank=True)),
                ('other_culture_environment', models.CharField(max_length=100, null=True, verbose_name='Other culture environment', blank=True)),
                ('culture_medium', models.CharField(max_length=45, null=True, verbose_name='Culture medium', blank=True)),
                ('passage_number_banked', models.CharField(max_length=10, null=True, verbose_name='Passage number banked (pre-EBiSC)', blank=True)),
                ('number_of_vials_banked', models.CharField(max_length=10, null=True, verbose_name='No. Vials banked (pre-EBiSC)', blank=True)),
                ('passage_history', models.NullBooleanField(default=None, verbose_name='Passage history (back to reprogramming)')),
                ('culture_history', models.NullBooleanField(default=None, verbose_name='Culture history (methods used)')),
                ('cell_line', models.OneToOneField(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line culture conditions',
                'verbose_name_plural': 'Cell line culture conditions',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CelllineCultureMediumSupplement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplement', models.CharField(max_length=45, verbose_name='Supplement')),
                ('amount', models.CharField(max_length=45, null=True, verbose_name='Amount', blank=True)),
                ('cell_line_culture_conditions', models.ForeignKey(related_name='medium_supplements', verbose_name='Cell line culture conditions', to='celllines.CelllineCultureConditions')),
            ],
            options={
                'ordering': ['supplement'],
                'verbose_name': 'Cell line culture supplements',
                'verbose_name_plural': 'Cell line culture supplements',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CelllineDerivation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary_cell_developmental_stage', models.CharField(max_length=45, null=True, verbose_name='Primary cell developmental stage', blank=True)),
                ('tissue_procurement_location', models.CharField(max_length=45, null=True, verbose_name='Location of primary tissue procurement', blank=True)),
                ('tissue_collection_date', models.DateField(null=True, verbose_name='Tissue collection date', blank=True)),
                ('reprogramming_passage_number', models.CharField(max_length=10, null=True, verbose_name='Passage number reprogrammed', blank=True)),
                ('selection_criteria_for_clones', models.TextField(null=True, verbose_name='Selection criteria for clones', blank=True)),
                ('xeno_free_conditions', models.NullBooleanField(default=None, verbose_name='Xeno free conditions')),
                ('derived_under_gmp', models.NullBooleanField(default=None, verbose_name='Derived under gmp')),
                ('available_as_clinical_grade', models.NullBooleanField(default=None, verbose_name='Available as clinical grade')),
                ('cell_line', models.OneToOneField(related_name='derivation', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line derivation',
                'verbose_name_plural': 'Cell line derivations',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CellLineDifferentiationPotency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passage_number', models.CharField(max_length=5, verbose_name='Passage number', blank=True)),
                ('cell_line', models.ForeignKey(verbose_name='Cell line', blank=True, to='celllines.Cellline', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line differentiation potency',
                'verbose_name_plural': 'Cell line differentiation potencies',
            },
        ),
        migrations.CreateModel(
            name='CellLineDifferentiationPotencyMarker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_line_differentiation_potency', models.ForeignKey(verbose_name='Cell line differentiation potency', blank=True, to='celllines.CellLineDifferentiationPotency', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line differentiation potency marker',
                'verbose_name_plural': 'Cell line differentiation potency markers',
            },
        ),
        migrations.CreateModel(
            name='CellLineDifferentiationPotencyMolecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_line_differentiation_potency_marker', models.ForeignKey(verbose_name='Cell line differentiation potency marker', blank=True, to='celllines.CellLineDifferentiationPotencyMarker', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line differentiation potency molecule',
                'verbose_name_plural': 'Cell line differentiation potency molecules',
            },
        ),
        migrations.CreateModel(
            name='CelllineDiseaseGenotype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allele_carried', models.CharField(max_length=12, null=True, verbose_name='Allele carried through', blank=True)),
                ('cell_line_form', models.CharField(max_length=12, null=True, verbose_name='Is the cell line homozygote or heterozygot for this variant', blank=True)),
                ('assembly', models.CharField(max_length=45, null=True, verbose_name='Assembly', blank=True)),
                ('chormosome', models.CharField(max_length=45, null=True, verbose_name='Chormosome', blank=True)),
                ('coordinate', models.CharField(max_length=45, null=True, verbose_name='Coordinate', blank=True)),
                ('reference_allele', models.CharField(max_length=45, null=True, verbose_name='Reference allele', blank=True)),
                ('alternative_allele', models.CharField(max_length=45, null=True, verbose_name='Alternative allele', blank=True)),
                ('protein_sequence_variants', models.CharField(max_length=100, null=True, verbose_name='Protein sequence variants', blank=True)),
                ('cell_line', models.OneToOneField(related_name='genotyping_variant', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line disease associated genotype',
                'verbose_name_plural': 'Cell line disease associated genotypes',
            },
        ),
        migrations.CreateModel(
            name='CelllineEthics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('donor_consent', models.NullBooleanField(verbose_name='Donor consent')),
                ('no_pressure_statement', models.NullBooleanField(verbose_name='No pressure statement')),
                ('no_inducement_statement', models.NullBooleanField(verbose_name='No inducement statement')),
                ('donor_consent_form', models.NullBooleanField(verbose_name='Copy of consent form')),
                ('donor_consent_form_url', models.URLField(null=True, verbose_name='URL of donor consent form', blank=True)),
                ('known_location_of_consent_form', models.NullBooleanField(verbose_name='Do you know who holds the consent form')),
                ('copy_of_consent_form_obtainable', models.NullBooleanField(verbose_name='Is copy of consent form obtainable')),
                ('obtain_new_consent_form', models.NullBooleanField(verbose_name='Is new form obtainable')),
                ('donor_recontact_agreement', models.NullBooleanField(verbose_name='Has the donor agreed to be recontacted')),
                ('consent_anticipates_donor_notification_research_results', models.NullBooleanField(verbose_name='Consent anticipates the donor will be notified of results of research involving the donated samples or derived cells')),
                ('donor_expects_notification_health_implications', models.NullBooleanField(verbose_name='Donor expects to be informed if, during use of donated material, something with significant health implications for the donor is discovered')),
                ('copy_of_donor_consent_information_english_obtainable', models.NullBooleanField(verbose_name='Is copy of consent information obtainable in English')),
                ('copy_of_donor_consent_information_english_url', models.URLField(null=True, verbose_name='URL of donor consent information in English', blank=True)),
                ('copy_of_donor_consent_form_english_obtainable', models.NullBooleanField(verbose_name='Is copy of consent form obtainable in English')),
                ('copy_of_donor_consent_form_english_url', models.URLField(null=True, verbose_name='URL of donor consent form in English', blank=True)),
                ('consent_permits_ips_derivation', models.NullBooleanField(verbose_name='Consent expressly permits derivation of iPS cells')),
                ('consent_pertains_specific_research_project', models.NullBooleanField(verbose_name='Consent pertains to one specific research project')),
                ('consent_permits_future_research', models.NullBooleanField(verbose_name='Consent permits unforeseen future research')),
                ('future_research_permitted_specified_areas', models.NullBooleanField(verbose_name='Future research is permitted only in relation to specified areas or types of research')),
                ('future_research_permitted_areas', models.TextField(null=True, verbose_name='Future research permitted areas or types', blank=True)),
                ('consent_permits_clinical_treatment', models.NullBooleanField(verbose_name='Consent permits uses for clinical treatment or human applications')),
                ('formal_permission_for_distribution', models.NullBooleanField(verbose_name='Formal permission from the owner for distribution')),
                ('consent_permits_research_by_academic_institution', models.NullBooleanField(verbose_name='Consent permits research by academic institution')),
                ('consent_permits_research_by_org', models.NullBooleanField(verbose_name='Consent permits research by public organization')),
                ('consent_permits_research_by_non_profit_company', models.NullBooleanField(verbose_name='Consent permits research by non-profit company')),
                ('consent_permits_research_by_for_profit_company', models.NullBooleanField(verbose_name='Consent permits research by for-profit company')),
                ('consent_permits_development_of_commercial_products', models.NullBooleanField(verbose_name='Consent permits development of commercial products')),
                ('consent_expressly_prevents_commercial_development', models.NullBooleanField(verbose_name='Consent expressly prevents commercial development')),
                ('consent_expressly_prevents_financial_gain', models.NullBooleanField(verbose_name='Consent expressly prevents financial gain')),
                ('further_constraints_on_use', models.NullBooleanField(verbose_name='Any further constraints on use')),
                ('further_constraints_on_use_desc', models.TextField(null=True, verbose_name='Further constraints on use', blank=True)),
                ('consent_expressly_permits_indefinite_storage', models.NullBooleanField(verbose_name='Consent expressly permits indefinite storage')),
                ('consent_prevents_availiability_to_worldwide_research', models.NullBooleanField(verbose_name='Consent prevents availiability to worldwide research')),
                ('consent_permits_genetic_testing', models.NullBooleanField(verbose_name='Consent permits genetic testing')),
                ('consent_permits_testing_microbiological_agents_pathogens', models.NullBooleanField(verbose_name='Consent permits testing for microbiological agents pathogens')),
                ('derived_information_influence_personal_future_treatment', models.NullBooleanField(verbose_name='Derived information may influence personal future treatment')),
                ('donor_data_protection_informed', models.NullBooleanField(verbose_name='Donor informed about data protection')),
                ('donated_material_code', models.NullBooleanField(verbose_name='Donated material is coded')),
                ('donated_material_rendered_unidentifiable', models.NullBooleanField(verbose_name='Donated material has been rendered unidentifiable')),
                ('donor_identity_protected_rare_disease', models.CharField(blank=True, max_length=10, null=True, verbose_name='Donor identity protected', choices=[(b'yes', b'Yes'), (b'no', b'No'), (b'unknown', b'Unknown')])),
                ('genetic_information_exists', models.NullBooleanField(verbose_name='Is there genetic information associated with the cell line')),
                ('genetic_information_access_policy', models.CharField(blank=True, max_length=50, null=True, verbose_name='Access policy for genetic information derived from the cell line', choices=[(b'open_access', b'Open access'), (b'controlled_access', b'Controlled access'), (b'no_information', b'No information')])),
                ('genetic_information_available', models.NullBooleanField(verbose_name='Is genetic information associated with the cell line available')),
                ('consent_permits_access_medical_records', models.NullBooleanField(verbose_name='Consent permits access to medical records')),
                ('consent_permits_access_other_clinical_source', models.NullBooleanField(verbose_name='Consent permits access to other clinical sources')),
                ('medical_records_access_consented', models.NullBooleanField(verbose_name='Access to ongoing medical records has been consented')),
                ('medical_records_access_consented_organisation_name', models.TextField(null=True, verbose_name='Organisation holding medical records', blank=True)),
                ('consent_permits_stop_of_derived_material_use', models.NullBooleanField(verbose_name='Consent permits stopping the use of derived material')),
                ('consent_permits_stop_of_delivery_of_information_and_data', models.NullBooleanField(verbose_name='Consent permits stopping delivery or use of information and data about donor')),
                ('authority_approval', models.NullBooleanField(verbose_name='Institutional review board/competent authority approval')),
                ('approval_authority_name', models.TextField(null=True, verbose_name='Name of accrediting authority', blank=True)),
                ('approval_number', models.CharField(max_length=100, null=True, verbose_name='Approval number', blank=True)),
                ('ethics_review_panel_opinion_relation_consent_form', models.NullBooleanField(verbose_name='Ethics review panel provided a favourable opinion in relation of the form of consent')),
                ('ethics_review_panel_opinion_project_proposed_use', models.NullBooleanField(verbose_name='Ethics review panel provided a favourable opinion in relation to the project')),
                ('recombined_dna_vectors_supplier', models.TextField(null=True, verbose_name='Recombined DNA vectors supplier', blank=True)),
                ('use_or_distribution_constraints', models.NullBooleanField(verbose_name='Any use or distribution constraints')),
                ('use_or_distribution_constraints_desc', models.TextField(null=True, verbose_name='Use or distribution constraints', blank=True)),
                ('third_party_obligations', models.NullBooleanField(verbose_name='Any third party obligations')),
                ('third_party_obligations_desc', models.TextField(null=True, verbose_name='Third party obligations', blank=True)),
                ('cell_line', models.OneToOneField(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Cell line ethics',
                'verbose_name_plural': 'Cell line ethics',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CelllineGeneticModification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('protocol', models.FileField(upload_to=ebisc.celllines.models.upload_to, null=True, verbose_name='Protocol', blank=True)),
                ('cell_line', models.OneToOneField(related_name='genetic_modification', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line genetic modification',
                'verbose_name_plural': 'Cell line genetic modifications',
            },
        ),
        migrations.CreateModel(
            name='CelllineGenomeAnalysis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.CharField(max_length=100, null=True, verbose_name='Data', blank=True)),
                ('link', models.URLField(null=True, verbose_name='Link', blank=True)),
                ('cell_line', models.OneToOneField(related_name='genome_analysis', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line genome analysis',
                'verbose_name_plural': 'Cell line genome analysis',
            },
        ),
        migrations.CreateModel(
            name='CelllineGenotypingRsNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rs_number', models.CharField(max_length=12, null=True, verbose_name='rs Number', blank=True)),
                ('link', models.URLField(null=True, verbose_name='Link', blank=True)),
                ('disease_genotype', models.ForeignKey(related_name='rs_number', verbose_name='Cell line disease genotype', blank=True, to='celllines.CelllineDiseaseGenotype', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line rs number',
                'verbose_name_plural': 'Cell line rs numbers',
            },
        ),
        migrations.CreateModel(
            name='CelllineGenotypingSNP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene_name', models.CharField(max_length=45, null=True, verbose_name='SNP gene name', blank=True)),
                ('chromosomal_position', models.CharField(max_length=45, null=True, verbose_name='SNP choromosomal position', blank=True)),
                ('disease_genotype', models.ForeignKey(related_name='snps', verbose_name='Cell line disease genotype', blank=True, to='celllines.CelllineDiseaseGenotype', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line snp',
                'verbose_name_plural': 'Cell line snps',
            },
        ),
        migrations.CreateModel(
            name='CelllineHlaTyping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hla_class', models.CharField(max_length=10, null=True, verbose_name='HLA class', blank=True)),
                ('hla', models.CharField(max_length=10, null=True, verbose_name='HLA', blank=True)),
                ('hla_allele_1', models.CharField(max_length=45, null=True, verbose_name='Cell line HLA allele 1', blank=True)),
                ('hla_allele_2', models.CharField(max_length=45, null=True, verbose_name='Cell line HLA allele 2', blank=True)),
                ('cell_line', models.ForeignKey(related_name='hla_typing', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line HLA typing',
                'verbose_name_plural': 'Cell line HLA typing',
            },
        ),
        migrations.CreateModel(
            name='CelllineIntegratingVector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('excisable', models.NullBooleanField(default=None, verbose_name='Excisable')),
                ('absence_reprogramming_vectors', models.NullBooleanField(default=None, verbose_name='Absence of reprogramming vector(s)')),
                ('cell_line', models.OneToOneField(related_name='integrating_vector', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Cell line integrating vector',
                'verbose_name_plural': 'Cell line integrating vectors',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CelllineKaryotype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('karyotype', models.CharField(max_length=500, null=True, verbose_name='Karyotype', blank=True)),
                ('karyotype_method', models.CharField(max_length=100, null=True, verbose_name='Karyotype method', blank=True)),
                ('passage_number', models.CharField(max_length=10, null=True, verbose_name='Passage number', blank=True)),
                ('cell_line', models.OneToOneField(related_name='karyotype', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line karyotype',
                'verbose_name_plural': 'Cell line karyotypes',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CellLineMarker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_line', models.ForeignKey(verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line marker',
                'verbose_name_plural': 'Cell line markers',
            },
        ),
        migrations.CreateModel(
            name='CelllineNonIntegratingVector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_line', models.OneToOneField(related_name='non_integrating_vector', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Cell line non integrating vector',
                'verbose_name_plural': 'Cell line non integrating vectors',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CelllineOrganization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_line', models.ForeignKey(related_name='organizations', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line organization',
                'verbose_name_plural': 'Cell line organizations',
            },
        ),
        migrations.CreateModel(
            name='CelllineOrgType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_line_org_type', models.CharField(max_length=45, verbose_name='Cell line organization type', blank=True)),
            ],
            options={
                'ordering': ['cell_line_org_type'],
                'verbose_name': 'Cell line org type',
                'verbose_name_plural': 'Cell line org types',
            },
        ),
        migrations.CreateModel(
            name='CelllinePublication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference_type', models.CharField(max_length=100, verbose_name='Type', choices=[(b'pubmed', b'PubMed')])),
                ('reference_id', models.CharField(max_length=100, null=True, verbose_name='ID', blank=True)),
                ('reference_url', models.URLField(verbose_name='URL')),
                ('reference_title', models.CharField(max_length=500, verbose_name='Title')),
                ('cell_line', models.ForeignKey(related_name='publications', verbose_name='Cell line', blank=True, to='celllines.Cellline', null=True)),
            ],
            options={
                'ordering': ('reference_title',),
                'verbose_name': 'Cell line publication',
                'verbose_name_plural': 'Cell line publications',
            },
        ),
        migrations.CreateModel(
            name='CelllineStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(unique=True, max_length=50, verbose_name='Cell line status')),
            ],
            options={
                'ordering': ['status'],
                'verbose_name': 'Cell line status',
                'verbose_name_plural': 'Cell line statuses',
            },
        ),
        migrations.CreateModel(
            name='CelllineStrFingerprinting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locus', models.CharField(max_length=45, null=True, verbose_name='Locus', blank=True)),
                ('allele1', models.CharField(max_length=45, null=True, verbose_name='Allele 1', blank=True)),
                ('allele2', models.CharField(max_length=45, null=True, verbose_name='Allele 2', blank=True)),
                ('cell_line', models.ForeignKey(related_name='str_fingerprinting', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line STR finger printing',
                'verbose_name_plural': 'Cell line STR finger printing',
            },
        ),
        migrations.CreateModel(
            name='CelllineValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('potential_use', models.CharField(max_length=100, verbose_name='Potential use', blank=True)),
                ('value_to_society', models.CharField(max_length=100, verbose_name='Value to society', blank=True)),
                ('value_to_research', models.CharField(max_length=100, verbose_name='Value to research', blank=True)),
                ('other_value', models.CharField(max_length=100, verbose_name='Other value', blank=True)),
                ('cell_line', models.OneToOneField(null=True, blank=True, to='celllines.Cellline', verbose_name='Cell line')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Cell line value',
                'verbose_name_plural': 'Cell line values',
            },
        ),
        migrations.CreateModel(
            name='CelllineVectorFreeReprogrammingFactors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_line', models.OneToOneField(related_name='vector_free_reprogramming_factors', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Cell line Vector-free Programming Factor',
                'verbose_name_plural': 'Cell line Vector-free Programming Factors',
            },
        ),
        migrations.CreateModel(
            name='CellType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Cell type')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Cell type',
                'verbose_name_plural': 'Cell types',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state_county', models.IntegerField(null=True, verbose_name='State county', blank=True)),
                ('city', models.CharField(max_length=45, verbose_name='City', blank=True)),
                ('street', models.CharField(max_length=45, verbose_name='Street', blank=True)),
                ('building_number', models.CharField(max_length=20, verbose_name='Building number', blank=True)),
                ('suite_or_apt_or_dept', models.CharField(max_length=10, null=True, verbose_name='Suite or apt or dept', blank=True)),
                ('office_phone', models.CharField(max_length=20, null=True, verbose_name='Office phone', blank=True)),
                ('fax', models.CharField(max_length=20, null=True, verbose_name='Fax', blank=True)),
                ('mobile_phone', models.CharField(max_length=20, null=True, verbose_name='Mobile phone', blank=True)),
                ('website', models.CharField(max_length=45, null=True, verbose_name='Website', blank=True)),
                ('email_address', models.CharField(max_length=45, null=True, verbose_name='Email address', blank=True)),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_type', models.CharField(max_length=45, verbose_name='Contact type', blank=True)),
            ],
            options={
                'ordering': ['contact_type'],
                'verbose_name': 'Contact type',
                'verbose_name_plural': 'Contact types',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='Country')),
                ('code', models.CharField(max_length=3, unique=True, null=True, verbose_name='Country code', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='CultureMediumOther',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('base', models.CharField(max_length=45, verbose_name='Culture medium base', blank=True)),
                ('protein_source', models.CharField(max_length=45, null=True, verbose_name='Protein source', blank=True)),
                ('serum_concentration', models.IntegerField(null=True, verbose_name='Serum concentration', blank=True)),
                ('cell_line_culture_conditions', models.OneToOneField(related_name='culture_medium_other', verbose_name='Cell line culture conditions', to='celllines.CelllineCultureConditions')),
            ],
            options={
                'ordering': ['base', 'protein_source', 'serum_concentration'],
                'verbose_name': 'Culture medium',
                'verbose_name_plural': 'Culture mediums',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icdcode', models.CharField(max_length=30, unique=True, null=True, verbose_name='DOID', blank=True)),
                ('purl', models.URLField(max_length=300, unique=True, null=True, verbose_name='Purl', blank=True)),
                ('disease', models.CharField(max_length=45, verbose_name='Disease', blank=True)),
                ('synonyms', models.CharField(max_length=500, null=True, verbose_name='Synonyms', blank=True)),
            ],
            options={
                'ordering': ['disease'],
                'verbose_name': 'Disease',
                'verbose_name_plural': 'Diseases',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_line', models.IntegerField(null=True, verbose_name='Cell line', blank=True)),
                ('title', models.CharField(max_length=45, verbose_name='Title', blank=True)),
                ('abstract', models.TextField(null=True, verbose_name='Abstract', blank=True)),
                ('depositor', models.IntegerField(null=True, verbose_name='Document depositor', blank=True)),
                ('authors', models.TextField(null=True, verbose_name='Authors', blank=True)),
                ('owner', models.IntegerField(null=True, verbose_name='Owner', blank=True)),
                ('version', models.CharField(max_length=5, verbose_name='Version', blank=True)),
                ('access_level', models.IntegerField(null=True, verbose_name='Access level', blank=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document_type', models.CharField(max_length=30, verbose_name='Document type', blank=True)),
            ],
            options={
                'ordering': ['document_type'],
                'verbose_name': 'Document type',
                'verbose_name_plural': 'Document types',
            },
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('biosamples_id', models.CharField(unique=True, max_length=12, verbose_name='Biosamples ID')),
                ('provider_donor_ids', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), null=True, verbose_name='Provider donor ids', size=None)),
                ('ethnicity', models.CharField(max_length=100, null=True, verbose_name='Ethnicity', blank=True)),
                ('phenotypes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, verbose_name='Phenotypes', size=None)),
                ('karyotype', models.CharField(max_length=500, null=True, verbose_name='Karyotype', blank=True)),
                ('country_of_origin', models.ForeignKey(verbose_name='Country of origin', blank=True, to='celllines.Country', null=True)),
            ],
            options={
                'ordering': ['biosamples_id'],
                'verbose_name': 'Donor',
                'verbose_name_plural': 'Donors',
            },
        ),
        migrations.CreateModel(
            name='DonorGenotype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allele_carried', models.CharField(max_length=12, null=True, verbose_name='Allele carried through', blank=True)),
                ('homozygous_heterozygous', models.CharField(max_length=12, null=True, verbose_name='Is the donor homozygous or heterozygous for this variant', blank=True)),
                ('assembly', models.CharField(max_length=45, null=True, verbose_name='Assembly', blank=True)),
                ('chormosome', models.CharField(max_length=45, null=True, verbose_name='Chormosome', blank=True)),
                ('coordinate', models.CharField(max_length=45, null=True, verbose_name='Coordinate', blank=True)),
                ('reference_allele', models.CharField(max_length=45, null=True, verbose_name='Reference allele', blank=True)),
                ('alternative_allele', models.CharField(max_length=45, null=True, verbose_name='Alternative allele', blank=True)),
                ('protein_sequence_variants', models.CharField(max_length=100, null=True, verbose_name='Protein sequence variants', blank=True)),
                ('donor', models.OneToOneField(related_name='donor_genotyping', verbose_name='Donor', to='celllines.Donor')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Donor Genotyping',
                'verbose_name_plural': 'Donor Genotyping',
            },
        ),
        migrations.CreateModel(
            name='DonorGenotypingRsNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rs_number', models.CharField(max_length=12, verbose_name='rs Number')),
                ('link', models.URLField(null=True, verbose_name='Link', blank=True)),
                ('donor_genotype', models.ForeignKey(related_name='donor_rs_number', verbose_name='Donor Genotype', to='celllines.DonorGenotype')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Donor rs number',
                'verbose_name_plural': 'Donor rs numbers',
            },
        ),
        migrations.CreateModel(
            name='DonorGenotypingSNP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene_name', models.CharField(max_length=45, verbose_name='SNP gene name')),
                ('chromosomal_position', models.CharField(max_length=45, null=True, verbose_name='SNP choromosomal position', blank=True)),
                ('donor_genotype', models.ForeignKey(related_name='donor_snps', verbose_name='Donor Genotype', to='celllines.DonorGenotype')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Donor snp',
                'verbose_name_plural': 'Donor snps',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10, verbose_name='Gender')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
            },
        ),
        migrations.CreateModel(
            name='GeneticModificationGeneKnockIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivery_method', models.CharField(max_length=45, null=True, verbose_name='Delivery method', blank=True)),
                ('cell_line', models.OneToOneField(related_name='genetic_modification_gene_knock_in', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Genetic modification - Gene knock-in',
                'verbose_name_plural': 'Genetic modifications - Gene knock-in',
            },
        ),
        migrations.CreateModel(
            name='GeneticModificationGeneKnockOut',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivery_method', models.CharField(max_length=45, null=True, verbose_name='Delivery method', blank=True)),
                ('cell_line', models.OneToOneField(related_name='genetic_modification_gene_knock_out', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Genetic modification - Gene knock-out',
                'verbose_name_plural': 'Genetic modifications - Gene knock-out',
            },
        ),
        migrations.CreateModel(
            name='GeneticModificationIsogenic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('change_type', models.CharField(max_length=45, null=True, verbose_name='Type of change', blank=True)),
                ('modified_sequence', models.CharField(max_length=100, null=True, verbose_name='Modified sequence', blank=True)),
                ('cell_line', models.OneToOneField(related_name='genetic_modification_isogenic', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Genetic modification - Isogenic modification',
                'verbose_name_plural': 'Genetic modifications - Isogenic modification',
            },
        ),
        migrations.CreateModel(
            name='GeneticModificationTransgeneExpression',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivery_method', models.CharField(max_length=45, null=True, verbose_name='Delivery method', blank=True)),
                ('cell_line', models.OneToOneField(related_name='genetic_modification_transgene_expression', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Genetic modification - Transgene Expression',
                'verbose_name_plural': 'Genetic modifications - Transgene Expression',
            },
        ),
        migrations.CreateModel(
            name='Germlayer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('germlayer', models.CharField(max_length=15, verbose_name='Germ layer', blank=True)),
            ],
            options={
                'ordering': ['germlayer'],
                'verbose_name': 'Germ layer',
                'verbose_name_plural': 'Germ layers',
            },
        ),
        migrations.CreateModel(
            name='IntegratingVector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Integrating vector')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Integrating vector',
                'verbose_name_plural': 'Integrating vectors',
            },
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Marker', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Marker',
                'verbose_name_plural': 'Markers',
            },
        ),
        migrations.CreateModel(
            name='Molecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('kind', models.CharField(max_length=20, verbose_name='Kind', choices=[(b'gene', 'Gene'), (b'protein', 'Protein')])),
            ],
            options={
                'ordering': ['name', 'kind'],
                'verbose_name': 'Molecule',
                'verbose_name_plural': 'Molecules',
            },
        ),
        migrations.CreateModel(
            name='MoleculeReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catalog', models.CharField(max_length=20, verbose_name='Molecule ID source', choices=[(b'entrez', 'Entrez'), (b'ensembl', 'Ensembl')])),
                ('catalog_id', models.CharField(max_length=20, verbose_name='ID')),
                ('molecule', models.ForeignKey(verbose_name=b'Molecule', to='celllines.Molecule')),
            ],
            options={
                'ordering': ['molecule', 'catalog'],
                'verbose_name': 'Molecule reference',
                'verbose_name_plural': 'Molecule references',
            },
        ),
        migrations.CreateModel(
            name='Morphologymethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('morphologymethod', models.CharField(max_length=45, verbose_name='Morphology method', blank=True)),
            ],
            options={
                'ordering': ['morphologymethod'],
                'verbose_name': 'Morphology method',
                'verbose_name_plural': 'Morphology methods',
            },
        ),
        migrations.CreateModel(
            name='NonIntegratingVector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Non-integrating vector')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Non-integrating vector',
                'verbose_name_plural': 'Non-integrating vectors',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, unique=True, null=True, verbose_name='Organization name', blank=True)),
                ('short_name', models.CharField(max_length=6, unique=True, null=True, verbose_name='Organization short name', blank=True)),
                ('contact', models.ForeignKey(verbose_name='Contact', blank=True, to='celllines.Contact', null=True)),
            ],
            options={
                'ordering': ['name', 'short_name'],
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
        ),
        migrations.CreateModel(
            name='OrgType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('org_type', models.CharField(max_length=45, verbose_name='Organization type', blank=True)),
            ],
            options={
                'ordering': ['org_type'],
                'verbose_name': 'Organization type',
                'verbose_name_plural': 'Organization types',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization', models.IntegerField(null=True, verbose_name='Organization', blank=True)),
                ('last_name', models.CharField(max_length=20, verbose_name='Person last name', blank=True)),
                ('first_name', models.CharField(max_length=45, verbose_name='Person first name', blank=True)),
                ('contact', models.ForeignKey(verbose_name='Contact', blank=True, to='celllines.Contact', null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.CreateModel(
            name='PhoneCountryCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phonecountrycode', models.DecimalField(null=True, verbose_name='Phone country code', max_digits=4, decimal_places=0, blank=True)),
            ],
            options={
                'ordering': ['phonecountrycode'],
                'verbose_name': 'Phone country code',
                'verbose_name_plural': 'Phone country codes',
            },
        ),
        migrations.CreateModel(
            name='Postcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postcode', models.CharField(max_length=45, verbose_name='Postcode', blank=True)),
                ('district', models.CharField(max_length=20, verbose_name='District')),
            ],
            options={
                'ordering': ['postcode', 'district'],
                'verbose_name': 'Postcode',
                'verbose_name_plural': 'Postcodes',
            },
        ),
        migrations.CreateModel(
            name='Transposon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Transposon')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Transposon',
                'verbose_name_plural': 'Transposons',
            },
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerExpressionProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('method', models.CharField(max_length=100, null=True, verbose_name='Method', blank=True)),
                ('passage_number', models.CharField(max_length=10, null=True, verbose_name='Passage number', blank=True)),
                ('data_url', models.URLField(null=True, verbose_name='Data URL', blank=True)),
                ('uploaded_data_url', models.URLField(null=True, verbose_name='Uploaded data URL', blank=True)),
                ('cell_line', models.OneToOneField(related_name='undifferentiated_morphology_marker_expression_profile', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Markerd Undiff - Expression profile',
                'verbose_name_plural': 'Markerd Undiff - Expression profile',
            },
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerExpressionProfileMolecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('molecule', models.CharField(max_length=25, verbose_name='Molecule')),
                ('result', models.CharField(max_length=5, verbose_name='Result', choices=[(b'+', b'+'), (b'-', b'-'), (b'nd', b'n.d.')])),
                ('marker', models.ForeignKey(related_name='molecules', verbose_name='Marker', to='celllines.UndifferentiatedMorphologyMarkerExpressionProfile')),
            ],
            options={
                'ordering': ['molecule'],
                'abstract': False,
                'verbose_name': 'Marker molecule',
                'verbose_name_plural': 'Marker molecules',
            },
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerFacs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passage_number', models.CharField(max_length=10, null=True, verbose_name='Passage number', blank=True)),
                ('cell_line', models.OneToOneField(related_name='undifferentiated_morphology_marker_facs', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Markerd Undiff - Facs',
                'verbose_name_plural': 'Markerd Undiff - Facs',
            },
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerFacsMolecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('molecule', models.CharField(max_length=25, verbose_name='Molecule')),
                ('result', models.CharField(max_length=5, verbose_name='Result', choices=[(b'+', b'+'), (b'-', b'-'), (b'nd', b'n.d.')])),
                ('marker', models.ForeignKey(related_name='molecules', verbose_name='Marker', to='celllines.UndifferentiatedMorphologyMarkerFacs')),
            ],
            options={
                'ordering': ['molecule'],
                'abstract': False,
                'verbose_name': 'Marker molecule',
                'verbose_name_plural': 'Marker molecules',
            },
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerImune',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passage_number', models.CharField(max_length=10, null=True, verbose_name='Passage number', blank=True)),
                ('cell_line', models.OneToOneField(related_name='undifferentiated_morphology_marker_imune', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Markerd Undiff - Imune',
                'verbose_name_plural': 'Markerd Undiff - Imune',
            },
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerImuneMolecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('molecule', models.CharField(max_length=25, verbose_name='Molecule')),
                ('result', models.CharField(max_length=5, verbose_name='Result', choices=[(b'+', b'+'), (b'-', b'-'), (b'nd', b'n.d.')])),
                ('marker', models.ForeignKey(related_name='molecules', verbose_name='Marker', to='celllines.UndifferentiatedMorphologyMarkerImune')),
            ],
            options={
                'ordering': ['molecule'],
                'abstract': False,
                'verbose_name': 'Marker molecule',
                'verbose_name_plural': 'Marker molecules',
            },
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerMorphology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passage_number', models.CharField(max_length=10, null=True, verbose_name='Passage number', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('data_url', models.URLField(null=True, verbose_name='URL', blank=True)),
                ('cell_line', models.OneToOneField(related_name='undifferentiated_morphology_marker_morphology', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Markerd Undiff - Morphology',
                'verbose_name_plural': 'Markerd Undiff - Morphology',
            },
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerRtPcr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passage_number', models.CharField(max_length=10, null=True, verbose_name='Passage number', blank=True)),
                ('cell_line', models.OneToOneField(related_name='undifferentiated_morphology_marker_rtpcr', verbose_name='Cell line', to='celllines.Cellline')),
            ],
            options={
                'verbose_name': 'Markerd Undiff - RtPcr',
                'verbose_name_plural': 'Markerd Undiff - RtPcr',
            },
        ),
        migrations.CreateModel(
            name='UndifferentiatedMorphologyMarkerRtPcrMolecule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('molecule', models.CharField(max_length=25, verbose_name='Molecule')),
                ('result', models.CharField(max_length=5, verbose_name='Result', choices=[(b'+', b'+'), (b'-', b'-'), (b'nd', b'n.d.')])),
                ('marker', models.ForeignKey(related_name='molecules', verbose_name='Marker', to='celllines.UndifferentiatedMorphologyMarkerRtPcr')),
            ],
            options={
                'ordering': ['molecule'],
                'abstract': False,
                'verbose_name': 'Marker molecule',
                'verbose_name_plural': 'Marker molecules',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20, verbose_name='Units')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Units',
                'verbose_name_plural': 'Units',
            },
        ),
        migrations.CreateModel(
            name='VectorFreeReprogrammingFactor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vector_free_reprogramming_factor', models.CharField(max_length=15, verbose_name='Vector free reprogram factor', blank=True)),
                ('reference_id', models.CharField(max_length=45, verbose_name='Referenceid', blank=True)),
            ],
            options={
                'ordering': ['vector_free_reprogramming_factor'],
                'verbose_name': 'Vector free reprogram factor',
                'verbose_name_plural': 'Vector free reprogram factors',
            },
        ),
        migrations.CreateModel(
            name='Virus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Virus')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Virus',
                'verbose_name_plural': 'Viruses',
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='org_type',
            field=models.ForeignKey(verbose_name='Organization type', blank=True, to='celllines.OrgType', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='molecule',
            unique_together=set([('name', 'kind')]),
        ),
        migrations.AddField(
            model_name='geneticmodificationtransgeneexpression',
            name='genes',
            field=models.ManyToManyField(to='celllines.Molecule', blank=True),
        ),
        migrations.AddField(
            model_name='geneticmodificationtransgeneexpression',
            name='transposon',
            field=models.ForeignKey(verbose_name='Transposon', blank=True, to='celllines.Transposon', null=True),
        ),
        migrations.AddField(
            model_name='geneticmodificationtransgeneexpression',
            name='virus',
            field=models.ForeignKey(verbose_name='Virus', blank=True, to='celllines.Virus', null=True),
        ),
        migrations.AddField(
            model_name='geneticmodificationisogenic',
            name='target_locus',
            field=models.ManyToManyField(to='celllines.Molecule', blank=True),
        ),
        migrations.AddField(
            model_name='geneticmodificationgeneknockout',
            name='target_genes',
            field=models.ManyToManyField(to='celllines.Molecule', blank=True),
        ),
        migrations.AddField(
            model_name='geneticmodificationgeneknockout',
            name='transposon',
            field=models.ForeignKey(verbose_name='Transposon', blank=True, to='celllines.Transposon', null=True),
        ),
        migrations.AddField(
            model_name='geneticmodificationgeneknockout',
            name='virus',
            field=models.ForeignKey(verbose_name='Virus', blank=True, to='celllines.Virus', null=True),
        ),
        migrations.AddField(
            model_name='geneticmodificationgeneknockin',
            name='target_genes',
            field=models.ManyToManyField(related_name='target_genes', to='celllines.Molecule', blank=True),
        ),
        migrations.AddField(
            model_name='geneticmodificationgeneknockin',
            name='transgenes',
            field=models.ManyToManyField(related_name='transgenes', to='celllines.Molecule', blank=True),
        ),
        migrations.AddField(
            model_name='geneticmodificationgeneknockin',
            name='transposon',
            field=models.ForeignKey(verbose_name='Transposon', blank=True, to='celllines.Transposon', null=True),
        ),
        migrations.AddField(
            model_name='geneticmodificationgeneknockin',
            name='virus',
            field=models.ForeignKey(verbose_name='Virus', blank=True, to='celllines.Virus', null=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='gender',
            field=models.ForeignKey(verbose_name='Gender', blank=True, to='celllines.Gender', null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='document_type',
            field=models.ForeignKey(verbose_name='Document type', blank=True, to='celllines.DocumentType', null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_type',
            field=models.ForeignKey(verbose_name='Contact type', blank=True, to='celllines.ContactType', null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='country',
            field=models.ForeignKey(db_column=b'country', verbose_name='Country', to='celllines.Country'),
        ),
        migrations.AddField(
            model_name='contact',
            name='fax_country_code',
            field=models.ForeignKey(related_name='contacts_faxcountrycode', verbose_name='Phone country code', blank=True, to='celllines.PhoneCountryCode', null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='mobile_country_code',
            field=models.ForeignKey(related_name='contacts_mobilecountrycode', verbose_name='Phone country code', blank=True, to='celllines.PhoneCountryCode', null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='office_phone_country_code',
            field=models.ForeignKey(related_name='contacts_officephonecountrycode', verbose_name='Phone country code', blank=True, to='celllines.PhoneCountryCode', null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='postcode',
            field=models.ForeignKey(db_column=b'postcode', verbose_name='Postcode', to='celllines.Postcode'),
        ),
        migrations.AddField(
            model_name='celllinevectorfreereprogrammingfactors',
            name='factor',
            field=models.ForeignKey(verbose_name='Vector-free reprogramming factor', blank=True, to='celllines.VectorFreeReprogrammingFactor', null=True),
        ),
        migrations.AddField(
            model_name='celllineorganization',
            name='cell_line_org_type',
            field=models.ForeignKey(verbose_name='Cell line org type', to='celllines.CelllineOrgType'),
        ),
        migrations.AddField(
            model_name='celllineorganization',
            name='organization',
            field=models.ForeignKey(verbose_name='Organization', to='celllines.Organization'),
        ),
        migrations.AddField(
            model_name='celllinenonintegratingvector',
            name='genes',
            field=models.ManyToManyField(to='celllines.Molecule', blank=True),
        ),
        migrations.AddField(
            model_name='celllinenonintegratingvector',
            name='vector',
            field=models.ForeignKey(verbose_name='Non-integrating vector', blank=True, to='celllines.NonIntegratingVector', null=True),
        ),
        migrations.AddField(
            model_name='celllinemarker',
            name='marker',
            field=models.ForeignKey(verbose_name='Marker', blank=True, to='celllines.Marker', null=True),
        ),
        migrations.AddField(
            model_name='celllinemarker',
            name='morphology_method',
            field=models.ForeignKey(verbose_name='Morphology method', blank=True, to='celllines.Morphologymethod', null=True),
        ),
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='genes',
            field=models.ManyToManyField(to='celllines.Molecule', blank=True),
        ),
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='transposon',
            field=models.ForeignKey(verbose_name='Transposon', blank=True, to='celllines.Transposon', null=True),
        ),
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='vector',
            field=models.ForeignKey(verbose_name='Integrating vector', blank=True, to='celllines.IntegratingVector', null=True),
        ),
        migrations.AddField(
            model_name='celllineintegratingvector',
            name='virus',
            field=models.ForeignKey(verbose_name='Virus', blank=True, to='celllines.Virus', null=True),
        ),
        migrations.AddField(
            model_name='celllinedifferentiationpotencymolecule',
            name='molecule',
            field=models.ForeignKey(verbose_name='Molecule', blank=True, to='celllines.Molecule', null=True),
        ),
        migrations.AddField(
            model_name='celllinedifferentiationpotencymarker',
            name='morphology_method',
            field=models.ForeignKey(verbose_name='Morphology method', blank=True, to='celllines.Morphologymethod', null=True),
        ),
        migrations.AddField(
            model_name='celllinedifferentiationpotency',
            name='germ_layer',
            field=models.ForeignKey(verbose_name='Germ layer', blank=True, to='celllines.Germlayer', null=True),
        ),
        migrations.AddField(
            model_name='celllinederivation',
            name='primary_cell_type',
            field=models.ForeignKey(verbose_name='Primary cell type', blank=True, to='celllines.CellType', null=True),
        ),
        migrations.AddField(
            model_name='celllineculturemediumsupplement',
            name='unit',
            field=models.ForeignKey(verbose_name='Unit', blank=True, to='celllines.Unit', null=True),
        ),
        migrations.AddField(
            model_name='celllinealiquot',
            name='batch',
            field=models.ForeignKey(related_name='aliquots', verbose_name='Cell line', to='celllines.CelllineBatch'),
        ),
        migrations.AddField(
            model_name='celllinealiquot',
            name='derived_from_aliqot',
            field=models.ForeignKey(verbose_name='Derived from aliquot', blank=True, to='celllines.CelllineAliquot', null=True),
        ),
        migrations.AddField(
            model_name='cellline',
            name='derivation_country',
            field=models.ForeignKey(verbose_name='Derivation country', blank=True, to='celllines.Country', null=True),
        ),
        migrations.AddField(
            model_name='cellline',
            name='donor',
            field=models.ForeignKey(verbose_name='Donor', blank=True, to='celllines.Donor', null=True),
        ),
        migrations.AddField(
            model_name='cellline',
            name='donor_age',
            field=models.ForeignKey(verbose_name='Age', blank=True, to='celllines.AgeRange', null=True),
        ),
        migrations.AddField(
            model_name='cellline',
            name='generator',
            field=models.ForeignKey(related_name='generator_of_cell_lines', verbose_name='Generator', to='celllines.Organization'),
        ),
        migrations.AddField(
            model_name='cellline',
            name='owner',
            field=models.ForeignKey(related_name='owner_of_cell_lines', verbose_name='Owner', blank=True, to='celllines.Organization', null=True),
        ),
        migrations.AddField(
            model_name='cellline',
            name='primary_disease',
            field=models.ForeignKey(verbose_name='Diagnosed disease', blank=True, to='celllines.Disease', null=True),
        ),
        migrations.AddField(
            model_name='cellline',
            name='status',
            field=models.ForeignKey(verbose_name='Cell line status', blank=True, to='celllines.CelllineStatus', null=True),
        ),
        migrations.AddField(
            model_name='batchcultureconditions',
            name='batch',
            field=models.OneToOneField(verbose_name='Batch', to='celllines.CelllineBatch'),
        ),
        migrations.AlterUniqueTogether(
            name='moleculereference',
            unique_together=set([('molecule', 'catalog')]),
        ),
        migrations.AlterUniqueTogether(
            name='celllinepublication',
            unique_together=set([('cell_line', 'reference_url')]),
        ),
        migrations.AlterUniqueTogether(
            name='celllineorganization',
            unique_together=set([('cell_line', 'organization', 'cell_line_org_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='celllinebatch',
            unique_together=set([('cell_line', 'batch_id')]),
        ),
    ]
