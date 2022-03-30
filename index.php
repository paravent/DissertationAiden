<?php
require_once "pdo.php";
require_once "functions.php";
session_start();
$usernameSession = $_SESSION["username"];
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Website!</title>
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
                            <?php
                            if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
                                echo <<< EOT
                                <li class="nav-item">
                                    <a class="nav-link colour-primary" href="profile.php">Profile</a>
                                </li>
                            EOT ; 
                            }
                            ?>
                            <li class="nav-item">
                            <?php
                            if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
                        
                                echo " <a class=\"nav-link colour-primary\"  </a> ";
                                echo htmlspecialchars($_SESSION["username"]);
                                echo " <a class=\"nav-link colour-primary\" href=\"logout.php\">Logout </a> ";
                                }
                                else {
                                    echo " <a class=\"nav-link colour-primary\" href=\"login.php\">Login </a> ";
                                }
                                ?>
                            </li>
                        </ul>
                    
                            <form class="form-inline" action="search.php" method="get" >
                                <input id="test" class="search-query"  type="text" name="test"  placeholder="Search" aria-label="Search" />
                                <script>
                                    var options = {
                                        url: "movies.json",
                                    

                                        getValue: "movieTitle",

                                        list: {
                                            maxNumberOfElements: 8,
                                            match: {
                                                enabled: true
                                            },
                                            sort: {
                                                enabled: true
                                            }
                                        },

                                        theme: "square"
                                    };

                                    $("#test").easyAutocomplete(options);

                                </script>
                                

                            </form>
                        </div>
                    </nav>
                    
                        
                        
                    <div class="jumbotron">
                    <?php 
                        if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
                            echo htmlspecialchars("Hey " . $_SESSION["username"] . "  If you want to update your liked genres, please submit this form :D");

                            echo <<< EOT
                            
                            <form method="post" action="">      
                                <fieldset>      
                                    <legend>Favourite Genres</legend>      
                                    <input type="checkbox" name="fav_genre[]" value="Action">Action<br>      
                                    <input type="checkbox" name="fav_genre[]" value="Music">Music<br>      
                                    <input type="checkbox" name="fav_genre[]" value="Romance">Romance<br> 
                                    <input type="checkbox" name="fav_genre[]" value="Family">Family<br>      
                                    <input type="checkbox" name="fav_genre[]" value="War">War<br>   
                                    <input type="checkbox" name="fav_genre[]" value="Crime">Crime<br>      
                                    <input type="checkbox" name="fav_genre[]" value="Adventure">Adventure<br>      
                                    <input type="checkbox" name="fav_genre[]" value="Fantasy">Fantasy<br> 
                                    <input type="checkbox" name="fav_genre[]" value="Animation">Animation<br>      
                                    <input type="checkbox" name="fav_genre[]" value="Drama">Drama<br> 
                                    <input type="checkbox" name="fav_genre[]" value="Horror">Horror<br>      
                                    <input type="checkbox" name="fav_genre[]" value="Comedy">Comedy<br>      
                                    <input type="checkbox" name="fav_genre[]" value="Thriller">Thriller<br>     
                                    <br>      
                                    <input type="submit" name="genQuery" value="Submit now" />      
                                </fieldset>      
                            </form>
                            EOT; 
                        }
                    
                        else {
                            echo <<< EOT
                            <h1>Your movie recommender system!</h1>
                                <p class="lead">Just hit the button below, make an account and get started!</p>
                                <p><a class="btn btn-lg btn-success" href="login.php" role="button"">Lets go!</a></p>
                            EOT;
                            
                        }
                        if(!empty($_POST['fav_genre'])) {
                            $space = " "; 
                            // SELECT userEmail FROM users WHERE userUsername LIKE '%$user%' LIMIT 1
                             
                            $findID = $pdo->prepare("SELECT userID FROM users WHERE  userUsername LIKE '%$usernameSession%'"); 
                            $findID->execute(); 
                            $myID = $findID->fetch(PDO::FETCH_ASSOC) ;
                            $myIDString = implode($space , $myID); 
                            $toString = implode( $space, $_POST['fav_genre']) ; 
                            
                            $stmt = $pdo->prepare("UPDATE `users` SET `userTrendGenre` = '$toString' WHERE `users`.`userID` = '$myIDString'"); 
                            
                            $stmt->execute(); 
                            // if($stmt->execute()){
                            //     $command = ("python3 api_call.py '%$$usernameSession%' "); 
                            //     exec($command);

                            //     $command_test = escapeshellcmd("python3 api_call.py '%$$usernameSession%' ");
                            //     $output = shell_exec($command_test);

                            //     echo $output; 
                            // }
                            
                  
                        }           
                    ?>
                    </div>
                    
                </div>
                
            </div>



            <footer class="footer bg-black small text-center text-white-50">
                <div class="container">

                    <div class="social d-flex justify-content-center">
                        <a class="mx-2" href="#!"><i class="fab fa-twitter fa-2x colour-primary"></i></a>
                        <a class="mx-2" href="#!"><i class="fab fa-facebook-f fa-2x colour-primary"></i></a>
                        <a class="mx-2" href="#!"><i class="fab fa-instagram fa-2x colour-primary"></i></a>
                        <a class="mx-2" href="#!"><i class="fab fa-pinterest fa-2x colour-primary"></i></a>
                    </div>
                            <div class="footer-options row justify-content-md-center">
                            <div class="col-sm-2">
                                Home
                            </div>
                            <div class="col-sm-2">
                                Wishlist
                            </div>
                            <div class="col-sm-2">
                                Profile
                            </div>
                            <div class="col-sm-2">
                                Login
                            </div>
                            </div>
                    </div>
                    <p>Website by Aiden Fairclough</p>
                </div>
            </footer>

        </body>
    </div>
</html>