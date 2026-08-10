import mymodule

sonuc = mymodule.sayi
sonuc = mymodule.sayilar
sonuc = mymodule.urun
sonuc = mymodule.urun["urunAdi"]
sonuc = mymodule.urun["renkler"]
sonuc = mymodule.toplama(5,10)

import mymodule as m

from mymodule import sayi,sayilar,urun

sonuc = m.urun["urunAdi"]

sonuc = sayi
sonuc = sayilar

from mymodule import *

sonuc = urun


print(sonuc)