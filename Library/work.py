import pandas as pd
from pandas import DataFrame

data = DataFrame()
data_new = DataFrame()
suffer = DataFrame()
path_one = ""
path_second = ""


def load_dataframe(db_city_path, db_town_path):
    global data, path_one, path_second, suffer
    path_one = db_city_path
    path_second = db_town_path
    data = pd.read_csv(path_one)
    data_new = pd.read_csv(path_second)
    suffer = pd.merge(data, data_new, on='Key', how='left')


def get_records():
    return [el[1:] for el in suffer.iloc[:, 1:].itertuples()]


def _save_dataframe():
    suffer.iloc[:, :4].to_csv(path_one, index=False)
    suffer[['Key', 'Federal_subject', 'Population_area']].drop_duplicates(subset=['Key'],
                                                                          keep='first').to_csv(path_second, index=False)


def insert_record(record):
    global suffer

    f = suffer[suffer.Town == record['Town']]
    k = suffer[suffer.Federal_subject == record['Federal_subject']]
    try:
        if list(f.Town)[0] == record['Town']:
            for key, value in record.items():
                suffer.replace(list(f[key])[0], value, inplace=True)

                suffer.Population_area.replace(list(k.Population_area)[0], record['Population_area'], inplace=True)
    except IndexError:
        try:
            if list(k.Federal_subject)[0] == record['Federal_subject']:
                record['Key'] = list(k.Key)[0]
                merged = suffer.append(record, ignore_index=True)
                merged.Population_area.replace(list(k.Population_area)[0], record['Population_area'], inplace=True)
        except IndexError:
            record['Key'] = suffer['Key'][pd.Series(suffer['Key']).idxmax()] + 1
            suffer = suffer.append(record, ignore_index=True)


def delete_record(index):
    global suffer
    suffer = suffer.drop(index).reset_index(drop=True)


def update_record(index, record_list):
    data.iloc[index] = record_list


def research():
    zero = suffer['Town'][pd.Series(suffer['Founded']).idxmax()]
    one = suffer.Founded.max()
    two = suffer['Town'][pd.Series(suffer['Founded']).idxmin()]
    three = suffer.Founded.min()
    four = suffer['Federal_subject'][pd.Series(suffer['Population_area']).idxmax()]
    five = suffer.Population_area.max()
    six = suffer['Federal_subject'][pd.Series(suffer['Population_area']).idxmin()]
    seven = suffer.Population_area.min()
    eight = suffer['Federal_subject'][pd.Series(suffer['Population']).idxmax()]
    nine = suffer.Population.max()
    ten = suffer['Federal_subject'][pd.Series(suffer['Population']).idxmin()]
    eleven = suffer.Population.min()

    pulpy = """
    Самый молодой город : {0}, основан: {1}
    Самый древний город: {2}, основан: {3} 
    Самая многонаселенная область: {4}, численность: {5} 
    Самая малонаселенная область: {6}, численность: {7}
    Самый многонаселенный город: {8}, численность: {9}
    Самый малонаселенный город: {10}, численность: {11}"""
    pulpy = pulpy.format(zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven)
    return pulpy
