import os
import numpy as np
import pandas as pd


def process_data():
    fertility = pd.read_csv(os.getenv('GAPMINDER_FERTILITY'), index_col='Country', encoding='utf-8')
    life_expectancy = pd.read_csv(os.getenv('GAPMINDER_LIFE_EXPECTANCY'), index_col='Country', encoding='utf-8')
    population = pd.read_csv(os.getenv('GAPMINDER_POPULATION'), index_col='Country', encoding='utf-8')
    regions = pd.read_csv(os.getenv('GAPMINDER_REGIONS'), index_col='Country', encoding='utf-8')

    # Make the column names ints not strings for handling
    columns = list(fertility.columns)
    years = list(range(int(columns[0]), int(columns[-1])))
    rename_dict = dict(zip(columns, years))

    fertility = fertility.rename(columns=rename_dict)
    life_expectancy = life_expectancy.rename(columns=rename_dict)
    population = population.rename(columns=rename_dict)
    regions = regions.rename(columns=rename_dict)

    regions_list = list(regions.Group.unique())

    # Turn population into bubble sizes. Use min_size and factor to tweak.
    scale_factor = 200
    population_size = np.sqrt(population / np.pi) / scale_factor
    min_size = 3
    population_size = population_size.where(population_size >= min_size).fillna(min_size)

    return fertility, life_expectancy, population_size, regions, years, regions_list
