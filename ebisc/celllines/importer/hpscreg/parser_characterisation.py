import logging
logger = logging.getLogger('management.commands')

from .parser import inject_valuef, value_of_file

from ebisc.celllines.models import \
    CelllineCharacterization, \
    CelllineCharacterizationMarkerExpression, \
    CelllineCharacterizationMarkerExpressionMethod, \
    CelllineCharacterizationMarkerExpressionMethodFile, \
    CelllineCharacterizationPluritest, \
    CelllineCharacterizationPluritestFile, \
    CelllineCharacterizationEpipluriscore, \
    CelllineCharacterizationEpipluriscoreFile, \
    CelllineCharacterizationUndifferentiatedMorphologyFile, \
    CelllineCharacterizationHpscScorecard, \
    CelllineCharacterizationHpscScorecardReport, \
    CelllineCharacterizationHpscScorecardScorecard, \
    CelllineCharacterizationRNASequencing, \
    CelllineCharacterizationGeneExpressionArray, \
    CelllineCharacterizationDifferentiationPotency, \
    CelllineCharacterizationDifferentiationPotencyCellType, \
    CelllineCharacterizationDifferentiationPotencyCellTypeMarker, \
    CelllineCharacterizationDifferentiationPotencyMorphologyFile, \
    CelllineCharacterizationDifferentiationPotencyProtocolFile


# -----------------------------------------------------------------------------

# Microbiology/Virology Screening
@inject_valuef
def parse_characterization(valuef, source, cell_line):

    cell_line_characterization, created = CelllineCharacterization.objects.get_or_create(cell_line=cell_line)

    certificate_of_analysis_flag = valuef('certificate_of_analysis_flag', 'nullbool')
    certificate_of_analysis_passage_number = valuef('certificate_of_analysis_passage_number')

    virology_screening_flag = valuef('virology_screening_flag', 'nullbool')
    screening_hiv1 = valuef('virology_screening_hiv_1_result')
    screening_hiv2 = valuef('virology_screening_hiv_2_result')
    screening_hepatitis_b = valuef('virology_screening_hbv_result')
    screening_hepatitis_c = valuef('virology_screening_hcv_result')
    screening_mycoplasma = valuef('virology_screening_mycoplasma_result')

    if len([x for x in (certificate_of_analysis_flag, certificate_of_analysis_passage_number, virology_screening_flag, screening_hiv1, screening_hiv2, screening_hepatitis_b, screening_hepatitis_c, screening_mycoplasma) if x is not None]):
        cell_line_characterization.certificate_of_analysis_flag = certificate_of_analysis_flag
        cell_line_characterization.certificate_of_analysis_passage_number = certificate_of_analysis_passage_number
        cell_line_characterization.virology_screening_flag = virology_screening_flag
        cell_line_characterization.screening_hiv1 = screening_hiv1
        cell_line_characterization.screening_hiv2 = screening_hiv2
        cell_line_characterization.screening_hepatitis_b = screening_hepatitis_b
        cell_line_characterization.screening_hepatitis_c = screening_hepatitis_c
        cell_line_characterization.screening_mycoplasma = screening_mycoplasma

    if created or cell_line_characterization.is_dirty():
        if created:
            logger.info('Added cell line characterization: %s' % cell_line_characterization)
        else:
            logger.info('Updated cell line characterization: %s' % cell_line_characterization)

        cell_line_characterization.save()

        return True

    return False


# Pluritest
@inject_valuef
def parse_characterization_pluritest(valuef, source, cell_line):

    if valuef('characterisation_pluritest_flag'):
        cell_line_characterization_pluritest, created = CelllineCharacterizationPluritest.objects.get_or_create(cell_line=cell_line)

        cell_line_characterization_pluritest.pluritest_flag = valuef('characterisation_pluritest_flag', 'nullbool')
        cell_line_characterization_pluritest.pluripotency_score = valuef(['characterisation_pluritest_data', 'pluripotency_score'])
        cell_line_characterization_pluritest.novelty_score = valuef(['characterisation_pluritest_data', 'novelty_score'])
        cell_line_characterization_pluritest.microarray_url = valuef(['characterisation_pluritest_data', 'microarray_url'])

        # Parse files and save them

        characterization_pluritest_files_old = list(cell_line_characterization_pluritest.pluritest_files.all().order_by('id'))
        characterization_pluritest_files_old_encs = set([f.file_enc for f in characterization_pluritest_files_old])

        characterization_pluritest_files_new = []

        for f in valuef(['characterisation_pluritest_data']).get('uploads', []):
            if f.get('is_private') != '1':
                characterization_pluritest_files_new.append(parse_characterization_pluritest_file(f, cell_line_characterization_pluritest))

        characterization_pluritest_files_new_encs = set(characterization_pluritest_files_new)

        # Delete existing files that are not present in new data

        to_delete = characterization_pluritest_files_old_encs - characterization_pluritest_files_new_encs

        for characterization_pluritest_file in [f for f in characterization_pluritest_files_old if f.file_enc in to_delete]:
            logger.info('Deleting obsolete pluritest file %s' % characterization_pluritest_file)
            characterization_pluritest_file.file_doc.delete()
            characterization_pluritest_file.delete()

        if created or cell_line_characterization_pluritest.is_dirty():
            if created:
                logger.info('Added cell line characterization pluritest: %s' % cell_line_characterization_pluritest)
            else:
                logger.info('Updated cell line characterization pluritest: %s' % cell_line_characterization_pluritest)

            cell_line_characterization_pluritest.save()

            return True

        return False

    else:
        try:
            p = CelllineCharacterizationPluritest.objects.get(cell_line=cell_line)
            p.delete()
            return True

        except CelllineCharacterizationPluritest.DoesNotExist:
            pass


@inject_valuef
def parse_characterization_pluritest_file(valuef, source, characterization_pluritest):

    characterization_pluritest_file, created = CelllineCharacterizationPluritestFile.objects.get_or_create(
        pluritest=characterization_pluritest,
        file_enc=valuef('filename_enc').split('.')[0]
    )

    if created:
        current_enc = None
    else:
        current_enc = characterization_pluritest_file.file_enc

    characterization_pluritest_file.file_enc = value_of_file(valuef('url'), valuef('filename'), characterization_pluritest_file.file_doc, current_enc)

    characterization_pluritest_file.file_description = valuef('description')
    characterization_pluritest_file.save()

    return characterization_pluritest_file.file_enc


# EpiPluriTest
@inject_valuef
def parse_characterization_epipluriscore(valuef, source, cell_line):

    if valuef('characterisation_epipluriscore_flag'):
        cell_line_characterization_epipluriscore, created = CelllineCharacterizationEpipluriscore.objects.get_or_create(cell_line=cell_line)

        cell_line_characterization_epipluriscore.epipluriscore_flag = valuef('characterisation_epipluriscore_flag', 'nullbool')
        cell_line_characterization_epipluriscore.score = valuef(['characterisation_epipluriscore_data', 'score'])

        if valuef(['characterisation_epipluriscore_data', 'mcpg_present_flag']) == '1':
            marker_mcpg = True
        elif valuef(['characterisation_epipluriscore_data', 'mcpg_absent_flag']) == '1':
            marker_mcpg = False
        else:
            marker_mcpg = None

        if valuef(['characterisation_epipluriscore_data', 'oct4_present_flag']) == '1':
            marker_OCT4 = True
        elif valuef(['characterisation_epipluriscore_data', 'oct4_absent_flag']) == '1':
            marker_OCT4 = False
        else:
            marker_OCT4 = None

        cell_line_characterization_epipluriscore.marker_mcpg = marker_mcpg
        cell_line_characterization_epipluriscore.marker_OCT4 = marker_OCT4

        # Parse files and save them

        characterization_epipluriscore_files_old = list(cell_line_characterization_epipluriscore.epipluriscore_files.all().order_by('id'))
        characterization_epipluriscore_files_old_encs = set([f.file_enc for f in characterization_epipluriscore_files_old])

        characterization_epipluriscore_files_new = []

        for f in valuef(['characterisation_epipluriscore_data']).get('uploads', []):
            if f.get('is_private') != '1':
                characterization_epipluriscore_files_new.append(parse_characterization_epipluriscore_file(f, cell_line_characterization_epipluriscore))

        characterization_epipluriscore_files_new_encs = set(characterization_epipluriscore_files_new)

        # Delete existing files that are not present in new data

        to_delete = characterization_epipluriscore_files_old_encs - characterization_epipluriscore_files_new_encs

        for characterization_epipluriscore_file in [f for f in characterization_epipluriscore_files_old if f.file_enc in to_delete]:
            logger.info('Deleting obsolete epipluriscore file %s' % characterization_epipluriscore_file)
            characterization_epipluriscore_file.file_doc.delete()
            characterization_epipluriscore_file.delete()

        if created or cell_line_characterization_epipluriscore.is_dirty():
            if created:
                logger.info('Added cell line characterization EpiPluriScore: %s' % cell_line_characterization_epipluriscore)
            else:
                logger.info('Updated cell line characterization EpiPluriScore: %s' % cell_line_characterization_epipluriscore)

            cell_line_characterization_epipluriscore.save()

            return True

        return False

    else:
        try:
            p = CelllineCharacterizationEpipluriscore.objects.get(cell_line=cell_line)
            p.delete()
            return True

        except CelllineCharacterizationEpipluriscore.DoesNotExist:
            pass


@inject_valuef
def parse_characterization_epipluriscore_file(valuef, source, characterization_epipluriscore):

    characterization_epipluriscore_file, created = CelllineCharacterizationEpipluriscoreFile.objects.get_or_create(
        epipluriscore=characterization_epipluriscore,
        file_enc=valuef('filename_enc').split('.')[0]
    )

    if created:
        current_enc = None
    else:
        current_enc = characterization_epipluriscore_file.file_enc

    characterization_epipluriscore_file.file_enc = value_of_file(valuef('url'), valuef('filename'), characterization_epipluriscore_file.file_doc, current_enc)

    characterization_epipluriscore_file.file_description = valuef('description')
    characterization_epipluriscore_file.save()

    return characterization_epipluriscore_file.file_enc


# Morphology images - undifferentitated cells
@inject_valuef
def parse_characterization_undiff_morphology(valuef, source, cell_line):

    if valuef('characterisation_morphology_flag'):

        # Parse files and save them

        characterization_undiff_morphology_files_old = list(cell_line.undifferentiated_morphology_files.all().order_by('id'))

        characterization_undiff_morphology_files_old_encs = set([f.file_enc for f in characterization_undiff_morphology_files_old])

        characterization_undiff_morphology_files_new = []
        characterization_undiff_morphology_files_new_encs = set([])

        if valuef('characterisation_morphology_data'):
            for f in valuef(['characterisation_morphology_data']).get('uploads', []):
                if f.get('is_private') != '1':
                    characterization_undiff_morphology_files_new.append(parse_characterization_undiff_morphology_file(f, cell_line))

            characterization_undiff_morphology_files_new_encs = set(characterization_undiff_morphology_files_new)

        # Delete existing files that are not present in new data

        to_delete = characterization_undiff_morphology_files_old_encs - characterization_undiff_morphology_files_new_encs

        for characterization_undiff_morphology_file in [f for f in characterization_undiff_morphology_files_old if f.file_enc in to_delete]:
            logger.info('Deleting obsolete undiff morphology file %s' % characterization_undiff_morphology_file)
            characterization_undiff_morphology_file.file_doc.delete()
            characterization_undiff_morphology_file.delete()

        if characterization_undiff_morphology_files_old_encs != characterization_undiff_morphology_files_new_encs:
            logger.info('Updated cell line characterization morphology')
            return True
        else:
            return False


@inject_valuef
def parse_characterization_undiff_morphology_file(valuef, source, cell_line):

    characterization_undiff_morphology_file, created = CelllineCharacterizationUndifferentiatedMorphologyFile.objects.get_or_create(
        cell_line=cell_line,
        file_enc=valuef('filename_enc').split('.')[0]
    )

    if created:
        current_enc = None
    else:
        current_enc = characterization_undiff_morphology_file.file_enc

    characterization_undiff_morphology_file.file_enc = value_of_file(valuef('url'), valuef('filename'), characterization_undiff_morphology_file.file_doc, current_enc)

    characterization_undiff_morphology_file.file_description = valuef('description')
    characterization_undiff_morphology_file.save()

    return characterization_undiff_morphology_file.file_enc


# hPSC Scorecard
@inject_valuef
def parse_characterization_hpscscorecard(valuef, source, cell_line):

    if valuef('characterisation_hpsc_scorecard_flag') and valuef('characterisation_hpsc_scorecard_data'):
        cell_line_characterization_hpscscorecard, created = CelllineCharacterizationHpscScorecard.objects.get_or_create(cell_line=cell_line)

        if valuef(['characterisation_hpsc_scorecard_data', 'self_renewal_flag']) == '1':
            self_renewal = True
        elif valuef(['characterisation_hpsc_scorecard_data', 'self_renewal_flag']) == '0':
            self_renewal = False
        else:
            self_renewal = None

        cell_line_characterization_hpscscorecard.self_renewal = self_renewal

        if valuef(['characterisation_hpsc_scorecard_data', 'endoderm_flag']) == '1':
            endoderm = True
        elif valuef(['characterisation_hpsc_scorecard_data', 'endoderm_flag']) == '0':
            endoderm = False
        else:
            endoderm = None

        cell_line_characterization_hpscscorecard.endoderm = endoderm

        if valuef(['characterisation_hpsc_scorecard_data', 'mesoderm_flag']) == '1':
            mesoderm = True
        elif valuef(['characterisation_hpsc_scorecard_data', 'mesoderm_flag']) == '0':
            mesoderm = False
        else:
            mesoderm = None

        cell_line_characterization_hpscscorecard.mesoderm = mesoderm

        if valuef(['characterisation_hpsc_scorecard_data', 'ectoderm_flag']) == '1':
            ectoderm = True
        elif valuef(['characterisation_hpsc_scorecard_data', 'ectoderm_flag']) == '0':
            ectoderm = False
        else:
            ectoderm = None

        cell_line_characterization_hpscscorecard.ectoderm = ectoderm

        # Parse files and save them

        # Data files
        characterization_hpscscorecard_files_old = list(cell_line_characterization_hpscscorecard.hpsc_scorecard_reports.all().order_by('id'))
        characterization_hpscscorecard_files_old_encs = set([f.file_enc for f in characterization_hpscscorecard_files_old])

        characterization_hpscscorecard_files_new = []

        for f in valuef(['characterisation_hpsc_scorecard_data']).get('data_analysis_uploads', []):
            if f.get('is_private') != '1':
                characterization_hpscscorecard_files_new.append(parse_characterization_hpscscorecard_file(f, cell_line_characterization_hpscscorecard))

        characterization_hpscscorecard_files_new_encs = set(characterization_hpscscorecard_files_new)

        # Scorecards
        characterization_hpscscorecard_cards_old = list(cell_line_characterization_hpscscorecard.hpsc_scorecard_files.all().order_by('id'))
        characterization_hpscscorecard_cards_old_encs = set([f.file_enc for f in characterization_hpscscorecard_cards_old])

        characterization_hpscscorecard_cards_new = []

        for f in valuef(['characterisation_hpsc_scorecard_data']).get('scorecard_uploads', []):
            if f.get('is_private') != '1':
                characterization_hpscscorecard_cards_new.append(parse_characterization_hpscscorecard_card(f, cell_line_characterization_hpscscorecard))

        characterization_hpscscorecard_cards_new_encs = set(characterization_hpscscorecard_cards_new)

        # Delete existing files that are not present in new data

        # Data files
        to_delete = characterization_hpscscorecard_files_old_encs - characterization_hpscscorecard_files_new_encs

        for characterization_hpscscorecard_file in [f for f in characterization_hpscscorecard_files_old if f.file_enc in to_delete]:
            logger.info('Deleting obsolete hPSC Scorecard data file %s' % characterization_hpscscorecard_file)
            characterization_hpscscorecard_file.file_doc.delete()
            characterization_hpscscorecard_file.delete()

        # hPSC Scorecards files
        to_delete = characterization_hpscscorecard_cards_old_encs - characterization_hpscscorecard_cards_new_encs

        for characterization_hpscscorecard_card in [f for f in characterization_hpscscorecard_cards_old if f.file_enc in to_delete]:
            logger.info('Deleting obsolete hPSC Scorecard %s' % characterization_hpscscorecard_card)
            characterization_hpscscorecard_card.file_doc.delete()
            characterization_hpscscorecard_card.delete()

        # Save

        if created or cell_line_characterization_hpscscorecard.is_dirty():
            if created:
                logger.info('Added cell line characterization hPSC Scorecard: %s' % cell_line_characterization_hpscscorecard)
            else:
                logger.info('Updated cell line characterization hPSC Scorecard: %s' % cell_line_characterization_hpscscorecard)

            cell_line_characterization_hpscscorecard.save()

            return True

        return False

    else:
        try:
            p = CelllineCharacterizationHpscScorecard.objects.get(cell_line=cell_line)
            p.delete()
            return True

        except CelllineCharacterizationHpscScorecard.DoesNotExist:
            pass


@inject_valuef
def parse_characterization_hpscscorecard_file(valuef, source, characterization_hpscscorecard):

    characterization_hpscscorecard_file, created = CelllineCharacterizationHpscScorecardReport.objects.get_or_create(
        hpsc_scorecard=characterization_hpscscorecard,
        file_enc=valuef('filename_enc').split('.')[0]
    )

    if created:
        current_enc = None
    else:
        current_enc = characterization_hpscscorecard_file.file_enc

    characterization_hpscscorecard_file.file_enc = value_of_file(valuef('url'), valuef('filename'), characterization_hpscscorecard_file.file_doc, current_enc)

    characterization_hpscscorecard_file.file_description = valuef('description')
    characterization_hpscscorecard_file.save()

    return characterization_hpscscorecard_file.file_enc


@inject_valuef
def parse_characterization_hpscscorecard_card(valuef, source, characterization_hpscscorecard):

    characterization_hpscscorecard_card, created = CelllineCharacterizationHpscScorecardScorecard.objects.get_or_create(
        hpsc_scorecard=characterization_hpscscorecard,
        file_enc=valuef('filename_enc').split('.')[0]
    )

    if created:
        current_enc = None
    else:
        current_enc = characterization_hpscscorecard_card.file_enc

    characterization_hpscscorecard_card.file_enc = value_of_file(valuef('url'), valuef('filename'), characterization_hpscscorecard_card.file_doc, current_enc)

    characterization_hpscscorecard_card.file_description = valuef('description')
    characterization_hpscscorecard_card.save()

    return characterization_hpscscorecard_card.file_enc


@inject_valuef
def parse_characterization_marker_expression(valuef, source, cell_line):

    cell_line_marker_expressions_old = list(cell_line.undifferentiated_marker_expression.all().order_by('marker_id'))
    cell_line_marker_expressions_old_ids = set([m.marker_id for m in cell_line_marker_expressions_old])

    # Parse marker expressions and save them

    cell_line_marker_expressions_new = []

    for marker in source.get('characterisation_marker_expression_data', []):
        cell_line_marker_expressions_new.append(parse_marker_expression(marker, cell_line))

    cell_line_marker_expressions_new_ids = set([m.marker_id for m in cell_line_marker_expressions_new if m is not None])

    # Delete existing marker expressions that are not present in new data

    to_delete = cell_line_marker_expressions_old_ids - cell_line_marker_expressions_new_ids

    for cell_line_marker_expression in [me for me in cell_line_marker_expressions_old if me.marker_id in to_delete]:
        logger.info('Deleting obsolete cell line marker expression %s' % cell_line_marker_expression)
        cell_line_marker_expression.delete()

    # Check for changes (dirty)

    if (cell_line_marker_expressions_old_ids != cell_line_marker_expressions_new_ids):
        return True

    # TODO - add checking for updates once hPSCreg export is fixed
    # else:
    #     def marker_expressions_equal(a, b):
    #         return (
    #             a.marker_id == b.marker_id and
    #             a.marker == b.marker and
    #             a.expressed == b.expressed
    #         )
    #     for (old, new) in zip(cell_line_marker_expressions_old, cell_line_marker_expressions_new):
    #         if not marker_expressions_equal(old, new):
    #             return True

    return False


@inject_valuef
def parse_marker_expression(valuef, source, cell_line):

    if valuef('marker') is not None and valuef('marker_id') is not None:
        marker_id = valuef('marker_id')
        marker_name = valuef('marker').get('name')

        if valuef('expressed') == '1':
            marker_expressed_flag = True
        elif valuef('not_expressed') == '1':
            marker_expressed_flag = False
        else:
            marker_expressed_flag = None

        cell_line_marker_expression, created = CelllineCharacterizationMarkerExpression.objects.update_or_create(
            cell_line=cell_line,
            marker_id=marker_id,
            marker=marker_name,
            defaults={
                'expressed': marker_expressed_flag,
            }
        )

        for method in source.get('methods', []):
            parse_marker_expression_method(method, cell_line_marker_expression)

        # TODO - add checking for updates once hPSCreg export is fixed
        # list_old = list(cell_line_marker_expression.marker_expression_method.all().order_by('id'))
        # list_old_ids = set([m.id for m in list_old])
        #
        # list_new = []
        #
        # for method in source.get('methods', []):
        #     list_new.append(parse_marker_expression_method(method, cell_line_marker_expression))
        #
        # list_new_ids = set([m.id for m in list_new if m is not None])

        # Delete existing disease variants that are not present in new data

        # to_delete = list_old_ids - list_new_ids
        #
        # for marker_expression_method in [m for m in list_old if m.id in to_delete]:
        #     logger.info('Deleting obsolete marker expression method %s' % marker_expression_method)
        #     marker_expression_method.delete()

        if created:
            logger.info('Created new cell line marker expression: %s' % cell_line_marker_expression)

        return cell_line_marker_expression

    else:
        return None


@inject_valuef
def parse_marker_expression_method(valuef, source, cell_line_marker_expression):

    if valuef('name') is not None:

        cell_line_marker_expression_method, created = CelllineCharacterizationMarkerExpressionMethod.objects.update_or_create(
            marker_expression=cell_line_marker_expression,
            name=valuef('name'),
        )

        # Parse files and save them

        method_files_old = list(cell_line_marker_expression_method.marker_expression_method_files.all().order_by('id'))
        method_files_old_encs = set([f.file_enc for f in method_files_old])

        method_files_new = []
        method_files_new_encs = set()

        if valuef('uploads'):
            for f in valuef('uploads'):
                if f.get('is_private') != '1':
                    method_files_new.append(parse_marker_expression_method_file(f, cell_line_marker_expression_method))

            method_files_new_encs = set(method_files_new)

        # Delete existing files that are not present in new data

        to_delete = method_files_old_encs - method_files_new_encs

        for method_file in [f for f in method_files_old if f.file_enc in to_delete]:
            logger.info('Deleting obsolete marker method file %s' % method_file)
            method_file.file_doc.delete()
            method_file.delete()

        if created:
            logger.info('Created new cell line marker expression method: %s' % cell_line_marker_expression_method)

        return cell_line_marker_expression_method

    else:
        return None


@inject_valuef
def parse_marker_expression_method_file(valuef, source, cell_line_marker_expression_method):

    marker_method_file, created = CelllineCharacterizationMarkerExpressionMethodFile.objects.get_or_create(
        marker_expression_method=cell_line_marker_expression_method,
        file_enc=valuef('filename_enc').split('.')[0]
    )

    if created:
        current_enc = None
    else:
        current_enc = marker_method_file.file_enc

    marker_method_file.file_enc = value_of_file(valuef('url'), valuef('filename'), marker_method_file.file_doc, current_enc)

    marker_method_file.file_description = valuef('description')
    marker_method_file.save()

    return marker_method_file.file_enc


# RNA sequencing
@inject_valuef
def parse_characterization_rna_sequencing(valuef, source, cell_line):

    if valuef('characterisation_rna_sequencing_data'):
        if valuef('characterisation_rna_sequencing_data').get('data_url'):

            cell_line_characterization_rna_sequencing, created = CelllineCharacterizationRNASequencing.objects.update_or_create(
                cell_line=cell_line,
                defaults={
                    'data_url': valuef('characterisation_rna_sequencing_data').get('data_url')
                },
            )

            if created or cell_line_characterization_rna_sequencing.is_dirty():
                if created:
                    logger.info('Added cell line RNA sequencing link')
                else:
                    logger.info('Updated cell line RNA sequencing link')

                cell_line_characterization_rna_sequencing.save()

                return True

            else:
                return False

        else:
            try:
                rs = CelllineCharacterizationRNASequencing.objects.get(cell_line=cell_line)
                rs.delete()

                logger.info('Deleting cell line RNA sequencing link')
                return True

            except CelllineCharacterizationRNASequencing.DoesNotExist:
                return False

    else:
        try:
            rs = CelllineCharacterizationRNASequencing.objects.get(cell_line=cell_line)
            rs.delete()

            logger.info('Deleting cell line RNA sequencing link')
            return True

        except CelllineCharacterizationRNASequencing.DoesNotExist:
            return False


# Gene expression array
@inject_valuef
def parse_characterization_gene_expression_array(valuef, source, cell_line):

    if valuef('characterisation_gene_expression_array_data'):
        if valuef('characterisation_gene_expression_array_data').get('data_url'):

            cell_line_characterization_gene_expression_array, created = CelllineCharacterizationGeneExpressionArray.objects.update_or_create(
                cell_line=cell_line,
                defaults={
                    'data_url': valuef('characterisation_gene_expression_array_data').get('data_url')
                },
            )

            if created or cell_line_characterization_gene_expression_array.is_dirty():
                if created:
                    logger.info('Added cell line Gene Expression Array link')
                else:
                    logger.info('Updated cell line Gene Expression Array link')

                cell_line_characterization_gene_expression_array.save()

                return True

            else:
                return False

        else:
            try:
                gea = CelllineCharacterizationGeneExpressionArray.objects.get(cell_line=cell_line)
                gea.delete()

                logger.info('Deleting cell line Gene Expression Array link')
                return True

            except CelllineCharacterizationGeneExpressionArray.DoesNotExist:
                return False

    else:
        try:
            gea = CelllineCharacterizationGeneExpressionArray.objects.get(cell_line=cell_line)
            gea.delete()

            logger.info('Deleting cell line Gene Expression Array link')
            return True

        except CelllineCharacterizationGeneExpressionArray.DoesNotExist:
            return False


# Differentiation potency
@inject_valuef
def parse_characterization_differentiation_potency(valuef, source, cell_line):

    germ_layer_data = (
        ('endoderm', 'characterisation_differentiation_potency_endoderm_data'),
        ('mesoderm', 'characterisation_differentiation_potency_mesoderm_data'),
        ('ectoderm', 'characterisation_differentiation_potency_ectoderm_data'),
    )

    for data in germ_layer_data:
        if valuef(data[1]):
            if valuef(data[1]).get('detected_cell_types'):
                germ_layer, created = CelllineCharacterizationDifferentiationPotency.objects.get_or_create(cell_line=cell_line, germ_layer=data[0])

                cell_types_old = CelllineCharacterizationDifferentiationPotencyCellType.objects.filter(germ_layer=germ_layer)

                cell_types_old_names = set([ct.name for ct in cell_types_old])

                cell_types_new = []

                for cell_type in valuef(data[1]).get('detected_cell_types', []):
                    cell_types_new.append(parse_characterization_differentiation_potency_cell_type(cell_type, germ_layer))

                cell_types_new_names = set([ct.name for ct in cell_types_new])

                # Delete old cell types
                to_delete = cell_types_old_names - cell_types_new_names

                for cell_type_deleted in [ct for ct in cell_types_old if ct.name in to_delete]:
                    logger.info('Deleting obsolete cell line differentation potency cell type %s' % cell_type_deleted)
                    cell_type_deleted.delete()

        else:
            try:
                d = CelllineCharacterizationDifferentiationPotency.objects.get(cell_line=cell_line, germ_layer=data[0])
                d.delete()

                logger.info('Deleted cell line Differentiation potency %s' % (data[0],))
                return True

            except CelllineCharacterizationDifferentiationPotency.DoesNotExist:
                return False


@inject_valuef
def parse_characterization_differentiation_potency_cell_type(valuef, source, germ_layer):

    cell_type, created = CelllineCharacterizationDifferentiationPotencyCellType.objects.update_or_create(
        germ_layer=germ_layer,
        name=valuef('ont_name'),
        defaults={
            'in_vivo_teratoma_flag': valuef('in_vivo_teratoma_flag', 'nullbool'),
            'in_vitro_spontaneous_differentiation_flag': valuef('in_vitro_spontaneous_differentiation_flag', 'nullbool'),
            'in_vitro_directed_differentiation_flag': valuef('in_vitro_directed_differentiation_flag', 'nullbool'),
            'scorecard_flag': valuef('scorecard_flag', 'nullbool'),
            'other_flag': valuef('other_flag', 'nullbool'),
            'transcriptome_data': valuef('transcriptome_data_url'),
        }
    )

    # Parse markers

    markers_old = CelllineCharacterizationDifferentiationPotencyCellTypeMarker.objects.filter(cell_type=cell_type)

    marker_names_old = set([m.name for m in CelllineCharacterizationDifferentiationPotencyCellTypeMarker.objects.filter(cell_type=cell_type)])

    markers_new = []

    for marker in source.get('markers', []):
        markers_new.append(parse_characterization_differentiation_potency_cell_type_marker(marker, cell_type))

    marker_names_new = set([m.name for m in markers_new])

    # Delete old markers
    to_delete = marker_names_old - marker_names_new

    for marker_deleted in [m for m in markers_old if m.name in to_delete]:
        logger.info('Deleting obsolete cell line differentation potency marker %s' % marker_deleted)
        marker_deleted.delete()

    # Parse Morphology files and save them

    cell_type_morphology_files_old = list(cell_type.germ_layer_cell_type_morphology_files.all().order_by('id'))
    cell_type_morphology_files_old_encs = set([f.file_enc for f in cell_type_morphology_files_old])

    cell_type_morphology_files_new = []
    cell_type_morphology_files_new_encs = set([])

    for f in source.get('morphology_uploads', []):
        if f.get('is_private') != '1':
            cell_type_morphology_files_new.append(parse_characterization_differentiation_potency_cell_type_morphology_file(f, cell_type))

    cell_type_morphology_files_new_encs = set(cell_type_morphology_files_new)

    # Delete existing files that are not present in new data

    to_delete = cell_type_morphology_files_old_encs - cell_type_morphology_files_new_encs

    for cell_type_morphology_file in [f for f in cell_type_morphology_files_old if f.file_enc in to_delete]:
        logger.info('Deleting obsolete diff potency morphology file %s' % cell_type_morphology_file)
        cell_type_morphology_file.file_doc.delete()
        cell_type_morphology_file.delete()

    # Parse Protocol files and save them

    cell_type_protocol_files_old = list(cell_type.germ_layer_cell_type_protocol_files.all().order_by('id'))
    cell_type_protocol_files_old_encs = set([f.file_enc for f in cell_type_protocol_files_old])

    cell_type_protocol_files_new = []
    cell_type_protocol_files_new_encs = set([])

    for f in source.get('protocol_uploads', []):
        if f.get('is_private') != '1':
            cell_type_protocol_files_new.append(parse_characterization_differentiation_potency_cell_type_protocol_file(f, cell_type))

    cell_type_protocol_files_new_encs = set(cell_type_protocol_files_new)

    # Delete existing files that are not present in new data

    to_delete = cell_type_protocol_files_old_encs - cell_type_protocol_files_new_encs

    for cell_type_protocol_file in [f for f in cell_type_protocol_files_old if f.file_enc in to_delete]:
        logger.info('Deleting obsolete diff potency protocol file %s' % cell_type_protocol_file)
        cell_type_protocol_file.file_doc.delete()
        cell_type_protocol_file.delete()

    # Check if dirty and save

    if created or cell_type.is_dirty(check_relationship=True):
        if created:
            logger.info('Added cell line Differentiation potency cell type')
        else:
            logger.info('Updated cell line Differentiation potency cell type')

        cell_type.save()

    return cell_type


@inject_valuef
def parse_characterization_differentiation_potency_cell_type_morphology_file(valuef, source, cell_type):

    cell_type_morphology_file, created = CelllineCharacterizationDifferentiationPotencyMorphologyFile.objects.get_or_create(
        cell_type=cell_type,
        file_enc=valuef('filename_enc').split('.')[0]
    )

    if created:
        current_enc = None
    else:
        current_enc = cell_type_morphology_file.file_enc

    cell_type_morphology_file.file_enc = value_of_file(valuef('url'), valuef('filename'), cell_type_morphology_file.file_doc, current_enc)

    cell_type_morphology_file.file_description = valuef('description')
    cell_type_morphology_file.save()

    return cell_type_morphology_file.file_enc


@inject_valuef
def parse_characterization_differentiation_potency_cell_type_protocol_file(valuef, source, cell_type):

    cell_type_protocol_file, created = CelllineCharacterizationDifferentiationPotencyProtocolFile.objects.get_or_create(
        cell_type=cell_type,
        file_enc=valuef('filename_enc').split('.')[0]
    )

    if created:
        current_enc = None
    else:
        current_enc = cell_type_protocol_file.file_enc

    cell_type_protocol_file.file_enc = value_of_file(valuef('url'), valuef('filename'), cell_type_protocol_file.file_doc, current_enc)

    cell_type_protocol_file.file_description = valuef('description')
    cell_type_protocol_file.save()

    return cell_type_protocol_file.file_enc


@inject_valuef
def parse_characterization_differentiation_potency_cell_type_marker(valuef, source, cell_type):

    expressed_value = None

    if valuef('expressed') == '1':
        expressed_value = True

    if valuef('not_expressed') == '1':
        expressed_value = False

    marker, created = CelllineCharacterizationDifferentiationPotencyCellTypeMarker.objects.update_or_create(
        cell_type=cell_type,
        name=valuef('name'),
        defaults={
            'expressed': expressed_value,
        }
    )

    if created or marker.is_dirty():
        if created:
            logger.info('Added cell line Differentiation potency cell type marker')
        else:
            logger.info('Updated cell line Differentiation potency cell type marker')

        marker.save()

    return marker
