# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

##################################################
# Migration erstellen
# - Aus Verzeichnis 01 Python
# python3 manage.py makemigrations ki_energie
# python3 manage.py migrate ki_energie
##################################################

from ctypes.wintypes import LANGID
from ipaddress import ip_address
from pickle import TRUE
from re import S
from django.db import models
from django.urls import reverse
from django.contrib.gis.db import models


class AuwStatkurven(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    id_messwert_1 = models.BigIntegerField(
        db_column='id_Messwert_1', blank=True, null=True)
    # Field name made lowercase.
    id_messwert_2 = models.BigIntegerField(
        db_column='id_Messwert_2', blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    wert_num_1 = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    wert_num_2 = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    wert_diff = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    phase = models.CharField(max_length=20, blank=True, null=True)
    log_date = models.DateTimeField(blank=True, null=True)

    # class Meta:
    #    managed = True
    #    app_label = 'ki_energie'
    #    db_table = 'AUW_StatKurven'


class Geraete(models.Model):
    use_in_migrations = True
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    geraete_name = models.CharField(max_length=50, blank=True, null=True)
    geraete_art = models.CharField(max_length=50, blank=True, null=True)
    dns_name = models.CharField(max_length=60, blank=True, null=True)
    seriennummer = models.CharField(max_length=50, blank=True, null=True)
    hw_hersteller = models.CharField(max_length=50, blank=True, null=True)
    hw_version = models.CharField(max_length=35, blank=True, null=True)
    sw_version = models.CharField(max_length=35, blank=True, null=True)
    connection = models.CharField(max_length=200, blank=True, null=True)
    ip_address = models.CharField(max_length=30, blank=True, null=True)
    ip_port = models.CharField(max_length=5, blank=True, null=True)
    get_request = models.CharField(max_length=300, blank=True, null=True)
    put_request = models.CharField(max_length=300, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # Kommentarfeld
    log_datum_vom = models.DateTimeField(blank=True, null=True)


# class Geraete2(models.Model):
#    use_in_migrations = True
#
#    geraete_id = models.AutoField(db_column='geraete_Id', primary_key=True)  # Field name made lowercase.
#    geraete_name = models.CharField(max_length=50, blank=True, null=True)
#    geraete_art = models.CharField(max_length=50, blank=True, null=True)
#    dns_name = models.CharField(max_length=60, blank=True, null=True)
#    seriennummer = models.CharField(max_length=50, blank=True, null=True)
#    hw_version = models.CharField(max_length=35, blank=True, null=True)
#    sw_version = models.CharField(max_length=35, blank=True, null=True)
#    bemerkung = models.CharField(max_length=100, blank=True, null=True)
#    log_erzeugt_am = models.DateTimeField(blank=True, null=True)
#    log_letzte_aenderung_am = models.DateTimeField(blank=True, null=True)


class Geraete2Kunde(models.Model):
    use_in_migrations = True
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    geraete_id = models.IntegerField(
        db_column='geraete_Id', blank=True, null=True)
    # Field name made lowercase.
    kunde_id = models.IntegerField(db_column='kunde_Id', blank=True, null=True)
    raum = models.CharField(max_length=50, blank=True, null=True)
    bemerkung = models.CharField(max_length=100, blank=True, null=True)
    log_erzeugt_am = models.DateTimeField(blank=True, null=True)
    log_letzte_aenderung_am = models.DateTimeField(blank=True, null=True)


class ImportMesswerte(models.Model):

    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    log_datum_vom = models.DateTimeField(blank=True, null=True)
    server_name = models.CharField(max_length=20, blank=True, null=True)
    etage = models.CharField(max_length=50, blank=True, null=True)
    raum = models.CharField(max_length=50, blank=True, null=True)
    geraete_name = models.CharField(max_length=50, blank=True, null=True)
    name_des_wertes = models.CharField(max_length=50, blank=True, null=True)
    wert_num = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # This field type is a guess.
    wert_bit = models.TextField(blank=True, null=True)
    wert_str = models.CharField(max_length=50, blank=True, null=True)
    sensorklasse = models.CharField(max_length=20, blank=True, null=True)
    name_sensorklasse = models.CharField(max_length=20, blank=True, null=True)
    log_eingelesen_am = models.DateTimeField(blank=True, null=True)


class ImportboxFehlerlog(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    server_name = models.CharField(max_length=20, blank=True, null=True)
    datei = models.CharField(max_length=128, blank=True, null=True)
    fehlertext = models.CharField(max_length=128, blank=True, null=True)
    satznummer = models.IntegerField(blank=True, null=True)
    datensatz = models.CharField(max_length=2000, blank=True, null=True)
    log_eingelesen_am = models.DateTimeField(blank=True, null=True)


class KiParams(models.Model):
    use_in_migrations = True
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    group = models.CharField(max_length=50, blank=True, null=True)
    subgroup = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    val_int = models.IntegerField(blank=True, null=True)
    val_dec = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True)
    val_string = models.CharField(max_length=45, blank=True, null=True)
    log_date = models.DateTimeField(blank=True, null=True)


class KiRgActor(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    geraete_id = models.BigIntegerField(blank=True, null=True)
    typen_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    gewerk_id = models.BigIntegerField(blank=True, null=True)
    raum_id = models.BigIntegerField(blank=True, null=True)
    montageort = models.CharField(max_length=100, blank=True, null=True)
    default_wert = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    log_date = models.DateTimeField(blank=True, null=True)
    # Field name made lowercase.
    isactive = models.IntegerField(db_column='isActive', blank=True, null=True)
    loop_time = models.CharField(max_length=45, blank=True, null=True)


class KiRgActorSensor(models.Model):
    use_in_migrations = True
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    aktor_id = models.BigIntegerField(blank=True, null=True)
    lfd = models.BigIntegerField(blank=True, null=True)
    sensor_id = models.BigIntegerField(blank=True, null=True)
    # Field name made lowercase.
    isactive = models.IntegerField(db_column='isActive', blank=True, null=True)
    log_date = models.DateTimeField(blank=True, null=True)


class KiRgData(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    sequence = models.BigIntegerField(blank=True, null=True)
    aktor_id = models.BigIntegerField(blank=True, null=True)
    learn_date = models.DateTimeField(blank=True, null=True)
    soll_val = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    sensor_val1 = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    sensor_val2 = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    sensor_val3 = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    sensor_val4 = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    sensor_val5 = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    aktor_val1 = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    aktor_val2 = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    correction_val = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    correction_from_id = models.IntegerField(blank=True, null=True)
    rating_old = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    rating_new = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    time_to_completion = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    reserve_val1 = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    reserve_val2 = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    reserve_val5 = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    log_date = models.DateTimeField(blank=True, null=True)


class KiRgGewerk(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    gewerk_name = models.CharField(max_length=100, blank=True, null=True)
    gewerk_ort = models.CharField(max_length=100, blank=True, null=True)
    gewerk_etage = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    log_date = models.DateTimeField(blank=True, null=True)


class KiRgSensor(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    geraete_id = models.BigIntegerField(blank=True, null=True)
    typen_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    gewerk_id = models.BigIntegerField(blank=True, null=True)
    raum_id = models.BigIntegerField(blank=True, null=True)
    montageort = models.CharField(max_length=100, blank=True, null=True)
    default_wert = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    log_date = models.DateTimeField(blank=True, null=True)


class KiRgTypen(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    typ_name = models.CharField(max_length=20, blank=True, null=True)
    einheit = models.CharField(max_length=20, blank=True, null=True)
    min_val = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    max_val = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    log_date = models.DateTimeField(blank=True, null=True)


class Raumliste(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True, default=0)
    # Verknüpfung mit Tabelle Kunde
    kunde_id = models.BigIntegerField(blank=True, null=True)
    raum = models.CharField(max_length=50, blank=True, null=True)
    beschreibung = models.CharField(max_length=100, blank=True, null=True)
    gebaeude_id = models.BigIntegerField(
        blank=True, null=True)  # Verknüpfung mit Tabelle Gebäude
    # Verknüpfung mit Tabelle Etage
    etage_id = models.BigIntegerField(blank=True, null=True)
    # Verknüpfung mit Tabelle Server
    server_id = models.BigIntegerField(blank=True, null=True)
    wunsch_temperatur = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    wunsch_luftfeuchte = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    groesse_qm = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    raumhoehe = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    anzahl_sensoren = models.SmallIntegerField(blank=True, null=True)
    nutzungsbeschreibung = models.CharField(
        max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # Kommentarfeld
    log_datum_vom = models.DateTimeField(blank=True, null=True)
    #log_erzeugt_am = models.DateTimeField(blank=True, null=True)
    #log_letzte_änderung_am = models.DateTimeField(blank=True, null=True)


class RaumlisteInd1(models.Model):
    use_in_migrations = True

    id = models.AutoField(db_column='Id', primary_key=True, default=0)
    server_name = models.CharField(max_length=20, blank=True, null=True)
    etage = models.CharField(max_length=50, blank=True, null=True)
    raum = models.CharField(max_length=50, blank=True, null=True)

    # class Meta:
    #    abstract = True
    #    ordering = ['server_name', 'etage', 'raum']
    #    db_table = 'ki_energie_raumliste'


class Adressen(models.Model):
    use_in_migrations = True

    vorname = models.CharField(max_length=50)
    nachname = models.CharField(max_length=50)
    strasse = models.CharField(max_length=200)
    land = models.CharField(max_length=100)
    plz = models.IntegerField()
    ort = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)  # Kommentarfeld
    log_datum_vom = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['nachname', 'vorname']

    def __str__(self):
        return self.nachname

    def get_absolute_url(self):
        return reverse("adress_detail", args=[str(self.id)])


class SensorValueTypes(models.Model):
    use_in_migrations = True

    id = models.AutoField(db_column='Id', primary_key=True)
    kategorie = models.CharField(
        max_length=1, blank=True, null=True)  # T, F, L, H
    # Temperatur, Feuchte, Leistung, Helligkeit
    kategorie_name = models.CharField(max_length=50, blank=True, null=True)
    sub_kategorie = models.CharField(
        max_length=1, blank=True, null=True)  # Vorlauf, Rücklauf, Raum,
    # Temperatur, Feuchte, Leistung, Helligkeit
    sub_kategorie_name = models.CharField(max_length=50, blank=True, null=True)
    soll_ist_value = models.CharField(
        max_length=1, blank=True, null=True)  # S, I
    inside_outside = models.CharField(
        max_length=1, blank=True, null=True)  # I, O
    # P(rimary), S(econdary)
    pri_sec = models.CharField(max_length=1, blank=True, null=True)
    medium = models.CharField(
        max_length=20, blank=True, null=True)  # Wasser, Luft, usw
    bemerkung = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # Kommentarfeld
    log_datum_vom = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['sub_kategorie', 'sub_kategorie_name']


class ErgAnalyse(models.Model):

    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Enthält die ID des Wertes aus ImportMesswerte
    messwert_id = models.BigIntegerField(blank=False, null=True)
    # Verknüpfung mit Tabelle Kunde
    kunde_id = models.BigIntegerField(blank=True, null=True)
    # Primär immer nach Raum sortiert, Raum aus raumliste
    server_id = models.BigIntegerField(blank=False, null=False)
    gebaeude_id = models.BigIntegerField(
        blank=True, null=True)  # Verknüpfung mit Tabelle Gebäude
    # Verknüpfung mit Tabelle Etage
    etage_id = models.BigIntegerField(blank=True, null=True)
    # Primär immer nach Raum sortiert, Raum aus raumliste
    raum_id = models.BigIntegerField(blank=False, null=False)
    # Fortlaufenden Nummerierung der Periode
    periode = models.BigIntegerField(blank=False, null=False)
    periode_typ = models.BigIntegerField(
        blank=False, null=False)  # typ aus Periodentyp
    von_date_time = models.DateTimeField(blank=False, null=True)  # Beginn
    bis_date_time = models.DateTimeField(blank=False, null=True)  # Ende
    geraete_id = models.BigIntegerField(
        blank=False, null=False)  # Id des verwendeten Gerätes
    wert_typ = models.BigIntegerField(
        blank=False, null=False)  # Typ aus kirgtypen
    tgt_val = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    min_val = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    max_val = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    rise_time = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    max_rise = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    min_rise = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # Wert von 1..10, 1 = Gut, 10 = Schlecht
    goodness = models.BigIntegerField(blank=False, null=False)
    # Gegenüberstellung zur optimalen Kennlinie
    optimum_percent = models.BigIntegerField(blank=False, null=False)
    log_datum_vom = models.DateTimeField(blank=True, null=True)


class Workparameter(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Application (z.Bsp. ki_energie, rpi usw.)
    app = models.CharField(max_length=50, blank=True, null=True)
    # Modulbezeichnung (z.Bsp. Analyse, Frontend, Backend, usw )
    modul = models.CharField(max_length=50, blank=True, null=True)
    # Hauotname, kann auch der Programmteil sein, uz. Bsp. ANA_ALL
    name = models.CharField(max_length=100, blank=True, null=True)
    # Untername z. Bsp. LAST_IMPORT_ID
    subname = models.CharField(max_length=100, blank=True, null=True)
    # 0=int, 1=String, 2=Decimal, 3=Text, 4=Datum, 5=Zeit 6=Datetime
    typ = models.BigIntegerField(blank=False, null=False)
    int_val = models.BigIntegerField(blank=False, null=True)
    str_val = models.CharField(max_length=256, blank=True, null=True)
    text_val = models.TextField(blank=True, null=True)
    date_val = models.DateField(null=True)
    time_val = models.TimeField(null=True)
    datetime_val = models.DateTimeField(null=True)
    comment = models.TextField()  # Kommentarfeld
    log_datum_vom = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['app', 'modul', 'name', 'subname']

# Stammdatentabellen
# Server
#   Typ, Seriennummer, Kunde, Gebäude, Etage, Ausstattung


class Server(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Server Name  (z.Bsp. PI0001)
    name = models.CharField(max_length=50, blank=True, null=True)
    # Verknüpfung mit Tabelle Kunde
    kunde_id = models.BigIntegerField(blank=True, null=True)
    gebaeude_id = models.BigIntegerField(
        blank=True, null=True)  # Verknüpfung mit Tabelle Gebäude
    # Verknüpfung mit Tabelle Etage
    etage_id = models.BigIntegerField(blank=True, null=True)
    # Verknüpfung mit Tabelle Raum
    raum_id = models.BigIntegerField(blank=True, null=True)
    # Wo steht der Server  (z.Bsp. Schrank 1, Fach 4)
    montageort = models.CharField(max_length=200, blank=True, null=True)
    serial_nbr = models.CharField(
        max_length=50, blank=True, null=True)  # Seriennummer des Servers
    # 4B, WLAN, 2GB usw.
    hw_version = models.CharField(max_length=200, blank=True, null=True)
    # Operating System (Typ, Version usw.
    os_system = models.CharField(max_length=200, blank=True, null=True)
    os_version = models.CharField(
        max_length=50, blank=True, null=True)  # Version Operating System
    last_update = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # Kommentarfeld
    log_datum_vom = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['name']


# Gebäude
class Gebaeude(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Gebäudebezeichnung / Kennung
    name = models.CharField(max_length=50, blank=True, null=True)
    adress_id = models.BigIntegerField(
        blank=True, null=True)  # Verknüpfung mit Adressen
    comment = models.TextField(blank=True, null=True)  # Kommentarfeld
    log_datum_vom = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['name']

# Etagen


class Etage(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Etage Nr, in besonderen Fällen auch ein Name)
    name = models.CharField(max_length=50, blank=True, null=True)
    gebaeude_id = models.BigIntegerField(
        blank=True, null=True)  # Verknüpfung mit Tabelle Gebäude
    comment = models.TextField(blank=True, null=True)  # Kommentarfeld
    log_datum_vom = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['name']

# Adressen


class Adressen(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    strasse = models.CharField(max_length=200, blank=True, null=True)
    hausnummer = models.CharField(max_length=10, blank=True, null=True)
    postleitzahl = models.CharField(max_length=10, blank=True, null=True)
    iso_land = models.CharField(max_length=5, blank=True, null=True)
    land = models.CharField(max_length=200, blank=True, null=True)
    ort = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # Kommentarfeld
    festnetz = models.CharField(max_length=60, blank=True, null=True)
    faxnummer = models.CharField(max_length=60, blank=True, null=True)
    mobil = models.CharField(max_length=60, blank=True, null=True)
    mail = models.CharField(max_length=128, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # Kommentarfeld
    log_datum_vom = models.DateTimeField(blank=True, null=True)


# Kunden
class Kunde(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Verknüpfung it Tabelle Adressen
    adress_id = models.BigIntegerField(blank=True, null=True)
    anrede = models.CharField(max_length=5, blank=True, null=True)
    titel = models.CharField(max_length=20, blank=True, null=True)
    vorname = models.CharField(max_length=60, blank=True, null=True)
    nachname = models.CharField(max_length=60, blank=True, null=True)
    anmeldename = models.CharField(max_length=20, blank=True, null=True)
    passwort = models.CharField(max_length=60, blank=True, null=True)
    # This field type is a guess.
    anmeldung_aktiv = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # Kommentarfeld
    kunde_anlage = models.DateTimeField(blank=True, null=True)
    comments_id = models.BigIntegerField(
        blank=True, null=True)  # Verknüpfung mit Tabelle Status
    log_datum_vom = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['nachname', 'vorname']


# Freitexttabelle / Statusinfo
class Status(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='id', primary_key=True)
    # Name der Tabelle, z.Bsp. "Kunden" "Adresssen" "Server" usw.)
    ext_typ = models.CharField(max_length=20, blank=True, null=True)
    # externe id (z. Bps. Kunde, Adresse, Server etc.)
    ext_id = models.BigIntegerField(blank=True, null=True)
    # Laufende Nummer innerhalb der etx_id
    ext_lfd = models.BigIntegerField(blank=True, null=True)
    # CRT = Anlage, FR1 = Freigabe, DEL = Löschung, AEN = Aenderung
    stat_typ = models.CharField(max_length=5, blank=True, null=True)
    stat_text = models.TextField(blank=True, null=True)  # Freitext
    log_datum_vom = models.DateTimeField(blank=True, null=True)


# Anmerkungen / Fehler / Behebungen / Wünsche / Kommunikation / Telefonate
class Kommentar(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='id', primary_key=True)
    # Name der Tabelle, z.Bsp. "Kunden" "Adresssen" "Server" usw.)
    ext_typ = models.CharField(max_length=20, blank=True, null=True)
    # externe id (z. Bps. Kunde, Adresse, Server etc.)
    ext_id = models.BigIntegerField(blank=True, null=True)
    ext_lfd = models.BigIntegerField(blank=True, null=True)  # Laufende Nummer
    text = models.TextField(blank=True, null=True)  # Kommentar
    log_datum_vom = models.DateTimeField(blank=True, null=True)


# Dokumentenablage
# PDF's etc. anhängen zu Kunde, Server. Ablage im Verzeichnis, Dateiname
class Dokumente(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='id', primary_key=True)
    # Dokumententyp (Angebot, Mail, Auftrag, Rechnung, sonstige, Anmerkung )
    dok_typ = models.CharField(max_length=20, blank=True, null=True)
    # externe id (z. Bps. Kunde, Adresse, Server etc.)
    dok_id = models.BigIntegerField(blank=True, null=True)
    dok_lfd = models.BigIntegerField(blank=True, null=True)  # Laufende Nummer
    pfad = models.CharField(max_length=500, blank=False,
                            null=False)  # Pfad wo die Datei liegt
    name = models.TextField(max_length=128, blank=False,
                            null=False)  # Name der Datei
    log_datum_vom = models.DateTimeField(blank=True, null=True)


# Software
# welche Software und Schnittstellen und Version auf welchem Server / WLAN / enthernet / externen Zugriff
# Besonderheiten

# Raumliste über ID verknüpfen

# Preise

# Angebote

# Aufträge

# Rechnungen

# Erweiterungen ab 01.03.2023

# ab hier alle Tabelle für die Stammdaten -> sta_xxx
# ------------------------------------------------------------------------------------

class sta_lieferanten(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
 # heir fehlen noch Felder
    log_datum_erfasst = models.DateTimeField(blank=True, null=True)
    log_datum_ltz_aend = models.DateTimeField(blank=True, null=True)
    log_user = models.CharField(max_length=20, blank=True, null=True)


# ab hier alle Tabellen für die Messungen -> mst_xxx
# ------------------------------------------------------------------------------------

class mst_messtelle(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='id', primary_key=True)
    zaehler_nr = models.CharField(max_length=20, blank=True, null=True)
    # evtl. als Fremdschlüssel Registerwert
    zaehler_typ = models.CharField(max_length=20, blank=True, null=True)
    # evtl. als Fremdschlüssel Registerwert
    zaehler_einheit = models.BigIntegerField(blank=True, null=True)
    zaehler_name = models.TextField(
        max_length=128, blank=False, null=False)  # Name des Zählers
    log_datum_erfasst = models.DateTimeField(blank=True, null=True)
    log_datum_ltz_aend = models.DateTimeField(blank=True, null=True)
    log_user = models.CharField(max_length=20, blank=True, null=True)


class mst_tarife(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='id', primary_key=True)
    sta_lieferant_id = models.BigIntegerField(blank=True, null=True)
    tarif_typ = models.CharField(max_length=20, blank=True, null=True)
    tarif_preis = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    tarif_von = models.DateTimeField(blank=False, null=False)
    tarif_bis = models.DateTimeField(blank=False, null=False)
    log_datum_erfasst = models.DateTimeField(blank=True, null=True)
    log_datum_ltz_aend = models.DateTimeField(blank=True, null=True)
    log_user = models.CharField(max_length=20, blank=True, null=True)


class mst_messwerte(models.Model):
    use_in_migrations = True

    # Field name made lowercase.
    id = models.AutoField(db_column='id', primary_key=True)
    mst_messteile_id = models.BigIntegerField(blank=True, null=True)
    sta_lieferant_id = models.BigIntegerField(blank=True, null=True)
    messwert = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    quelle_messwert = models.CharField(max_length=128, blank=True, null=True)
    log_datum_erfasst = models.DateTimeField(blank=True, null=True)
    log_datum_ltz_aend = models.DateTimeField(blank=True, null=True)
    log_user = models.CharField(max_length=20, blank=True, null=True)
