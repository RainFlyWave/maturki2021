# 		zad 1
# # 	Podaj liczbę połączeń w rozbiciu na stacjonarne , 
# # 	komórkowe, zagraniczne

# 		zad 2
# # 	Podaj trzy numery telefonów, pod które wykonano najwięcej połączeń, 
# # 	i liczby tych połączeń.

# 		zad3
# # 	Utwórz zestawienie liczby połączeń – oddzielnie do telefonów stacjonarnych 
# # 	i komórkowych – wykonanych w poszczególnych dniach

# zagraniczne:	10+ cyfr
# komórkowe:	8 cyfr
# stacjonarne:	7 cyfrowe



#otwieramy plik telefony.txt
plik = open("telefony.txt", "r")
dane = []	#tworzymy pusta tablice dane

#pętla przechodzi przez każdą linijke w pliku
for i in plik:
	dane.append(i.rstrip("\n").split()) #zapisujemy linijki do tablicy dane
										# funkcja rstrip usuwa nam znak entera
										# funkcja split usuwa spacje i zamienia nam cała linie
										# w osobną tablice
plik.close() # zamykamy plik
dane.pop(0) # usuwamy pierwszą linijke w pliku (nagłówkową, zgodnie z polceniem)





def zad1():  #deklarujemy funkcje do zad 1
	print("\n\nzadanie 1\n")

	# tworzymy 3 zmienne przechowujące ilość numerów

	stacjonarne=0
	komorkowe=0
	zagraniczne=0

	# ta pętla przechodzi przez naszą tablice dane
	# jeżeli długość numeru telefonu będzie równa 7, doda ją do zmiennej "stacjonarne" ETC.

	for i in range(len(dane)):
		if len(dane[i][0]) == 7:
			stacjonarne+=1
		elif len(dane[i][0]) == 8:
			komorkowe+=1
		else:
			zagraniczne+=1

	# wypisywanie wyniku
	print("Liczba numerów stacjonarnych: "+str(stacjonarne))
	print("Liczba numerów komórkowych: "+str(komorkowe))
	print("Liczba numerów zagranicznych: "+str(zagraniczne))

def zad2():
	print("\n\nzadanie 2\n")

	dane_kopia = dane.copy() #tworzymy kopie tablicy aby nie pracowac na jej oryginale
	nr_tel = [] 
	#tworzymy pusta tablice nr_tel. Będzie ona przechowywać tylko numery telefonów(bez dat etc)
	for i in range(len(dane_kopia)):
		nr_tel.append(int(dane_kopia[i][0])) #tutaj dodaje nr tel do tablicy4

	bez_duplikatow = list(dict.fromkeys(nr_tel)) 	#usuwamy dupikaty i wrzucamy do nowej 
													#tablicy o nazwie bez duplikatów 

	ilosc_pol = [0] * len(bez_duplikatow) 	#tworzymy tablice która bedzie przechowywać ilosc polaczen
											# dla każdego numeru osobno
											# będzie ona posiadac tyle indexów co tablica "bez_duplikatu"
											# np nr_telefonu[0] = 444, ilosc_polaczen[0]= 10
											# ale to potem xD

	# Sprawdzamy ilośc duplikatów
	for i in range(len(bez_duplikatow)):
		for j in range(len(nr_tel)):
			if bez_duplikatow[i] == nr_tel[j]:
				ilosc_pol[i] += 1 	# jeżeli jakiś numer sie powtórzy, 
									#wpisujemy ilość wystąpienia powtórzenia

	#	deklarujemy 6 zmiennych
	#	top1_pol, top2_pol, top3_pol będą przechowywać największą ilośc połączeń(malejąco)
	#	top1_index, top2_index, top3_index będą przechowywać dany index ww. liczby
	top1_pol = 0
	top2_pol = 0
	top3_pol = 0

	top1_index = 0
	top2_index = 0
	top3_index = 0 



	# przebieg szukamy top1 ilości połączeń
	for i in range(len(ilosc_pol)):
		if ilosc_pol[i] >= top1_pol:
			top1_pol = ilosc_pol[i] #	największą ilośc połączeń zapisujemy do zmiennej top1_pol
			top1_index = i 			#	index największej liczby połączeń do zmiennej top1_index
	
	#drugi przebieg top2


	ilosc_pol_kopia = ilosc_pol.copy() 	#tworzymy kopie tablicy, ponieważ będziemy usuwac jeden z indeksów
	ilosc_pol_kopia.pop(top1_index)		#Usuwamy index z największą liczbą (top1_pol) aby wyszukac drugą największą


	for i in range(len(ilosc_pol_kopia)):  #to samo co w przebiegu 1
		if ilosc_pol_kopia[i] >= top2_pol:
			top2_pol = ilosc_pol_kopia[i]
			top2_index = i

	ilosc_pol_kopia.pop(top2_index) #ponowne usunięcie indeksu top2_pol

	# trzeci przebieg
	for i in range(len(ilosc_pol_kopia)):  #to samo co w przebiegu 1 tylko szukamy top3_pol
		if ilosc_pol_kopia[i] >= top3_pol:
			top3_pol = ilosc_pol_kopia[i]
			top3_index = i

			#wypisywanie wyniku :)
	print("Największa liczba połączeń:")
	print("Pod numer "+str(bez_duplikatow[top1_index])+" wykonano "+str(top1_pol)+" połączeń")
	print("Pod numer "+str(bez_duplikatow[top2_index])+" wykonano "+str(top2_pol)+" połączeń")
	print("Pod numer "+str(bez_duplikatow[top3_index])+" wykonano "+str(top3_pol)+" połączeń")


def zad3():
	print("\n\nzadanie 3\n")

	dane_kopia2 = dane.copy()	#	tworzymy kopie oryginalnej talicy "dane", just in case

	numery_komorkowe = []		#	tworzymy dwie tablice - każda z nich będzie przechowywać
	numery_stacjonarne = []		#	osobne dane dla numerów stacjonarnych i komórkowych


	# Dodajemy do tablicy "numery_komórkowe", wszystkie dane numerów 7 cyfrowych
	# a do tablicy "numery_stacjonarne", wszystkie dane numerów 8 cyfrowych
	for i in range(len(dane_kopia2)):
		if len(dane_kopia2[i][0]) == 7:
			numery_stacjonarne.append(dane_kopia2[i])
		elif len(dane_kopia2[i][0]) == 8:
			numery_komorkowe.append(dane_kopia2[i])
		
	#	tworzymy dwie tablice które będą przechowywać osobno ilość dni komórkowych i stacjonarnych

	dni_komorkowe = []
	dni_stacjonarne = []

	# wypełniamy ^^^ tablice dniami, od teraz będą one przechowywać TYLKO dni, 
	# bez innych danych takich jak
	# numer lub godzina
	for i in range(len(numery_komorkowe)):
		dni_komorkowe.append(numery_komorkowe[i][1])

	for i in range(len(numery_stacjonarne)):
		dni_stacjonarne.append(numery_stacjonarne[i][1])


	#	usuwamy duplikaty w obu tablicach
	nodupes_dni_komorkowe = list(dict.fromkeys(dni_komorkowe))
	nodupes_dni_stacjonarne = list(dict.fromkeys(dni_stacjonarne))

	#	deklarujemy tablice, będą one przyjomwały wartość 0 i będą miały długość(ilość indeksów)
	#	taką samą jak tablice bez duplikatów
	#	ponieważ każdy indeks dnia będzie odpowiadał ilośc połączeń
	ilosc_dni_kom = [0] * len(nodupes_dni_komorkowe)
	ilosc_dni_stac = [0] * len(nodupes_dni_stacjonarne)
	

	#	sprawdzane duplikatów i wpisywanie ilośc powtórzeń połączeń w danych dniach do tablicy
	#	wyżej stworzonych
	for i in range(len(nodupes_dni_komorkowe)):
		for j in range(len(dni_komorkowe)):
			if nodupes_dni_komorkowe[i] == dni_komorkowe[j]:
				ilosc_dni_kom[i]+=1

	for i in range(len(nodupes_dni_stacjonarne)):
		for j in range(len(dni_stacjonarne)):
			if nodupes_dni_stacjonarne[i] == dni_stacjonarne[j]:
				ilosc_dni_stac[i]+=1





				#	wypisywanie danych

	print("Dane dla Telefonów Komórkowych")
	for i in range(len(ilosc_dni_kom)):
		print("Dzien: "+nodupes_dni_komorkowe[i]+" Ilosc polączeń: "+ str(ilosc_dni_kom[i]))
	print("--------------------------------------")
	print("Dane dla Telefonów Stacjonarne")
	for i in range(len(ilosc_dni_stac)):
		print("Dzien: "+nodupes_dni_stacjonarne[i]+" Ilosc polączeń: "+ str(ilosc_dni_stac[i]))

	# PAMIĘTAJ ŻE PRZY WYPISYWANIU DANYCH FUNKCJĄ PRINT()
	# PRZEKONWERTUJ DANE FUNKCJA STR(), INACZEJ WYSTĄPI BŁĄD



zad1()
zad2()
zad3()