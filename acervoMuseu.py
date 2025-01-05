# Acervo do museu:
from Acervo import Acervo
from Fossil import Fossil

f2 = Fossil('IR100450','Irritator Challengeri', 'Carnívoro', 'Crânio', 'Cerca de 100 milhões de anos')
f1 = Fossil('UB456964', 'Ubirajara Jubatus', 'carnívoro', 'esqueleto parcial', 'Cerca de 110 milhões de anos')
f3 = Fossil('OX362519', 'Oxalaia Quilombensis', 'Carnívoro', 'Crânio', 'cerca de 95 milhões de anos')
f4 = Fossil('ST126306', 'Staurilosaurus pricei', 'Carnívoro', 'Esqueleto', 'cerca de 210 milhões de anos' )

acervoDino = Acervo([f1,f2,f3,f4])