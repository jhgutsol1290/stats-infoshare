import os, os.path, time
from datetime import datetime
from dateutil.parser import parse
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

class Stats_Infoshare():
    def __init__(self, list_files = [], dirs = []):
        self.list_files = []
        self.dirs = []

    def get_stats_in_csv(self, root_user, year_user, month_user):
        try:
            self.dirs = os.listdir(root_user)
            for file in self.dirs:
                data = '\\' + file
                new_date = parse(time.ctime(os.path.getctime(root_user + data)))
                name, ext = os.path.splitext(file)
                if new_date.year == year_user:
                    if new_date.month == month_user:
                        self.list_files.append([file, new_date, ext])
            df = pd.DataFrame(self.list_files, columns = ['nombre', 'fecha_de_creacion', 'tipo'])
            df.to_csv(f'output_file_{month_user}_{year_user}.csv', encoding='utf-8-sig')
            return True
        except Exception as e:
            print('¡¡¡¡Algo malo ocurrió en la búsqueda!!!!, ->', str(e))
    
    def count_stats(self):
        try:
            count_mp4 = len([element[2] for element in self.list_files if element[2] == '.mp4'])
            count_pdf = len([element[2] for element in self.list_files if element[2] == '.pdf'])
            count_png = len([element[2] for element in self.list_files if element[2] == '.png'])
            count_jpg = len([element[2] for element in self.list_files if element[2] == '.jpg'])
            count_gif = len([element[2] for element in self.list_files if element[2] == '.gif'])       
            return [count_mp4, count_pdf, count_png, count_jpg, count_gif]
        except Exception as e:
            print('¡¡¡¡Algo malo ocurrió en el conteo!!!!, ->', str(e))
    
    def plot_stats(self, stats_data):
        try:
            names = ['MP4', 'PDF', 'PNG', 'JPG', 'GIF']
            values = stats_data
            plt.figure(figsize=(16,4))
            plt.subplot(131)
            plt.bar(names, values)
            plt.suptitle('Total')
            return plt.show()
        except Exception as e:
            print('¡¡¡¡Algo malo ocurrió en el proceso de graficación!!!!, ->', str(e))