<?php
session_start();

if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
    header("location: login.php");
    exit;
}
?>
 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Main Page</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body{ font: 14px sans-serif; text-align: center; }
    </style>
</head>
<body>
    <div class=btn mt-3 style="margin-left:90%;">
        <a href="logout.php" class="btn btn-danger ml-3">Logout!</a>
    </div>

    <h1 class="my-5">Hello <?php echo $_SESSION["username"]; ?>, Welcome to Main Page.</h1>
    <h2> 
        Your city is <?php echo $_COOKIE['city']; ?>
    </h2>

</body>
</html>