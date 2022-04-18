# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuwStatkurven(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    id_messwert_1 = models.BigIntegerField(db_column='id_Messwert_1', blank=True, null=True)  # Field name made lowercase.
    id_messwert_2 = models.BigIntegerField(db_column='id_Messwert_2', blank=True, null=True)  # Field name made lowercase.
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    wert_num_1 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    wert_num_2 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    wert_diff = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    phase = models.CharField(max_length=20, blank=True, null=True)
    log_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AUW_StatKurven'


class Geraete(models.Model):
    geraete_id = models.AutoField(db_column='geraete_Id', primary_key=True)  # Field name made lowercase.
    geraete_name = models.CharField(max_length=50, blank=True, null=True)
    geraete_art = models.CharField(max_length=50, blank=True, null=True)
    dns_name = models.CharField(max_length=60, blank=True, null=True)
    seriennummer = models.CharField(max_length=50, blank=True, null=True)
    hw_version = models.CharField(max_length=35, blank=True, null=True)
    sw_version = models.CharField(max_length=35, blank=True, null=True)
    bemerkung = models.CharField(max_length=100, blank=True, null=True)
    log_erzeugt_am = models.DateTimeField(blank=True, null=True)
    log_letzte_aenderung_am = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geraete'


class Geraete2Kunde(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    geraete_id = models.IntegerField(db_column='geraete_Id', blank=True, null=True)  # Field name made lowercase.
    kunde_id = models.IntegerField(db_column='kunde_Id', blank=True, null=True)  # Field name made lowercase.
    raum = models.CharField(max_length=50, blank=True, null=True)
    bemerkung = models.CharField(max_length=100, blank=True, null=True)
    log_erzeugt_am = models.DateTimeField(blank=True, null=True)
    log_letzte_aenderung_am = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geraete2kunde'


class ImportMesswerte(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    log_datum_vom = models.DateTimeField(blank=True, null=True)
    server_name = models.CharField(max_length=20, blank=True, null=True)
    etage = models.CharField(max_length=50, blank=True, null=True)
    raum = models.CharField(max_length=50, blank=True, null=True)
    geraete_name = models.CharField(max_length=50, blank=True, null=True)
    name_des_wertes = models.CharField(max_length=50, blank=True, null=True)
    wert_num = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    wert_bit = models.TextField(blank=True, null=True)  # This field type is a guess.
    wert_str = models.CharField(max_length=50, blank=True, null=True)
    sensorklasse = models.CharField(max_length=20, blank=True, null=True)
    name_sensorklasse = models.CharField(max_length=20, blank=True, null=True)
    log_eingelesen_am = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_messwerte'


class ImportboxFehlerlog(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    server_name = models.CharField(max_length=20, blank=True, null=True)
    datei = models.CharField(max_length=128, blank=True, null=True)
    fehlertext = models.CharField(max_length=128, blank=True, null=True)
    satznummer = models.IntegerField(blank=True, null=True)
    datensatz = models.CharField(max_length=2000, blank=True, null=True)
    log_eingelesen_am = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'importbox_fehlerlog'


class KiRgActor(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    geraete_id = models.BigIntegerField(blank=True, null=True)
    typen_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    gewerk_id = models.BigIntegerField(blank=True, null=True)
    raum_id = models.BigIntegerField(blank=True, null=True)
    montageort = models.CharField(max_length=100, blank=True, null=True)
    default_wert = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    log_date = models.DateTimeField(blank=True, null=True)
    isactive = models.IntegerField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ki_rg_actor'


class KiRgActorSensor(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    aktor_id = models.BigIntegerField(blank=True, null=True)
    lfd = models.BigIntegerField(blank=True, null=True)
    sensor_id = models.BigIntegerField(blank=True, null=True)
    isactive = models.IntegerField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    log_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ki_rg_actor_sensor'


class KiRgData(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sequence = models.BigIntegerField(blank=True, null=True)
    aktor_id = models.BigIntegerField(blank=True, null=True)
    learn_date = models.DateTimeField(blank=True, null=True)
    soll_val = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    sensor_val1 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    sensor_val2 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    sensor_val3 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    sensor_val4 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    sensor_val5 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    regler_val1 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    regler_val2 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    regler_val3 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    regler_val4 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    regler_val5 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    aktor_val1 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    aktor_val2 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    aktor_val3 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    aktor_val4 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    aktor_val5 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    log_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ki_rg_data'


class KiRgGewerk(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    gewerk_name = models.CharField(max_length=100, blank=True, null=True)
    gewerk_ort = models.CharField(max_length=100, blank=True, null=True)
    gewerk_etage = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    log_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ki_rg_gewerk'


class KiRgSensor(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    geraete_id = models.BigIntegerField(blank=True, null=True)
    typen_id = models.BigIntegerField(blank=True, null=True)
    name = models.DateTimeField(blank=True, null=True)
    gewerk_id = models.BigIntegerField(blank=True, null=True)
    raum_id = models.BigIntegerField(blank=True, null=True)
    montageort = models.CharField(max_length=100, blank=True, null=True)
    default_wert = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    log_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ki_rg_sensor'


class KiRgTypen(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    typ_name = models.CharField(max_length=20, blank=True, null=True)
    einheit = models.CharField(max_length=20, blank=True, null=True)
    min_val = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    max_val = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    log_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ki_rg_typen'


class Kunde(models.Model):
    kunde_id = models.AutoField(db_column='kunde_Id', primary_key=True)  # Field name made lowercase.
    anrede = models.CharField(max_length=5, blank=True, null=True)
    titel = models.CharField(max_length=20, blank=True, null=True)
    vorname = models.CharField(max_length=60, blank=True, null=True)
    nachname = models.CharField(max_length=60, blank=True, null=True)
    plz = models.CharField(max_length=5, blank=True, null=True)
    ort = models.CharField(max_length=50, blank=True, null=True)
    strasse = models.CharField(max_length=50, blank=True, null=True)
    hausnummer = models.CharField(max_length=6, blank=True, null=True)
    festnetz = models.CharField(max_length=60, blank=True, null=True)
    faxnummer = models.CharField(max_length=60, blank=True, null=True)
    mobil = models.CharField(max_length=60, blank=True, null=True)
    mail = models.CharField(max_length=128, blank=True, null=True)
    anmeldename = models.CharField(max_length=20, blank=True, null=True)
    passwort = models.CharField(max_length=60, blank=True, null=True)
    anmeldung_aktiv = models.TextField(blank=True, null=True)  # This field type is a guess.
    bemerkung = models.CharField(max_length=100, blank=True, null=True)
    log_erzeugt_am = models.DateTimeField(blank=True, null=True)
    log_letzte_änderung_am = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kunde'


class Raumliste(models.Model):
    raum_id = models.AutoField(db_column='raum_Id', primary_key=True)  # Field name made lowercase.
    server_name = models.CharField(max_length=20, blank=True, null=True)
    etage = models.CharField(max_length=50, blank=True, null=True)
    raum = models.CharField(max_length=50, blank=True, null=True)
    beschreibung = models.CharField(max_length=100, blank=True, null=True)
    wunsch_temperatur = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    wunsch_luftfeuchte = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    groesse_qm = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    raumhoehe = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    anzahl_sensoren = models.SmallIntegerField(blank=True, null=True)
    nutzungsbeschreibung = models.CharField(max_length=100, blank=True, null=True)
    log_erzeugt_am = models.DateTimeField(blank=True, null=True)
    log_letzte_änderung_am = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raumliste'