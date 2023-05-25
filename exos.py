import math

#EXOS 1.1.1


def moyenne_trois_nb(x, y, z):
  """
    Number*Number *Number ->float
    retourne la moyenne arithmétique de trois nombres
    """
  return (x + y + z) / 3


#EXOS 1.1.2


def moyenne_ponderee(x, y, z, px, py, pz):
  # avec somme de px,py,pz non nulle
  return ((x * px) + (y * py) + (z * pz)) / (px + py + pz)


#EXOS 1.2.1


def aire_disque(r):
  return r * pow(math.pi, 2)


#EXOS 1.2.2


def aire_couronne(ri, re):
  """
  Number->float
  re>=ri>=0
  """
  aire = aire_disque(re) - aire_disque(ri)
  return aire


#EXOS 1.3.1


def prix_ttc(tva, ht):
  """
  tva %  
  Number Number -> float
  """
  return ht * (1 + (tva / 100))


#EXOS 1.3.2


def prix_ht(tva, ttc):
  """
  Number Number -> float 
   
  """
  return ttc / (1 + (tva / 100))


#EXOS 1.4.1


def fahrenheit_vers_celsius(t):
  """
  Number -> float
  t en Celsius
  """
  return (t - 32) * (5 / 9)


#EXOS 1.4.2


def celsius_vers_fahrenheit(t):
  """
  Number->float
  t en Fahrenheit
  """
  return ((9 / 5) * t) + 32


#EXOS 1.5.1
"""
PENSER A FACTORISER 
"""


def polynomiale(a, b, c, d, x):
  return (x * (c + (x * (a * x + b)))) + d


#EXOS 1.5.2


def poylnomiale_carre(a, b, c, x):
  return c + (x * x * (b + a * x * x))  # theoreme de hörner


#EXOS 1.6.1


def fermat(n):
  """
  Number->int
  """
  return pow(2, pow(2, n)) + 1


#EXOS 1.7.1


def excursion(nb_pers):
  """
  Number->int
  """
  prix_bus = 1200 * (math.ceil(nb_pers / 60))
  prix_guide = 300 * (math.ceil(nb_pers / 18))
  return prix_bus + prix_guide


def excursion2(nb_adu, nb_enf):
  prix_bus = 1200 * (math.ceil((nb_adu + nb_enf) / 60))
  prix_guide_adu = 300 * (math.ceil(nb_adu / 18))
  prix_guide_enf = 250 * (math.ceil(nb_enf / 8))
  return prix_bus + prix_guide_adu + prix_guide_enf


#EXOS 2.2.1


def volume_tetraedre(a, b, c, d, e, f):
  x = a * a + b * b - d * d
  y = b * b + c * c - e * e
  z = a * a + c * c - f * f

  p = 4 * a * a * b * b * c * c
  q = (a * a * x * x) + (b * b * z * z) + (c * c * y * y)
  r = x * y * z

  V = math.sqrt(p - q + r) / 12

  return V


#EXOS 2.2.2


def volume_tetraedre_regulier(a):
  V = math.sqrt(2) / 12 * math.pow(a, 3)
  return V


#EXOS 2.3.1


def mention(note):
  """
  Number->float Number >= 0 
  """
  if note < 10:
    mention = 'Elimine'
  elif note < 12 and note >= 10:  # pas besoin de mettre la double condition ..................
    mention = 'Passable'
  elif note >= 12 and note < 14:
    mention = 'AB'
  elif note >= 14 and note < 16:
    mention = 'B'
  elif note >= 16 and note <= 20:
    mention = 'TB'
  return mention


# EXOS 2.3.2


def mention_amelioree(note):
  if note < 12:
    if note < 10:
      return 'Elimine'
    else:
      return 'Passable'
  elif note < 14:
    return 'AB'
  elif note < 16:
    return 'B'
  else:
    return 'TB'


#EXOS 2.4.2
def f(n1, n2, n3):
  if n1 < n2:
    if n2 < n3:
      return 'cas1'
    elif n1 < n3:
      return 'cas5'
  elif n2 < n1:
    if n1 < n3:
      return 'cas3'
    elif n2 > n3:
      return 'cas6'
  elif n3 < n1:
    if n2 < n3:
      return 'cas4'
    else:
      return 'cas2'
#EXOS 2.5

  def ou(p, q):
    if (p):
      return True
    elif (q):
      return True
    else:
      return False

  def et(p, q):
    if (p):
      if (q):
        return True
    else:
      return False

  def non(p):
    if (p):
      return True
    else:
      return False

#EXOS 2.6

  def egal_eps(x1, x2, epsilon):
    """
    Float*Float*Float
    """
    if abs(x1 - x2) < epsilon:
      return True
    else:
      return False

  def fiabilite(v1, v2, v3, epsilon):
    if egal_eps(v1, v2, epsilon) and egal_eps(v2, v3, epsilon) and egal_eps(
        v1, v3, epsilon):
      return 1
    elif ((egal_eps(v1, v2, epsilon) and egal_eps(v2, v3, epsilon))
          or (egal_eps(v1, v2, epsilon) and egal_eps(v1, v3, epsilon))
          or (egal_eps(v1, v3, epsilon) and egal_eps(v2, v3, epsilon))):
      return 2 / 3
    else:
      return 0


#EXOS 3.1.1


def somme_impairs_inf(n):
  i = 1
  s = 0
  while i <= n:
    s += i
    i += 2
  return s


#EXOS 3.1.2


def somme_premiers_impairs(n):
  i = 1
  somme = 0
  imp = 1
  while i <= n:
    somme += imp
    imp += 2
    i += 1
  return somme


#EXOS 3.2.1
def reste(a, b):
  return ((a / b) - math.floor(a / b)) * b


#EXOS 3.2.2
def est_divisible(a, b):
  if a % b == 0:
    return True
  else:
    return False


# EXOS 3.2.3
def ppcm(a, b):
  r = a
  while not (est_divisible(r, b)):
    r += a
  return r


#EXOS 3.4.1
def divise(n, p):
  if n % p == 0:
    return True
  else:
    return False  # pas besoin ....., juste return n%p == 0 ça retourne True ou False


#EXOS 3.4.2
def est_premier(n):
  i = n - 1
  b = True
  while i > 1:
    if (divise(n, i)):
      b = False
    i -= 1
  return b


#EXOS 3.5 Suite de Fibonacci
# 3.5.1
def fibonacci(n):
  if n == 0:
    return 0
  elif n >= 1:
    # initialisation de la boucle
    ff = 0
    f = 1
    i = 2
    while i <= n:
      fff = ff  #fff represente f indice n-2
      ff = f  # ff represente f indice n-1
      f = ff + fff  # calcul de f
      i += 1
    print(f)
    return f


# 3.5.2
def fibo_diff(k):
  if (k >= 2):
    return fibonacci(k) / fibonacci(k - 1)


# 3.5.3
def fibo_approx(n):
  f = ((1 + math.sqrt(5)) / 2)**n / math.sqrt(5)
  return f


#EXOS 4.4
"""
Donner une définition de la fonction nb_couples_intervalle qui, étant donné deux entiers n
et p tels que n <= p, renvoie le nombre de couples (i, j) d’entiers appartenant à l’intervalle [n, p]
tels que i < j.
"""


def nb_couples_intervalle(n, p):
  i = n
  nb = 0
  while i < p:
    j = i + 1
    while j <= p:
      nb += 1
      j += 1
    i += 1
  return nb


"""
Donner une définition de la fonction nb_couple_divise qui, étant donné deux entiers n et p
tels que n <= p, compte le nombre de couples (i, j) d’entiers distincts appartenant à l’intervalle
[n, p] tels que i divise j.
"""


def nb_couples_divise(n, p):
  i = n
  nb = 0
  while i < p:
    j = i + 1
    while j <= p:
      if j % i == 0:
        nb += 1
      j += 1
    i += 1
  return nb


"""
Modifier la fonction précédente pour qu’elle trace l’exécution des boucles imbriquées. Il faut
pour cela insérer des instructions d’affichage (print) au bon endroit.
"""


def nb_couples_divise_print(n, p):
  i = n
  nb = 0
  while i < p:
    j = i + 1
    while j <= p:
      print('couple(', i, ',', j, ')')
      if j % i == 0:
        nb += 1
        print(i, 'divise', j)
      j += 1
    i += 1
  return nb


"""
On se pose maintenant le problème non pas du nombre mais de l’existence d’un tel couple (i, j)
tel que i divise j.On pourra aussi compter le nombre de boucle effectuée.
"""


def existe_couples_divise(n, p):
  i = n
  exist = False
  nb_test = 0
  while i < p:
    j = i + 1
    while j <= p:
      nb_test += 1
      if j % i == 0:
        return True, nb_test
      j += 1
    i += 1
  return exist, nb_test


#EXOS 5.6 ADN
"""
Donner une définition de la fonction base_comp qui, étant donnée une base azotée, renvoie la
base complémentaire.
"""


def base_comp(a):
  """
  a appartient à l'ensemble {'A','T','G','C'}
  string->string
  """
  if a == 'A':
    return 'T'
  if a == 'T':
    return 'A'
  if a == 'G':
    return 'C'
  if a == 'C':
    return 'G'


"""
Donner une définition de la fonction brin_comp qui, étant donné un brin d’ADN, renvoie le
brin d’ADN complémentaire.
"""


def brin_comp(brin):
  """
  string->string
  """
  i = 0
  comp = ''
  while i < len(brin):
    comp += base_comp(brin[i])
    i += 1
  return comp


"""
Donner une définition test_comp qui, étant donné deux brins d’ADN, teste si ces deux brins
sont complémentaires.
"""


def test_comp(brinA, brinB):
  if len(brinA) == len(brinB):
    if brin_comp(brinA) == brinB:
      return True

  return False


"""
Donner une définition de la fonction test_sous_sequence qui étant donnés deux brins d’ADN,
teste si le premier est une sous-sequence du second.
"""


def test_sous_sequence(sousbrin, brin):
  i = 0
  m = len(sousbrin)
  n = len(brin)

  if n == 0:
    return True
  else:
    while i + m <= n:
      if sousbrin == brin[i:i + m]:
        return True
      i += 1
  return False  # test_sous_sequence('AC','ACDC')


"""
Donner une définition de la fonction recherche_sous_sequence qui étant donnés deux brins
d’ADN b1 et b2, renvoie l’indice de b2 correspondant au début de b1 si b1 est une sous-séquence
de b2 et ne renvoie rien (None) sinon.
"""


def recherche_sous_sequence(sousbrin, brin):
  i = 0
  m = len(sousbrin)
  n = len(brin)

  if n == 0:
    return True
  else:
    while i + m <= n:
      if sousbrin == brin[i:i + m]:
        return '[', i, ':', i + m, ']'
      i += 1
  return None


# EXOS 5.8 Compression (RLE)


def est_chiffre(c):
  return ('0' <= c) and (c <= '9')


"""
Donner une définition de la fonction de décompression.
Vous pourrez vous aider de la fonction est_chiffre donnée ci-dessus
"""


def decompression(comp):
  result = ''
  i = 0
  while i < len(comp):
    if est_chiffre(comp[i]):
      # reinitialisation des variables pour chaque nouveau chiffre
      j = 0
      k = 1
      nb = ''
      while est_chiffre(comp[i + j]):
        nb += comp[i + j]
        j += 1
      nb = int(nb)
      while k < nb:
        result += comp[i + j]
        k += 1
    else:
      result += comp[i]
    i += 1
  return result


"""
Donner une définition de la fonction compression qui retourne la version compressée de la
chaîne s passée en paramètre selon le principe RLE.
"""


# definition de la fonction supression qui va supprimer les caractères en doublons de la chaine pour ne pas avoir à les recalculer
def suppression(c, s):
  res =''
  for d in s:
    if d != c:
      res = res + d
  return res


def compression(s):
  """
  string->string
  """
  nb = 0
  r = ''
  prev = ''
  for e in s:
    if e == prev:
      nb = nb + 1
    else:
      if nb > 1:
        r = r + str(nb)
      r = r + prev
      prev = e
      nb = 1
  if nb > 1:
    r = r + str(nb)
  r = r + prev
  return r


# EXOS 5.9 Anagramme

def moins_lettre(c,a):
  premiere_trouvee = False
  res = ''
  for d in c:
    if d != a:
      res = res + d
    elif not premiere_trouvee:
      premiere_trouvee = True
    else:
      res = res + d
  if premiere_trouvee:
    return res
  else:
    return None
def anagramme(m1,m2):
  copy=m2
  res=''
  for x in m1:
    res=moins_lettre(copy,x)
    if res==None:
      return False
    else:
      copy=res
  return(copy=='')
    

  
# EXOS 6.1
"""
Donner une définition de la fonction repetition qui, étant donné un élément x et un entier
naturel k, renvoie la liste contenant k occurrences de x.
"""


def repetition(k, n):
  i = 0
  result = []
  while i < n:
    result.append(k)
    i += 1
  return result


"""
Donner une définition de la fonction repetition_bloc qui, étant donné une liste L et un entier
naturel k, renvoie la liste obtenue en concaténant k fois la liste L.
"""


def repetition_bloc(k, n):
  """
  List*Integer -> List
  """
  result = []
  i = 0
  while i < n:
    for elem in k:
      result.append(elem)
    i += 1
  return result


# EXOS 6.2
"""
Donner une définition de la fonction max_liste qui, étant donné une liste non vide de nombres,
renvoie le plus grand élément de cette liste.
"""


def max_liste(list):
  """
  List[float]->float
  """
  max = list[0]
  for x in list:
    if x > max:
      max = x
  return max


"""
Donner une définition de la fonction nb_occurrences qui, étant donné une liste L et un élément
x, renvoie le nombre d’occurrences de x dans L.
"""


def nb_occurences(L, n):
  i = 0
  for x in L:
    if n == x:
      i += 1
  return i


"""
Donner une définition de la fonction nb_max qui, étant donné une liste non vide de nombres L,
renvoie le nombre d’occurrences du maximum de L dans L.
"""


def nb_max(L):
  if L != []:
    return nb_occurences(L, max_liste(L))


# EXOS 6.3 Moyenne et Variance
"""
Donner une définition de la fonction somme qui, étant donné une liste de nombres, renvoie la
somme des éléments de cette liste, ou 0 si la liste est vide.
"""


def somme(L):
  if L != []:
    s = 0
    for x in L:
      s += x
    return s
  return 0


def moyenne(L):
  return somme(L) / (len(L))


def carres(L):
  C = []
  for x in L:
    C.append(x * x)
  return C


def variance(L):
  return moyenne(carres(L)) - moyenne(L)**2


def ecart_type(L):
  return math.sqrt(variance(L))

#6.4 Liste de diviseurs

#6.4.1
def list_diviseur(n):
  div=[]
  i=1
  while i <=n:
	   if n%i == 0 : 
		    div.append(i)
	   i+=1
  return div
#6.4.2
def list_diviseur_impair(n):
  div=[]
  i=1
  while i <=n:
	   if n%i == 0 : 
		    div.append(i)
	   i+=2
  return div
#6.4.3	
def list_diviseur_pair(n):
  div=[]
  i=2
  while i <=n:
	   if n%i == 0 : 
		    div.append(i)
	   i+=2
  return div

#6.7 Découpage      

#6.7.1
def decoupage_simple(i,j,L):
  if i>=0 and j>=0:
    return L[min([i,j]):max([i,j])]
#6.7.2
def decoupage_pas(i,j,L,p):
   if i>=0 and j>=0 and p>0:
    return L[min([i,j]):max([i,j]):p] 
#6.7.3
def decoupage_pas_inv(i,j,L,p):
  reversed=[]
  k=i
  while abs(k)<j:
    if k <len(L):
      reversed.append(L[k])
    k=k+p
  return reversed

  
#7.2 Nombre d'occurrence du maximum dans une liste
def nb_de_max(L):
  max=L[0]
  n=0
  for x in L:
    if x > max:
      max=x
      n=1
    elif x == max:
      n+=1
  return (max,n)

#7.4 Alignement de points
# Pour cet exercice on définit le type informel : Point: tuple[int,int]

#7.4.1
def vecteur(p1,p2):
  """
  Point*Point=>List
  """
  return [p2[0]-p1[0],p2[1]-p1[1]]
  
#7.4.2
def alignes(p1,p2,p3):
  v1=vecteur(p1,p2)
  v2=vecteur(p2,p3)
  if v1[0]/v2[0]==v1[1]/v2[1]:
    return True
  else:
    return False
#7.4.3
def alignement(L):
  """
  Liste[Point] => Bool
  """
  al=[]
  i=0
  while i<len(L)-2:
    if alignes(L[i],L[i+1],L[i+2]):
      al.append(1)
    i+=1
  if len(al)==len(L)-2:
    return True
  else:
    return False

#JEU DE TEST

x = 2
y = 9
z = 19

px = 2
py = 0.75
pz = 0.25


l = [3,5,5,4,6,6,6]
ll=['am','stram','gram','meanie','miny','moe','catch','atiger','byhis','toe']

px=[3,5]
py=[4,7]
pz=[6,11]
pw=[1,1]
Lp=[px,py,pz,pw]
print(alignement(Lp))
