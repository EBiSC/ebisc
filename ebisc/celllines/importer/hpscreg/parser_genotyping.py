import logging
logger = logging.getLogger('management.commands')

from .parser import inject_valuef, value_of_file

from ebisc.celllines.models import  \
    CelllineKaryotype,  \
    CelllineHlaTyping, \
    CelllineStrFingerprinting, \
    CelllineGenomeAnalysis, \
    CelllineGenomeAnalysisFile


# -----------------------------------------------------------------------------
# Genotyping

@inject_valuef
def parse_karyotyping(valuef, source, cell_line):

    if valuef('karyotyping_flag', 'bool'):
        if valuef('karyotyping_method') == 'Other' or valuef('karyotyping_method') == 'other':
            if valuef('karyotyping_method_other') is not None:
                karyotype_method = valuef('karyotyping_method_other')
            else:
                karyotype_method = u'Other'
        else:
            karyotype_method = valuef('karyotyping_method')

        if valuef('karyotyping_karyotype') or valuef('karyotyping_method') or valuef('karyotyping_number_passages') or valuef('karyotyping_image_upload_file_enc'):

            cell_line_karyotype, cell_line_karyotype_created = CelllineKaryotype.objects.get_or_create(cell_line=cell_line)

            cell_line_karyotype.karyotype = valuef('karyotyping_karyotype')
            cell_line_karyotype.karyotype_method = karyotype_method
            cell_line_karyotype.passage_number = valuef('karyotyping_number_passages')

            if cell_line_karyotype.karyotype_file_enc:
                karyotype_file_current_enc = cell_line_karyotype.karyotype_file_enc
            else:
                karyotype_file_current_enc = None

            # Save or upadate a file if it exists
            if valuef('karyotyping_image_upload_file_enc'):
                cell_line_karyotype.karyotype_file_enc = value_of_file(valuef('karyotyping_image_upload_file_enc'), valuef('karyotyping_image_upload_file'), cell_line_karyotype.karyotype_file, karyotype_file_current_enc)

            # Delete old file if it is no longer in the export
            elif cell_line_karyotype.karyotype_file_enc:
                logger.info('Deleting obsolete karyotyping file %s' % cell_line_karyotype.karyotype_file)
                cell_line_karyotype.karyotype_file.delete()
                cell_line_karyotype.karyotype_file_enc = None

            if cell_line_karyotype_created or cell_line_karyotype.is_dirty():
                if cell_line_karyotype_created:
                    logger.info('Added cell line karyotype: %s' % cell_line_karyotype)
                else:
                    logger.info('Updated cell line karyotype: %s' % cell_line_karyotype)

                cell_line_karyotype.save()

                return True

            return False


@inject_valuef
def parse_hla_typing(valuef, source, cell_line):

    if valuef('hla_flag', 'bool'):

        dirty = []

        if valuef('hla_i_a_all1') or valuef('hla_i_a_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='A')
            hla_typing.hla_class = 'I'
            hla_typing.hla_allele_1 = valuef('hla_i_a_all1')
            hla_typing.hla_allele_2 = valuef('hla_i_a_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]

        if valuef('hla_i_b_all1') or valuef('hla_i_b_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='B')
            hla_typing.hla_class = 'I'
            hla_typing.hla_allele_1 = valuef('hla_i_b_all1')
            hla_typing.hla_allele_2 = valuef('hla_i_b_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]

        if valuef('hla_i_c_all1') or valuef('hla_i_c_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='C')
            hla_typing.hla_class = 'I'
            hla_typing.hla_allele_1 = valuef('hla_i_c_all1')
            hla_typing.hla_allele_2 = valuef('hla_i_c_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]

        if valuef('hla_ii_dp_all1') or valuef('hla_ii_dp_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='DP')
            hla_typing.hla_class = 'II'
            hla_typing.hla_allele_1 = valuef('hla_ii_dp_all1')
            hla_typing.hla_allele_2 = valuef('hla_ii_dp_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]

        if valuef('hla_ii_dm_all1') or valuef('hla_ii_dm_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='DM')
            hla_typing.hla_class = 'II'
            hla_typing.hla_allele_1 = valuef('hla_ii_dm_all1')
            hla_typing.hla_allele_2 = valuef('hla_ii_dm_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]

        if valuef('hla_ii_doa_all1') or valuef('hla_ii_doa_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='DOA')
            hla_typing.hla_class = 'II'
            hla_typing.hla_allele_1 = valuef('hla_ii_doa_all1')
            hla_typing.hla_allele_2 = valuef('hla_ii_doa_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]

        if valuef('hla_ii_dq_all1') or valuef('hla_ii_dq_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='DQ')
            hla_typing.hla_class = 'II'
            hla_typing.hla_allele_1 = valuef('hla_ii_dq_all1')
            hla_typing.hla_allele_2 = valuef('hla_ii_dq_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]

        if valuef('hla_ii_dr_all1') or valuef('hla_ii_dr_all2'):
            hla_typing, hla_typing_created = CelllineHlaTyping.objects.get_or_create(cell_line=cell_line, hla='DR')
            hla_typing.hla_class = 'II'
            hla_typing.hla_allele_1 = valuef('hla_ii_dr_all1')
            hla_typing.hla_allele_2 = valuef('hla_ii_dr_all2')

            if hla_typing_created or hla_typing.is_dirty():
                hla_typing.save()
                dirty += [True]


@inject_valuef
def parse_str_fingerprinting(valuef, source, cell_line):

    if valuef('fingerprinting_flag', 'bool'):

        if valuef('fingerprinting') is None:
            return

        else:
            dirty = []

            for locus in valuef('fingerprinting'):
                (locus, allele1, allele2) = locus.split('###')

                str_fingerprinting, str_fingerprinting_created = CelllineStrFingerprinting.objects.get_or_create(cell_line=cell_line, locus=locus)

                str_fingerprinting.allele1 = allele1
                str_fingerprinting.allele2 = allele2

                if str_fingerprinting_created or str_fingerprinting.is_dirty():
                    str_fingerprinting.save()

                    dirty += [True]

            if True in dirty:
                logger.info('Modified cell STR/Fingerprinting')

                return True

            return False


# Genome analysis - Cell line
@inject_valuef
def parse_genome_analysis(valuef, source, cell_line):

    if valuef('genome_wide_analysis_flag'):

        cell_line_genome_analysis_old = list(cell_line.genome_analysis.all().order_by('id'))
        cell_line_genome_analysis_old_ids = set([d.id for d in cell_line_genome_analysis_old])

        # Parse new ones and save them

        cell_line_genome_analysis_new = []

        for analysis in source.get('genome_wide_analysis', []):
            cell_line_genome_analysis_new.append(parse_genome_analysis_item(analysis, cell_line))

        cell_line_genome_analysis_new_ids = set([a.id for a in cell_line_genome_analysis_new if a is not None])

        # Delete ones that are no longer in the export
        to_delete = cell_line_genome_analysis_old_ids - cell_line_genome_analysis_new_ids

        for genome_analysis in [ga for ga in cell_line_genome_analysis_old if ga.id in to_delete]:
            logger.info('Deleting obsolete genome analysis %s' % genome_analysis)
            genome_analysis.delete()


@inject_valuef
def parse_genome_analysis_item(valuef, source, cell_line):

    analysis_method = None

    if valuef('analysis_method'):
        if valuef('analysis_method') == 'Other':
            if valuef('analysis_method_other') is not None:
                analysis_method = valuef('analysis_method_other')
            else:
                analysis_method = u'Other'
        else:
            analysis_method = valuef('analysis_method')

        cell_line_genome_analysis, created = CelllineGenomeAnalysis.objects.update_or_create(
            cell_line=cell_line,
            analysis_method=analysis_method,
            defaults={
                'link': valuef('public_data_link'),
            }
        )

        genome_analysis_files_old = list(cell_line_genome_analysis.genome_analysis_files.all().order_by('id'))
        genome_analysis_files_old_encs = set([f.vcf_file_enc for f in genome_analysis_files_old])

        # Parse files and save them

        genome_analysis_files_new = []

        for f in source.get('uploads', []):
            genome_analysis_files_new.append(parse_genome_analysis_file(f, cell_line_genome_analysis))

        genome_analysis_files_new_encs = set(genome_analysis_files_new)

        # Delete existing files that are not present in new data

        to_delete = genome_analysis_files_old_encs - genome_analysis_files_new_encs

        for genome_analysis_file in [f for f in genome_analysis_files_old if f.vcf_file_enc in to_delete]:
            logger.info('Deleting obsolete genome analysis file %s' % genome_analysis_file)
            genome_analysis_file.vcf_file.delete()
            genome_analysis_file.delete()

        if created or cell_line_genome_analysis.is_dirty():
            if created:
                logger.info('Added cell line genome analysis')
            else:
                logger.info('Updated cell line genome analysis')

            cell_line_genome_analysis.save()

        return cell_line_genome_analysis

    else:
        return None


@inject_valuef
def parse_genome_analysis_file(valuef, source, genome_analysis):

    genome_analysis_file, created = CelllineGenomeAnalysisFile.objects.get_or_create(
        genome_analysis=genome_analysis,
        vcf_file_enc=valuef('filename_enc').split('.')[0]
    )

    genome_analysis_file.vcf_file_enc = value_of_file(valuef('url'), valuef('filename'), genome_analysis_file.vcf_file, genome_analysis_file.vcf_file_enc)

    genome_analysis_file.vcf_file_description = valuef('description')
    genome_analysis_file.save()

    return genome_analysis_file.vcf_file_enc
