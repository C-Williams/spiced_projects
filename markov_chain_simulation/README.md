# Markov Chain Monte Carlo

### This project builds a Markov Chain simulation to track fake customers in a fake grocery store.

Libraries used include:

- pandas
- matplotlib
- seaborn
- numpy
- glob
- cv2

Other tools:

- Tableau

This group project required collaboration and asynchronous communications to build and was a great
learning opportunity. One of my group mates was a Tableau expert and was gracious enough to show us around all the various features of Tableau.

In the end, three main parts of the project were built:

1. Expanded and clarified EDA was presented using Tableau
  - This is not on this page as I do not have a Tableau license and cannot access the completed files.
2. Two separate python scripts for simulating customer behavior (found in the simulation folder).
  - Both can be run in the terminal using CLI
  - [The first](https://github.com/C-Williams/spiced_projects/blob/main/markov_chain_simulation/simulation/customer.py) can be used to create a single customer and track their activity inside a store.
  - [The second](https://github.com/C-Williams/spiced_projects/blob/main/markov_chain_simulation/simulation/sim_day.py) utilizes the first python file to simulate any number of customers for a full day of activity and then saves this information into a csv file for later use.
3. Finally a [visual tool](https://github.com/C-Williams/spiced_projects/blob/main/markov_chain_simulation/grocery_store_visual/images/supermarket.gif) was created using the average number of customers per minute to help see and present when the store could be the busiest.