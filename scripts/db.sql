-- CREATE DATABASE
create database flight_game;

-- USE DATABASE
use flight_game;

-- RUN DATABASE STRUCTURE SCRIPT
source scripts/assets/flight_game_database_script.sql;

-- CREATE TOURNAMENTS TABLE
CREATE TABLE tournaments (
    id INT NOT NULL AUTO_INCREMENT,
    week INT,
    month VARCHAR(40),
    day INT,
    points INT,
    name VARCHAR(100),
    surface VARCHAR(40),
    city VARCHAR(40),
    iso_country VARCHAR(40),
    continent VARCHAR(40),
    prize_money BIGINT,
    PRIMARY KEY (id),
    CONSTRAINT fk_country
        FOREIGN KEY (iso_country)
        REFERENCES country(iso_country)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- POPULATE TOURNAMENTS TABLE - 1ST PART
INSERT INTO tournaments (week, month, day, points, name, surface, city, iso_country, continent, prize_money) VALUES
(1, 'December', 30, 250, 'Brisbane International', 'Hard', 'Brisbane', 'AU', 'Oceania', 372500),
(1, 'December', 30, 250, 'Hong Kong Open', 'Hard', 'Hong Kong', 'HK', 'Asia', 398250),
(2, 'January', 6, 250, 'Auckland Open', 'Hard', 'Auckland', 'NZ', 'Oceania', 355500),
(2, 'January', 6, 250, 'Adelaide International', 'Hard', 'Adelaide', 'AU', 'Oceania', 766290),
(5, 'January', 27, 250, 'Open Sud de France', 'Hard', 'Montpellier', 'FR', 'Europe', 426605),
(6, 'February', 3, 500, 'Dallas Open', 'Hard', 'Dallas', 'US', 'North America', 2760000),
(6, 'February', 3, 500, 'Rotterdam Open', 'Hard', 'Rotterdam', 'NL', 'Europe', 1265495),
(7, 'February', 10, 250, 'Delray Beach Open', 'Hard', 'Delray Beach', 'US', 'North America', 442500),
(7, 'February', 10, 250, 'Open 13', 'Hard', 'Marseille', 'FR', 'Europe', 512750),
(7, 'February', 10, 250, 'Argentina Open', 'Clay', 'Buenos Aires', 'AR', 'South America', 475300),
(8, 'February', 17, 500, 'Rio Open', 'Clay', 'Rio de Janeiro', 'BR', 'South America', 1309770),
(8, 'February', 17, 500, 'Qatar Open', 'Hard', 'Doha', 'QA', 'Asia', 1024000),
(9, 'February', 24, 500, 'Mexican Open', 'Hard', 'Acapulco', 'MX', 'North America', 955000),
(9, 'February', 24, 500, 'Dubai Tennis Championships', 'Hard', 'Dubai', 'AE', 'Asia', 1619500),
(9, 'February', 24, 250, 'Chile Open', 'Clay', 'Santiago', 'CL', 'South America', 680140),
(10, 'March', 5, 1000, 'Indian Wells Masters', 'Hard', 'Indian Wells', 'US', 'North America', 4500000),
(12, 'March', 19, 1000, 'Miami Open', 'Hard', 'Miami Gardens', 'US', 'North America', 3645000),
(14, 'March', 31, 250, 'Romanian Open', 'Clay', 'Bucharest', 'RO', 'Europe', 596035),
(14, 'March', 31, 250, 'Grand Prix Hassan II', 'Clay', 'Marrakech', 'MA', 'Africa', 398250),
(14, 'March', 31, 250, 'US Men Clay Court Championship', 'Clay', 'Houston', 'US', 'North America', 442500),
(15, 'April', 6, 1000, 'Monte-Carlo Masters', 'Clay', 'Roquebrune-Cap-Martin', 'FR', 'Europe', 2451208),
(16, 'April', 14, 500, 'Barcelona Open', 'Clay', 'Barcelona', 'ES', 'Europe', 1705667),
(16, 'April', 14, 500, 'Bavaria Open', 'Clay', 'Munich', 'DE', 'Europe', 398250),
(17, 'April', 23, 1000, 'Madrid Open', 'Clay', 'Madrid', 'ES', 'Europe', 3119719),
(19, 'May', 7, 1000, 'Italian Open', 'Clay', 'Rome', 'IT', 'Europe', 2451208),
(21, 'May', 18, 500, 'German Open', 'Clay', 'Hamburg', 'DE', 'Europe', 1000000),
(21, 'May', 18, 250, 'Geneva Open', 'Clay', 'Geneva', 'CH', 'Europe', 501345),
(22, 'May', 25, 1000, 'Paris Masters', 'Hard', 'Paris', 'FR', 'Europe', 2451208),
(24, 'June', 9, 250, 'Rosmalen Open', 'Grass', 'Hertogenbosch', 'NL', 'Europe', 398250),
(24, 'June', 9, 250, 'Stuttgart Open', 'Grass', 'Stuttgart', 'DE', 'Europe', 398250),
(25, 'June', 16, 500, 'Halle Open', 'Grass', 'Halle', 'DE', 'Europe', 663750),
(25, 'June', 16, 500, 'Queen Club Championships', 'Grass', 'London', 'GB', 'Europe', 640000),
(26, 'June', 23, 250, 'Eastbourne International', 'Grass', 'Eastbourne', 'GB', 'Europe', 547265),
(26, 'June', 23, 250, 'Mallorca Open', 'Grass', 'Santa Ponsa', 'ES', 'Europe', 720000),
(29, 'July', 14, 250, 'Los Cabos Open', 'Hard', 'Los Cabos', 'MX', 'North America', 889890),
(29, 'July', 14, 250, 'Swedish Open', 'Clay', 'Båstad', 'SE', 'Europe', 398250),
(29, 'July', 14, 250, 'Swiss Open', 'Clay', 'Gstaad', 'CH', 'Europe', 398250),
(30, 'July', 20, 250, 'Croatia Open', 'Clay', 'Umag', 'HR', 'Europe', 398250),
(30, 'July', 20, 250, 'Austrian Open', 'Clay', 'Kitzbühel', 'AT', 'Europe', 586140),
(31, 'July', 27, 1000, 'Canadian Open', 'Hard', 'Toronto', 'CA', 'North America', 2430000),
(31, 'August', 3, 500, 'Washington Open', 'Hard', 'Washington, D.C.', 'US', 'North America', 1165500),
(32, 'August', 5, 1000, 'Cincinnati Masters', 'Hard', 'Mason', 'US', 'North America', 2430000),
(34, 'August', 17, 250, 'Winston-Salem Open', 'Hard', 'Winston-Salem', 'US', 'North America', 663750),
(38, 'September', 17, 250, 'Chengdu Open', 'Hard', 'Chengdu', 'CN', 'Asia', 1190210),
(38, 'September', 17, 250, 'Hangzhou Open', 'Hard', 'Hangzhou', 'CN', 'Asia', 1019185),
(39, 'September', 24, 500, 'Japan Open', 'Hard', 'Tokyo', 'JP', 'Asia', 1100000),
(39, 'September', 24, 500, 'China Open', 'Hard', 'Beijing', 'CN', 'Asia', 2100000),
(40, 'October', 1, 1000, 'Shanghai Masters', 'Hard', 'Shanghai', 'CN', 'Asia', 3240000),
(42, 'October', 13, 250, 'Stockholm Open', 'Hard', 'Stockholm', 'SE', 'Europe', 531000),
(42, 'October', 13, 250, 'European Open', 'Hard', 'Antwerp', 'BE', 'Europe', 725540),
(42, 'October', 13, 250, 'Almaty Open', 'Hard', 'Almaty', 'KZ', 'Asia', 1055255),
(43, 'October', 20, 500, 'Vienna Open', 'Hard', 'Vienna', 'AT', 'Europe', 575250),
(43, 'October', 20, 500, 'Swiss Indoors', 'Hard', 'Basel', 'CH', 'Europe', 1225000),
(45, 'November', 2, 250, 'Moselle Open', 'Hard', 'Metz', 'FR', 'Europe', 398250),
(45, 'November', 2, 250, 'Belgrade Open', 'Hard', 'Belgrade', 'RS', 'Europe', 766715),
(46, 'November', 10, 1000, 'ATP Finals', 'Hard', 'Turin', 'IT', 'Europe', 5700000);

-- POPULATE TOURNAMENTS TABLE - 1ST PART
INSERT INTO tournaments (week, month, day, points, name, surface, city, iso_country, continent, prize_money) VALUES
(3, 'January', 12, 2000, 'Australian Open', 'Hard', 'Melbourne', 'AU', 'Oceania', 3000000),
(21, 'May', 25, 2000, 'French Open', 'Clay', 'Paris', 'FR', 'Europe', 3000000),
(27, 'June', 30, 2000, 'Wimbledon', 'Grass', 'London', 'GB', 'Europe', 3000000),
(35, 'August', 25, 2000, 'US Open', 'Hard', 'New York City', 'US', 'North America', 3000000);

-- CREATE FOREIGN KEY TO COUNTRY TABLE
ALTER TABLE tournaments
ADD CONSTRAINT fk_tournaments_country -- Nombre único
FOREIGN KEY (iso_country)
REFERENCES country(iso_country)
ON DELETE CASCADE
ON UPDATE CASCADE;