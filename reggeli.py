reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
ebed = {'víz', 'halászlé', 'kenyér'}

   
print(reggeli & ebed)
   
print(reggeli | ebed)
   
print(reggeli - ebed)
   
print(reggeli ^ ebed)

gyumolcskosar = ['eper', 'szilva', 'alma', 'eper']

fajta = set()
for gyumolcs in gyumolcskosar:
    fajta.add(gyumolcs)
print(fajta)

reggeli.add('lekvár')

reggeli.pop()
    

# reggeli.remove('sajt')

reggeli.discard('sajt')

'''
 Halmaz (set):
- rendezetlen (elemeknek nincs indexe)
    - egy elem csak egyszer szerepelhet
    - többféle típust tárolhat egyszerre is
    - a halmaz eleme maga nem változtatható meg
    '''
    
reggeli = {'tea', 'vaj', 'piritós'}
ebed = set()
ebed = set(['halászlé', 'kenyér', True]) 

#1feladat
