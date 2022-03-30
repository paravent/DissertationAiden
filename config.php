<?php
/* Database credentials. Assuming we are running MySQL
server with default setting (user 'root' with no password) */
define('DB_SERVER', 'localhost:8080');
define('DB_USERNAME', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'diss');
 
/* Attempt to connect to MySQL database */
$link = mysqli_connect('localhost', 'root', '', 'diss');
 
// Check connection
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
?>