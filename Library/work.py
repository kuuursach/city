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
    data.iloc[:, :4].to_csv(path_one, index=False)
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
    #_save_dataframe()


def delete_record(index):
    global suffer
    suffer = suffer.drop(index).reset_index(drop=True)
   # _save_dataframe()


def update_record(index, record_list):
    data.iloc[index] = record_list
#    _save_dataframe()
