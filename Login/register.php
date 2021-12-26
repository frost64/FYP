<?php

require_once "connect.php";
 
$username = $password = $confirm_password = $city = "";
$username_err = $password_err = $confirm_password_err = $city_err = "";
 
if($_SERVER["REQUEST_METHOD"] == "POST"){
 
    if(empty(trim($_POST["username"]))){
        $username_err = "Please enter a username.";
    } elseif(!preg_match('/^[a-zA-Z0-9_]+$/', trim($_POST["username"]))){
        $username_err = "Username can only contain letters, numbers, and underscores.";
    } else{
        $sql = "SELECT id FROM users WHERE username = ?";
        if($stmt = mysqli_prepare($link, $sql)){
            mysqli_stmt_bind_param($stmt, "s", $param_username);
            $param_username = trim($_POST["username"]);
            if(mysqli_stmt_execute($stmt)){
                mysqli_stmt_store_result($stmt);
                
                if(mysqli_stmt_num_rows($stmt) == 1){
                    $username_err = "This username is already taken.";
                } else{
                    $username = trim($_POST["username"]);
                }
            } else{
                echo "Something went wrong. Try again.";
            }
            mysqli_stmt_close($stmt);
        }
    }

    if(empty(trim($_POST["city"]))){
        $city_err = "Please enter a valid city.";     
    } else{
        $city = trim($_POST["city"]);
        if(empty($city) ){
            $city_err = "City is invalid.";
        }
    }

    if(empty(trim($_POST["password"]))){
        $password_err = "Enter password.";     
    } elseif(strlen(trim($_POST["password"])) < 6){
        $password_err = "Password must have more than 6 characters.";
    } else{
        $password = trim($_POST["password"]);
    }
    
    if(empty(trim($_POST["confirm_password"]))){
        $confirm_password_err = "Please confirm password.";     
    } else{
        $confirm_password = trim($_POST["confirm_password"]);
        if(empty($password_err) && ($password != $confirm_password)){
            $confirm_password_err = "Password did not match.";
        }
    }
    
    if(empty($username_err) && empty($password_err) && empty($confirm_password_err)){
        $sql = "INSERT INTO users (username, password) VALUES (?, ?)";
         
        if($stmt = mysqli_prepare($link, $sql)){
            mysqli_stmt_bind_param($stmt, "ss", $param_username, $param_password);

            $param_username = $username;
            $param_password = password_hash($password, PASSWORD_DEFAULT);
            
            if(mysqli_stmt_execute($stmt)){
                header("location: login.php");
            } else{
                echo "Something went wrong. Try again.";
            }
            mysqli_stmt_close($stmt);
        }
    }
    mysqli_close($link);
}

setcookie("city", $city);
?>
 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sign Up</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://use.fontawesome.com/releases/v5.7.2/css/all.css"></script>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="wrapper">
        <div class="logo"> <img src="https://www.freepnglogos.com/uploads/apex-legends-logo-png/apex-legends-transparent-picture-20.png" alt=""> </div>
        <div class="text-center mt-4 name"> Analyzer </div>

        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
            <div class="form-field d-flex align-items-center">
                <input type="text" name="username" id="username" placeholder="Username" <?php echo (!empty($username_err)) ? 'is-invalid' : ''; ?>" value="<?php echo $username; ?>">
                <span class="invalid-feedback"><?php echo $username_err; ?></span>
            </div>
            
            <div class="form-field d-flex align-items-center">
                <input type="text" name="city" id="city" placeholder="City" >
                <span class="invalid-feedback"><</span>
            </div>
            
            <div class="form-field d-flex align-items-center">
                <input type="password" name="password" id="pwd" placeholder="Password" <?php echo (!empty($password_err)) ? 'is-invalid' : ''; ?>" value="<?php echo $password; ?>">
                <span class="invalid-feedback"><?php echo $password_err; ?></span>
            </div>
            <div class="form-field d-flex align-items-center">
                <input type="password" name="confirm_password" placeholder="Confirm Password" <?php echo (!empty($confirm_password_err)) ? 'is-invalid' : ''; ?>" value="<?php echo $confirm_password; ?>">
                <span class="invalid-feedback"><?php echo $confirm_password_err; ?></span>
            </div>
                <button class="btn mt-3">Submit</button>
        </form>
        <div class="text-center fs-6"> <p>Already have an account? <a href="login.php">Login</a> here.</p></div>
    </div>    
</body>
</html>