USE boards_test;

CREATE TABLE BoardGames (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(80),
    `rank` INT,
    rating DECIMAL(3,2),
    complexity DECIMAL(3,2),
    max_players TINYINT,
    style VARCHAR(40),
    PRIMARY KEY (id)
);
