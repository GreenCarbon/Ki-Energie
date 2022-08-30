from datetime import *

# from ki_energie.models import ImportboxFehlerlog
# from ki_energie.models import ImportMesswerte
from ki_energie.models import ErgAnalyse


class grafiken():

    def graf_erzeugen(p_server, p_etage, p_raum, p_sensorklasse, p_wert, p_datum_von, p_datum_bis):

        # try:

        print('ich bin zurück, hier die Werte: ' + str(p_server) + ' | '
              + str(p_etage) + ' | '
              + str(p_raum) + ' | '
              + str(p_sensorklasse) + ' | '
              + str(p_wert) + ' | '
              + str(p_datum_von) + ' | '
              + str(p_datum_bis)
              )

        qs_ergebnis = ErgAnalyse.objects.filter(raum_id=p_raum)
        print(qs_ergebnis)

    #     sql_time_min = time.min.__str__()
    #     sql_datum_von = p_datum_von + ' ' + sql_time_min
    #     plus_1tag = timedelta(1)
    #     dat_datum_bis = datetime.strptime(p_datum_bis, "%Y-%m-%d")
    #     sql_datum_bis = dat_datum_bis + plus_1tag
    #     sql_anweisung = """SELECT * FROM ki_energie_importmesswerte
    #                     WHERE server_name = %s AND etage = %s AND raum = %s AND sensorklasse = %s AND name_des_wertes = %s
    #                           AND log_datum_vom >= DATE(%s) AND log_datum_vom < DATE(%s)
    #                     ORDER BY log_datum_vom"""
    #     sql_werte = (p_server_name, p_etage, p_raum, p_sensorklasse,
    #                  p_name_des_wertes, sql_datum_von, sql_datum_bis)

    #     cursor = con.cursor()
    #     cursor.execute(sql_anweisung, sql_werte)
    #     sql_ergebnis = cursor.fetchall()
    #     cursor.close()

    #     xwerte_init = []
    #     ywerte_init = []
    #     xwerte = []
    #     ywerte = []
    #     for daten in sql_ergebnis:
    #         xwerte_init = [daten[1]]
    #         xwerte.append(xwerte_init)
    #         ywerte_init = [daten[7]]
    #         ywerte.append(ywerte_init)

    # except mysql.connector.Error as error:
    #     fehler.set(
    #         "Fehler beim Lesen der Tabelle ki_energie_importmesswerte: {}".format(error))

    # fig = Figure(figsize=(7, 15), dpi=110)
    # plot1 = fig.add_subplot(1,1,1)

    # global m_datum_von
    # global m_datum_bis
    # if (m_datum_von != p_datum_von) or (m_datum_bis != p_datum_bis):
    #     m_datum_von = p_datum_von
    #     m_datum_bis = p_datum_bis
    # fig.clf()
    # plt.clf()
    # i_fenster.geometry('510x570+10+10')

    # i_fenster.geometry('1210x570+10+10')

    # rahmen1 = Frame(master=i_fenster, bg='magenta')
    # rahmen1.pack(side='right', padx='35')

    # dataPlot.clf()
    # dataPlot.plot(xwerte, ywerte)
    # dataPlot.set_xlabel('Zeit-Achse')
    # dataPlot.set_ylabel('Temperatur')

    # canvas = FigureCanvasTkAgg(fig, master=i_fenster)
    # canvas.draw()
    # canvas.get_tk_widget().pack(side='right', padx='35')

    # plt.plot(xwerte, ywerte) #, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
    # plt.step(xwerte, ywerte) #, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
    # plt.bar(xwerte, ywerte)
    # plt.xlabel('Zeit-Achse')
    # plt.ylabel('Temperatur')
    # s_grafik = aktuelle_zeit + '_' + p_server_name + '_' + p_etage + '_' + p_raum + '.png'
    # plt.figure()
    # plt.savefig(s_grafik)
    # plt.show()

    # n_grafik = ImageTk.PhotoImage(Image.open(x_grafik))
    # l_grafik .configure(image=n_grafik)
    # l_grafik.image = n_grafik
    # l_grafik.place(x=530, y=50)
    # ci_fenster.geometry('1210x570+10+10')

    # i_fenster.destroy()
# s_grafik
    # return
