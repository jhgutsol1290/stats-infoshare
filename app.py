from infoshare_stats_class import Stats_Infoshare

if __name__ == "__main__":
    root_user = str(input('Ingresa Ruta: '))
    year_user = int(input('Año a buscar: '))
    month_user = int(input('Mes a buscar en número: '))
    print('Iniciando búsqueda')
    print('-'*80)
    stats = Stats_Infoshare()
    get_data = stats.get_stats_in_csv(root_user, year_user, month_user)
    stats_data = stats.count_stats()
    plot_data = stats.plot_stats(stats_data)
    count_total = stats_data[0] + stats_data[1] + stats_data[2] + stats_data[3] + stats_data[4]
    print(f'Total MP4 -> {stats_data[0]}\nTotal PDF -> {stats_data[1]}\nTotal PNG -> {stats_data[2]}\nTotal JPG -> {stats_data[3]}\nTotal GIF -> {stats_data[4]}\nTotal archivos ----> {count_total}')
    print('-'*80)
    print('Búsqueda finalizada, archivo creado')