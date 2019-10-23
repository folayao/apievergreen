CREATE TABLE tipo_sensores (
    fecha DATETIME PRIMARY KEY,
    origen VARCHAR (200) ,
    valor varchar(20) NOT NULL,
    codigoSensor INTEGER(150) NOT NULL,
    observacion VARCHAR(100)
)

-- datetime format: YYYY-MM-DD HH:MM:SS.ffffff
