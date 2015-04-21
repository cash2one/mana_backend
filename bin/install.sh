#!/bin/bash
rm -fr /usr/lib/python2.*/dist-packages/mana_backend
rm -fr /usr/lib/python2.*/site-packages/mana_backend
rm -fr /usr/local/bin/mana-alarm 
rm -fr /etc/init.d/mana-backend
cp -r ../mana_backend /usr/lib/python2.*/dist-packages/
cp -r ../mana_backend /usr/lib/python2.*/site-packages/
cp mana-alarm /usr/local/bin/mana-alarm
cp mana-backend /etc/init.d/mana-backend
