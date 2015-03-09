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
