import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_style('whitegrid')


tips = sns.load_dataset('tips')
titanic = sns.load_dataset('titanic')
iris = sns.load_dataset('iris')

print(tips.head())
print(titanic.head())

################## lmplot; regression line ################
g = sns.lmplot(x= 'tip', y = 'total_bill', data = tips)
g = (g.set_axis_labels('Tip', 'Total Bill')).set(xlim = (0,10), ylim = (0,100))
plt.title('Title')
plt.show(g)

sns.regplot(x= 'tip', y = 'total_bill', data = tips)
plt.show()
################### Different subplots ###############################
h = sns.FacetGrid(titanic, col = 'survived', row = 'sex')
h = h.map(plt.hist, 'age')
plt.show(h)

############################ Scatter Pllot ###############
sns.stripplot(x = 'species', y = 'petal_length', data = iris)
plt.show()

sns.swarmplot(x = 'species', y = 'petal_length', data = iris)
plt.show()

############################# Bar Chart #####################
sns.barplot(x = 'sex', y = 'survived', hue = 'class', data = titanic)
plt.show()

############################# Count Plot ###########################
# Reds_d, Greens_d....
sns.countplot(x = 'deck', data = titanic, palette = 'Oranges_d')
plt.show()

############################# Point Plot #############################
sns.pointplot(x = 'class', y ='survived', data = titanic,\
                hue = 'sex', palette = {'male': 'g', 'female':'m'},\
                markers = ['^', 'o'],
                linestyles = ['-','--'] )
plt.show()

###################### Box Plot #############################
sns.boxplot(x = 'alive', y = 'age', hue = 'adult_male', data = titanic)
plt.show()

############################# Violin Plot  ###########################
sns.violinplot(x = 'age', y = 'sex', data = titanic, hue = 'survived')
plt.show()


##################### Univariate Distribution ######################
# Doesn't work if NaN present
sns.distplot(tips.tip, kde = False, color = 'b')
plt.show()

######################  HeatMap ##############################
sns.heatmap(tips.corr())
plt.show()

############################ Bivariate distribution #####################
sns.jointplot('sepal_length', 'sepal_width', data = iris)
plt.show()

h = sns.PairGrid(iris)
h = h.map(plt.scatter)
sns.pairplot(iris)
plt.show(h)


i = sns.JointGrid(x = 'sepal_length', y = 'sepal_width',data = iris)
i = i.plot(sns.regplot, sns.distplot)
plt.show(i)


########################### Configuration ######################
g.despine(left = True)

g.set_ylabels('Survived')

g.set_xticklabels(rotation = 45)

g.set_axis_labels('Survived', 'Sex')

h.set(xlim = (0,5),
      ylim = (0,5),
      xticks = [0,2.5,5],
      yticks = [0, 2.5, 5])

plt.title('Title')
plt.ylabel('Y')
plt.Xlabel('X')

plt.ylim(0,100)
plt.xlim(0,100)

plt.setp(ax, yticks =[0,5]) # Setting axis property
