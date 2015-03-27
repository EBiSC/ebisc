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


## ORM

CREATE DATABASE ebisc;
CREATE USER 'joh'@'localhost';
GRANT ALL ON ebisc.* TO 'joh'@'localhost';
mysql ebisc < schema.sql
./manage.py inspectdb --database source > ebisc/celllines/models-inspectd.py


## Questions

- Schema migration: how it is done?
    - Freeze feb 20
    - 4 changes since then
- HotStart data: is it aligned with the model?
    - It is incomplete
    - Has referential problems
    - cellinelab & cellinechecklist added
    - Report: where?
    - ECACC -> FTP, CSV
- Are there any 'unique together' constraints?
- Do we validate URLs -> fields containing url to URLField?
- Do we convert max_length=1000 fields to variable length char field TextField?

- A lot of fields are optional - this does not look right!

- Why is ForeignKey + Unique=True used instead of embedded fields?


## TODO

- [ ] Convert ForeignKey + Unique=True to OneToOne field or use embed (see questions)

## Search

- Dump ORM data to ElasticSearch
- Load data via ajax
- Display data
- Write update function
- Write searching / filtering widgets
- Connect widgets with update function

## Exec dashboard

- EBiSC Board Members (set user accounts)
- Order first by most recent 
- Print version Cell line data
- Grouping of data (Dana)
- Sales information (future goal - need to get QTY info from LIMS and sales data from ECACC)
- Option: Should there be a way for EBM to add notes to the Cell Line regarding Accept/Reject?
- Filters:
    - Accepted/Rejected/Pending
    - Depositor
    - Any other attribute? (Disease, Cell type, Tissue source)
    - Cell line status: available/not available
- Search: inlcudes all atributes

## Cell line Catalog

- User is customer
- Table:
    - Biosamples ID
    - Name
    - Depositor
    - Disease
    - Cell type
    - Cell line name synonims
- Filters:
    - Disease
    - Depositor
    - Cell type
    - Tissue source
    ------------------------------------
    - Protocol?
    - Mutant gene? (mutagene - not defined terms)
    - Growth mode?
    - Culture medium (we have, but empty for now) / culture system
    - Available formats? (ECACC)
- For sales link to ECACC?

## EBiSC Knowledge Community

- User is customer
- List of diseases? (page 97) -> then you get a list of celllines for that disease?? (... page 99) - primerjave med cell lini
- Assistance and support on differentiation, tests performed etc.?

  Services: 
    - Protocols (support material): (uploaded by depositors, approved by execs?)
        - cell line derivation protocol
        - quality control
        - investigations
        - etc
    - Training, support and experts
    - Knowledge forum

- Feedback form 30 days after purchase
- Support - not finalized

