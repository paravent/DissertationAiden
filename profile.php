<?php
require_once "pdo.php";
require_once "functions.php";
session_start();
$servername = "localhost";
$username = "root";
$password = "";
$tableName = "diss";
$mysqli = new mysqli($servername, $username, $password, $tableName);

$user = $_SESSION["username"]; 

$stmt = $pdo->prepare("SELECT userEmail FROM users WHERE userUsername LIKE '%$user%' LIMIT 1");
$stmt->execute(); 
$email = $stmt->fetch(PDO::FETCH_ASSOC); 

$UserTrendg = $pdo->prepare("SELECT userTrendGenre from users WHERE userUsername LIKE '%$user%'"); 
$UserTrendg->execute(); 
$UserTrendGenre = $UserTrendg->fetch(PDO::FETCH_ASSOC) ; 

$UserTrenda = $pdo->prepare("SELECT userTrendActor from users WHERE userUsername LIKE '%$user%'"); 
$UserTrenda->execute(); 
$UserTrendActor = $UserTrenda->fetch(PDO::FETCH_ASSOC) ;

$currentR = $pdo->prepare("SELECT userLiked from users WHERE userUsername LIKE '%$user%'"); 
$currentR->execute(); 
$currentRecommendPerUser = $currentR->fetch(PDO::FETCH_ASSOC) ;

$command = exec("python3 api_call.py '%$user%' "); 
ob_start();
passthru("/usr/local/bin/python3 api_call.py '%$user%' ");
$output = ob_get_clean(); 
shell_exec(" /usr/local/bin/python3 api_call.py '%$user%' ");

// exec($command);

// $command_test = escapeshellcmd("python3 api_call.py '%$username%' ");
// $output = shell_exec($command_test);

// echo $output; 
?>


<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Profile</title>
        <link rel="icon" type="image/x-icon" href="assets/img/favicon.ico" />
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>    
        <!-- Font Awesome icons (free version)-->
        <script src="https://use.fontawesome.com/releases/v5.15.1/js/all.js" crossorigin="anonymous"></script>
        <!-- JQUERY FILE -->
        <script
                src="https://code.jquery.com/jquery-1.11.2.min.js"
                integrity="sha256-Ls0pXSlb7AYs7evhd+VLnWsZ/AqEHcXBeMZUycz/CcA="
                crossorigin="anonymous"></script>
        <!-- JS file easy autocomplete -->
        <script src="jquery.easy-autocomplete.min.js"></script>
        <!-- CSS file -->
        <link rel="stylesheet" href="easy-autocomplete.min.css">
        <!-- Google fonts-->
        <link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaijaan+2:wght@500&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="cssMain/realStyle.css" rel="stylesheet" />
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

        

        <!-- bootstrap -->
    </head>

    <div class="home">
        <body>
        <!-- Navigation-->
            <div class="navbar-wrapper">
                <div class="container">
                    <nav class="navbar navbar-expand-lg navbar-light ">
                        <a class="navbar-brand" href="#">
                            <img src="dependables/sun.png" style="width: 50px;" alt="">
                        </a>
                        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                    
                        <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav mr-auto">
                            <li class="nav-item active">
                            <a class="nav-link colour-primary" href="index.php">Home</a>
                                </li>
                            <li class="nav-item">
                            <a class="nav-link colour-primary" href="wishlist.php">Wishlist</a>
                                </li>
                            
                        </ul>
                </div>
        </div>

        <div class="container">
    <div class="main-body">
   
          <div class="row gutters-sm">
            <div class="col-md-4 mb-3">
              <div class="card">
                <div class="card-body">
                  <div class="d-flex flex-column align-items-center text-center">
                    <img src="dependables/police.png" alt="Admin" class="rounded-circle" width="150">
                    <div class="mt-3">
                      <h4><?php echo htmlspecialchars($_SESSION["username"]); ?></h4>
                      <p class="text-secondary mb-1">Genius billionaire philanthropist</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-8">
              <div class="card mb-3">
                <div class="card-body">
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">username</h6>
                    </div>
                    <div class="col-sm-9 text-secondary">
                        <?php echo htmlspecialchars($_SESSION["username"]); ?>
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">Email</h6>
                    </div>
                    <div class="col-sm-9 text-secondary">
                      <?php print_r(implodeArrResult($email));  ?>
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">Favourite genres</h6>
                    </div>
                    <div class="col-sm-9 text-secondary">
                    <?php print_r(implodeArrResult($UserTrendGenre));  ?>
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">Favourite Actor(s)/Actress(es)</h6>
                    </div>
                    <div class="col-sm-9 text-secondary">
                    <?php print_r(implodeArrResult($UserTrendActor));  ?>
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">Current Recommendations from current popular releases</h6>
                    </div>
                    <div class="col-sm-9 text-secondary">
                    <?php print_r(implodeArrResult($currentRecommendPerUser));  ?>
                    </div>
                  </div>
                  <hr>
                  <div class="row">
                    <div class="col-sm-12">
                      <a>Current Recommendations from our system</a>
                    </div>
                  </div>
                  <hr>
                  
                </div>
              </div>

              <div class="row gutters-sm">
                <div class="col-sm-6 mb-3">
                  <div class="card h-100">
                    <div class="card-body">
                      <h6 class="d-flex align-items-center mb-3"><i class="material-icons text-info mr-2">Trending</i>Your media spread</h6>
                      <small>Comedy</small>
                      <div class="progress mb-3" style="height: 5px">
                        <div class="progress-bar bg-primary" role="progressbar" style="width: 80%" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"></div>
                      </div>
                      <small>Romance</small>
                      <div class="progress mb-3" style="height: 5px">
                        <div class="progress-bar bg-primary" role="progressbar" style="width: 72%" aria-valuenow="72" aria-valuemin="0" aria-valuemax="100"></div>
                      </div>
                      <small>Horror</small>
                      <div class="progress mb-3" style="height: 5px">
                        <div class="progress-bar bg-primary" role="progressbar" style="width: 89%" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>
                      </div>
                      <small>Documentary</small>
                      <div class="progress mb-3" style="height: 5px">
                        <div class="progress-bar bg-primary" role="progressbar" style="width: 55%" aria-valuenow="55" aria-valuemin="0" aria-valuemax="100"></div>
                      </div>
                      <small>War</small>
                      <div class="progress mb-3" style="height: 5px">
                        <div class="progress-bar bg-primary" role="progressbar" style="width: 66%" aria-valuenow="66" aria-valuemin="0" aria-valuemax="100"></div>
                      </div>
                    </div>
                  </div>
                </div>
                
              </div>



            </div>
          </div>

        </div>
    </div>
                                
