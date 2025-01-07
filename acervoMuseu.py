# Acervo do museu:
from Acervo import Acervo
from Fossil import Fossil

f2 = Fossil('IR100450','Irritator Challengeri','Irritator', 'Carnívoro', 'Crânio', 'Cerca de 100 milhões de anos','https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-XK32_4Us1DDqLprmGGfXBWW1UstLoC5j5LQl-rOXPg54AwaMAo0C2l_bgx4fO55om80Au4JwJHg0_3WS1VUu1lwPNh4JImSVrK_YipnJYvkFP6IPs4GUoRtZ4jJExJravD-X0MAFifI/s1600/irritator_skull.jpg')
f1 = Fossil('UB456964', 'Ubirajara Jubatus','Ubirajara', 'carnívoro', 'esqueleto parcial', 'Cerca de 110 milhões de anos','https://s2-g1.glbimg.com/tLSgqOz-5R_FLmMsRS5xupHrFZA=/0x0:1067x498/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2020/Z/o/m2SMNDSjyHjVo5EFrZJQ/fossil-ubirajara-jubatus.jpeg')
f3 = Fossil('OX362519', 'Oxalaia Quilombensis', 'Oxalaia','Carnívoro', 'Crânio', 'cerca de 95 milhões de anos','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAYcsrbfc5PS7iEVQLuNLh1CwkDwvndwVinQ&s')
f4 = Fossil('ST126306', 'Staurikosaurus pricei','Staurikosaurus', 'Carnívoro', 'Esqueleto', 'cerca de 210 milhões de anos', 'https://hypescience.com/wp-content/uploads/2024/10/Staurikosaurus_esqueleto.jpg')

acervoDino = Acervo([f1,f2,f3,f4])