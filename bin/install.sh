#!/bin/bash
rm -fr /usr/lib/python2.*/dist-packages/mana_backend
rm -fr /usr/lib/python2.*/site-packages/mana_backend
rm -fr /usr/local/bin/mana-alarm 
rm -fr /etc/init.d/mana-backend
python_path1="/usr/lib/python2.*/dist-packages/"
python_path2="/usr/lib/python2.*/site-packages/"
if [ -d $python_path1 ];then
    cp -r ../mana_backend /usr/lib/python2.*/dist-packages/
fi
if [ -d $python_path2 ];then
    cp -r ../mana_backend /usr/lib/python2.*/site-packages/
fi
cp mana-alarm /usr/local/bin/mana-alarm
cp mana-backend /etc/init.d/mana-backend
