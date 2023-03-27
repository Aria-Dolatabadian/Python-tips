#Create three dictionaries, then create one nested dictionary that will contain the other three dictionaries

Cultivar1 = {
  "name" : "Westar",
  "year" : 2018
}
Cultivar2 = {
  "name" : "Glacier",
  "year" : 2019
}
Cultivar3 = {
  "name" : "Quinta",
  "year" : 2020
}

Genotypes = {
  "Cultivar1" : Cultivar1,
  "Cultivar2" : Cultivar2,
  "Cultivar3" : Cultivar3
}
print(Genotypes)
