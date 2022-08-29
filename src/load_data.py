import tomli
import pandas as pd
from dateutil.parser import parse

class LoadData():

    def load_config(self, config_name:str):
        with open(f"config/config.{config_name}.toml", mode="rb") as fp:
            file_config = tomli.load(fp)
        return file_config

    def load_data(self, config_name:str):
        params_csv = self.load_config(config_name)
        path_file = params_csv["file"].get("path")

        dtype = {}
        converters =  {}
        fields = params_csv["fields"]
        for key in fields:
            if fields[key]["type"] == "date":
                converters[key] = lambda x: parse(x)
            else:
                dtype[key] = fields[key]["type"]

        df = pd.read_csv(path_file, dtype=dtype, converters=converters) 
        return df

    def search_data(self, data_source, col_source, data_destinatoin, col_destination):
        df = pd.DataFrame()
        for col in data_source[col_source]:
            row = data_destinatoin[col_destination].str.contains(col)
            if any(row):
                df_int = data_destinatoin.loc[row].copy()
                df_int[col_source] = col
                df = pd.concat([df,df_int])
        return df
