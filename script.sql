CREATE DATABASE `net-hw2` CHARACTER SET utf8 COLLATE utf8_general_ci;

GRANT ALL PRIVILEGES ON `net-hw2` TO 'dbuser'@'localhost';

use net-hw2;

CREATE TABLE notifications
(
    ID     int          NOT NULL AUTO_INCREMENT,
    vk_id  varchar(20)  NOT NULL,
    date   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    msg    varchar(255) NOT NULL,
    status varchar(20)  NOT NULL DEFAULT 'pending',
    PRIMARY KEY (ID)
);

INSERT INTO notifications (vk_id, date, msg)
VALUES ('242217382', '2022-12-04 20:00:00', 'У вас неоплаченная налоговая задолженность'),
       ('242217382', '2022-12-05 20:00:00', 'У вас новый штраф! Оплатите в течение 5 дней'),
       ('242217382', '2022-12-06 20:00:00', 'Ваш загранпаспорт готов к выдаче'),
       ('242217382', '2022-12-07 20:00:00', 'Открыта запись на ДЭГ в 2022 году'),
       ('242217382', '2022-12-08 20:00:00', 'Узнайте, как получить субсидию на ремонт');

-- execute after demo to restore the initial state
UPDATE notifications SET status = "pending";
