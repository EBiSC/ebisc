# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0007_remove_cellline_celllineecaccurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celllinelegal',
            name='applicable_legislation_and_regulation',
        ),
        migrations.RemoveField(
            model_name='celllinelegal',
            name='approved_use',
        ),
        migrations.RemoveField(
            model_name='celllinelegal',
            name='donor_trace',
        ),
        migrations.RemoveField(
            model_name='celllinelegal',
            name='informed_consent_reference',
        ),
        migrations.RemoveField(
            model_name='celllinelegal',
            name='ip_restrictions',
        ),
        migrations.RemoveField(
            model_name='celllinelegal',
            name='irb_approval',
        ),
        migrations.RemoveField(
            model_name='celllinelegal',
            name='jurisdiction',
        ),
        migrations.RemoveField(
            model_name='celllinelegal',
            name='managed_access',
        ),
        migrations.RemoveField(
            model_name='celllinelegal',
            name='restrictions',
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='approval_authority_name',
            field=models.TextField(null=True, verbose_name='Name of accrediting authority', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='approval_number',
            field=models.CharField(max_length=100, null=True, verbose_name='Approval number', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='authority_approval',
            field=models.NullBooleanField(verbose_name='Institutional review board/competent authority approval'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_anticipates_donor_notification_research_results',
            field=models.NullBooleanField(verbose_name='Consent anticipates the donor will be notified of results of research involving the donated samples or derived cells'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_expressly_permits_indefinite_storage',
            field=models.NullBooleanField(verbose_name='Consent expressly permits indefinite storage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_expressly_prevents_commercial_development',
            field=models.NullBooleanField(verbose_name='Consent expressly prevents commercial development'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_expressly_prevents_financial_gain',
            field=models.NullBooleanField(verbose_name='Consent expressly prevents financial gain'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_permits_access_medical_records',
            field=models.NullBooleanField(verbose_name='Consent permits access to medical records'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_permits_access_other_clinical_source',
            field=models.NullBooleanField(verbose_name='Consent permits access to other clinical sources'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_permits_clinical_treatment',
            field=models.NullBooleanField(verbose_name='Consent permits uses for clinical treatment or human applications'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_permits_development_of_commercial_products',
            field=models.NullBooleanField(verbose_name='Consent permits development of commercial products'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_permits_future_research',
            field=models.NullBooleanField(verbose_name='Consent permits unforeseen future research'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_permits_genetic_testing',
            field=models.NullBooleanField(verbose_name='Consent permits genetic testing'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_permits_ips_derivation',
            field=models.NullBooleanField(verbose_name='Consent expressly permits derivation of iPS cells'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_permits_research_by_academic_institution',
            field=models.NullBooleanField(verbose_name='Consent permits research by academic institution'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_permits_research_by_for_profit_company',
            field=models.NullBooleanField(verbose_name='Consent permits research by for-profit company'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_permits_research_by_non_profit_company',
            field=models.NullBooleanField(verbose_name='Consent permits research by non-profit company'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_permits_research_by_org',
            field=models.NullBooleanField(verbose_name='Consent permits research by public organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_permits_stop_of_delivery_of_information_and_data',
            field=models.NullBooleanField(verbose_name='Consent permits stopping delivery or use of information and data about donor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_permits_stop_of_derived_material_use',
            field=models.NullBooleanField(verbose_name='Consent permits stopping the use of derived material'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_permits_testing_microbiological_agents_pathogens',
            field=models.NullBooleanField(verbose_name='Consent permits testing for microbiological agents pathogens'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_pertains_specific_research_project',
            field=models.NullBooleanField(verbose_name='Consent pertains to one specific research project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='consent_prevents_availiability_to_worldwide_research',
            field=models.NullBooleanField(verbose_name='Consent prevents availiability to worldwide research'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='copy_of_consent_form_obtainable',
            field=models.NullBooleanField(verbose_name='Is copy of consent form obtainable'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='copy_of_donor_consent_form_english_obtainable',
            field=models.NullBooleanField(verbose_name='Is copy of consent form obtainable in English'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='copy_of_donor_consent_form_english_url',
            field=models.URLField(null=True, verbose_name='URL of donor consent form in English', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='copy_of_donor_consent_information_english_obtainable',
            field=models.NullBooleanField(verbose_name='Is copy of consent information obtainable in English'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='copy_of_donor_consent_information_english_url',
            field=models.URLField(null=True, verbose_name='URL of donor consent information in English', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='derived_information_influence_personal_future_treatment',
            field=models.NullBooleanField(verbose_name='Derived information may influence personal future treatment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='donated_material_code',
            field=models.NullBooleanField(verbose_name='Donated material is coded'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='donated_material_rendered_unidentifiable',
            field=models.NullBooleanField(verbose_name='Donated material has been rendered unidentifiable'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='donor_consent_form',
            field=models.NullBooleanField(verbose_name='Copy of consent form'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='donor_consent_form_url',
            field=models.URLField(null=True, verbose_name='URL of donor consent form', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='donor_data_protection_informed',
            field=models.NullBooleanField(verbose_name='Donor informed about data protection'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='donor_expects_notification_health_implications',
            field=models.NullBooleanField(verbose_name='Donor expects to be informed if, during use of donated material, something with significant health implications for the donor is discovered'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='donor_identity_protected_rare_disease',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Donor identity protected', choices=[(b'yes', b'Yes'), (b'no', b'No'), (b'unknown', b'Unknown')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='donor_recontact_agreement',
            field=models.NullBooleanField(verbose_name='Has the donor agreed to be recontacted'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='ethics_review_panel_opinion_project_proposed_use',
            field=models.NullBooleanField(verbose_name='Ethics review panel provided a favourable opinion in relation to the project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='ethics_review_panel_opinion_relation_consent_form',
            field=models.NullBooleanField(verbose_name='Ethics review panel provided a favourable opinion in relation of the form of consent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='formal_permission_for_distribution',
            field=models.NullBooleanField(verbose_name='Formal permission from the owner for distribution'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='further_constraints_on_use',
            field=models.NullBooleanField(verbose_name='Any further constraints on use'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='further_constraints_on_use_desc',
            field=models.TextField(null=True, verbose_name='Further constraints on use', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='future_research_permitted_areas',
            field=models.TextField(null=True, verbose_name='Future research permitted areas or types', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='future_research_permitted_specified_areas',
            field=models.NullBooleanField(verbose_name='Future research is permitted only in relation to specified areas or types of research'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='genetic_information_access_policy',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Access policy for genetic information derived from the cell line', choices=[(b'open_access', b'Open access'), (b'controlled_access', b'Controlled access'), (b'no_information', b'No information')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='genetic_information_available',
            field=models.NullBooleanField(verbose_name='Is genetic information associated with the cell line available'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='genetic_information_exists',
            field=models.NullBooleanField(verbose_name='Is there genetic information associated with the cell line'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='known_location_of_consent_form',
            field=models.NullBooleanField(verbose_name='Do you know who holds the consent form'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='medical_records_access_consented',
            field=models.NullBooleanField(verbose_name='Access to ongoing medical records has been consented'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='medical_records_access_consented_organisation_name',
            field=models.TextField(null=True, verbose_name='Organisation holding medical records', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='no_inducement_statement',
            field=models.NullBooleanField(verbose_name='No inducement statement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='no_pressure_statement',
            field=models.NullBooleanField(verbose_name='No pressure statement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='obtain_new_consent_form',
            field=models.NullBooleanField(verbose_name='Is new form obtainable'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='recombined_dna_vectors_supplier',
            field=models.TextField(null=True, verbose_name='Recombined DNA vectors supplier', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='third_party_obligations',
            field=models.NullBooleanField(verbose_name='Any third party obligations'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='third_party_obligations_desc',
            field=models.TextField(null=True, verbose_name='Third party obligations', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='use_or_distribution_constraints',
            field=models.NullBooleanField(verbose_name='Any use or distribution constraints'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celllinelegal',
            name='use_or_distribution_constraints_desc',
            field=models.TextField(null=True, verbose_name='Use or distribution constraints', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celllinelegal',
            name='donor_consent',
            field=models.NullBooleanField(verbose_name='Donor consent'),
            preserve_default=True,
        ),
    ]
