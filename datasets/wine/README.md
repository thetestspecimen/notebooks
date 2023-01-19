# Wine recognition data

These data are the results of a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars.

The analysis determined the quantities of 13 constituents found in each of the three types of wines. 

I think that the initial data set had around 30 variables, but for some reason I only have the 13 dimensional version. I had a list of what the 30 or so variables were, but a.) I lost it, and b.), I would not know which 13 variables are included in the set.

The attributes are (dontated by Riccardo Leardi, riclea@anchem.unige.it )

## Original dataset info

**Title of Database:** Wine recognition data 
**Updated Sept 21, 1998 by C.Blake:** Added attribute information

## Attributes

All attributes are continuous
	
No statistics available, but suggest to standardise variables for certain uses (e.g. for use with classifiers which are NOT scale invariant)

1) Alcohol
2) Malic acid
3) Ash
4) Alkalinity of ash  
5) Magnesium
6) Total phenols
7) Flavonoids
8) Non-flavonoid phenols
9) Proanthocyanins
10) Colour intensity
11) Hue
12) OD280/OD315 of diluted wines
13) Proline

Missing Attribute Values: None

## Labels

Labels are provided as the final column (14)

class 1 - 59 instances
class 2 - 71 instances
class 3 - 48 instances

## Sources

1. Forina, M. et al, PARVUS - An Extendible Package for Data Exploration, Classification and Correlation. Institute of Pharmaceutical and Food Analysis and Technologies, Via Brigata Salerno, 16147 Genoa, Italy.
2. Stefan Aeberhard, email: stefan@coral.cs.jcu.edu.au
3. July 1991

## Past Usage

1. S. Aeberhard, D. Coomans and O. de Vel, Comparison of Classifiers in High Dimensional Settings, Tech. Rep. no. 92-02, (1992), Dept. of Computer Science and Dept. of Mathematics and Statistics, James Cook University of North Queensland. (Also submitted to Technometrics).

    The data was used with many others for comparing various classifiers. The classes are separable, though only RDA has achieved 100% correct classification. (RDA : 100%, QDA 99.4%, LDA 98.9%, 1NN 96.1% (z-transformed data)) (All results using the leave-one-out technique)

    In a classification context, this is a well posed problem with "well behaved" class structures. A good data set for first testing of a new classifier, but not very challenging.

2. S. Aeberhard, D. Coomans and O. de Vel, "THE CLASSIFICATION PERFORMANCE OF RDA" Tech. Rep. no. 92-01, (1992), Dept. of Computer Science and Dept. of Mathematics and Statistics, James Cook University of North Queensland. (Also submitted to Journal of Chemometrics).

    Here, the data was used to illustrate the superior performance of the use of a new appreciation function with RDA. 

## Data Source

https://archive-beta.ics.uci.edu/dataset/109/wine

## License

[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/legalcode)