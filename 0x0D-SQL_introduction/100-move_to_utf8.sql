-- script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTERET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTERET utf8mb4 COLLATE utf8mb4_unicode_ci;
