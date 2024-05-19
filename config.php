<?php
    extract($_REQUEST);
    $file=fopen("data-save.txt","w");

    fwrite($file,"");
    fwrite($file, $username ."\n");
    fwrite($file,"");
    fwrite($file, $email ."\n");
    fclose($file);
    header("location: n.html");
 ?>
