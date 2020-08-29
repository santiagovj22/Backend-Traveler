#!/bin/sh

MONGOURI = DB_TRAVELER_CONNECTION

echo "\nBefore Migration"
pymongo-migrate show -u $MONGOURI -m ./migrations/

echo "\nRunning Migration"
pymongo-migrate migrate -u $MONGOURI -m ./migrations/

echo "\nAfter Migration"
pymongo-migrate show -u  $MONGOURI -m ./migrations/

echo "\nMigration Graph"
pymongo-migrate graph -u  $MONGOURI -m ./migrations/
