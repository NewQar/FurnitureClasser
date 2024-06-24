<?php
	if($_SERVER["REQUEST_METHOD"] == "POST"){
		$server = "localhost";
		$user = "root";
		$pw = "";
		$db = "esdb";
		
		$conn = new mysqli($server,$user,$pw,$db);
		
		$firstName = $_POST["FirstName"];
		$lastName = $_POST["LastName"];
		$username = $_POST["Username"];
		$password = $_POST["Password"];
		$email = $_POST["Email"];
		
		$sql = "INSERT INTO user (fname,lname,uname,pw,email) VALUES ('$firstName', '$lastName','$username','$password','$email')";
		
		if(mysqli_query($conn, $sql)) {
			echo"<script>
			alert('Register successfull');
			window.location.href='MainPage.html';  
			</script>";
		} else {
			echo "<script>alert('Register unsuccessfull');";
		}
		mysqli_close($conn);
	}
?>