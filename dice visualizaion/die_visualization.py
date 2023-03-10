from plotly.graph_objs import Bar, Layout
from plotly import offline


from die import Die

#Create a D6
die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
for value in range(1, (die1.num_sides+1 + die2.num_sides+1)):
    frequency = results.count(value)

    frequencies.append(frequency)


x_values = list(range(1, die1.num_sides+1 + die2.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title = "Results of rolling on D6 1000 times", xaxis = x_axis_config, yaxis = y_axis_config )

offline.plot({'data':data, 'layout':my_layout}, filename="d6.html")