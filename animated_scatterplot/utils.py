def fix_df(df):
    """
    Takes in a DataFrame and returns the same DataFrame with integer data types, 
    a renamed index, and the DataFrame is also melted to prepare for graphical
    representation.
    
    Args: 
        df (_DataFrame_): A DataFrame with an index full of country names and 
        yearly data across the horizontal axis.
        
    Returns:
        df _DataFrame_: The same DataFrame which has been transformed.
    """
    # Change all values to integer types for graphing
    df.columns = df.columns.astype(int)
    
    # Set a name to use in the melted DataFrame
    value_name = df.index.name.lower().replace(" ","_")
    
    # Change the index to the proper name
    df.index.name = 'country'
    
    # Bring the index out in order to melt.
    df = df.reset_index()
    
    # Melt the DataFrame into the proper shape using the previously defined
    # value_name
    df = df.melt(id_vars = 'country', 
                 var_name = 'year', 
                 value_name = value_name
                 )
    
    return df


def create_plots(df_) -> None:
    """
    Takes in a DataFrame and uses its values to produce several individual plots.
    
    Args:
        df (_DataFrame_): A DataFrame with a yearly data for life expectancy,
        total fertility rate, and population which also has a continent column.

    Returns:
        None: Saves plot figures into a 'data' folder with unique names for each 
        plot.
    """
    # Here, .unique is used in order to keep the graphs from repeating every time 
    # a year occurs in the DataFrame
    for year in df_['year'].unique():

        # The data is grouped in order to properly assign labels in the plots and
        # in the legend.
        df = df_.loc[df_['year'] == year]
        grouped_df = df.groupby('continent')

        fig, ax = plt.subplots(figsize=(10,10))
        for name, group in grouped_df:
            plt.scatter(x = group['life_expectancy'],
                        y = group['total_fertility_rate'],
                        color=colors[name],
                        s=group['total_population'],
                        label=name,
                        alpha=.5)
        
        # This builds a simple text block in the middle of the plots which tracks
        # what year the plot shows.
        ax.text(49, 5,f'{year}', fontsize=32, 
                alpha=.3, fontdict={'weight':'bold'})
        
        # Set titles
        ax.set_ylabel('Fertility Rate')
        ax.set_xlabel('Life Expectancy')
        plt.title(f'Life Expectancy and Fertility Rate by Continent')

        lgd = plt.legend(loc='upper right')

        # These handles redefine the size of each legend marker. Without this 
        # resizing, the markers would be proportional to their respective 
        # continent.
        lgd.legendHandles[0]._sizes = [60]
        lgd.legendHandles[1]._sizes = [60]
        lgd.legendHandles[2]._sizes = [60]
        lgd.legendHandles[3]._sizes = [60]
        lgd.legendHandles[4]._sizes = [60]
        lgd.legendHandles[5]._sizes = [60]
        
        # Establish a set axes so the graph size does not change.
        plt.axis((25, 85, 0, 10))

        # Create unique names for each figure and save them in a data folder.
        plt.savefig(f"./data/df_{year}.png")

        plt.close();
    