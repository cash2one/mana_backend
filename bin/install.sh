#!/bin/bash
rm -fr /usr/lib/python2.*/mana_backend
rm -fr /usr/local/bin/mana-alarm 
rm -fr /etc/init.d/mana-backend
cp -r ../mana_backend /usr/lib/python2.*/
cp mana-alarm /usr/local/bin/mana-alarm
cp mana-backend /etc/init.d/mana-backend
