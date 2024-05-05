<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $Vsisse = $_POST["Vsisse"];
    $Vvalja = $_POST["Vvalja"];
    
    // Create a string with form data
    $data = "$Vsisse\n$Vvalja\n";
    
    // Set file path
    $file_path = "form_data.txt";
    
    // Open or create the file
    $file = fopen($file_path, "w") or die("Unable to open file!");
    
    // Write form data to the file
    fwrite($file, $data);
    
    // Close the file
    fclose($file);
    
    echo "Form data saved successfully!";
} else {
    echo "Form submission method not supported.";
}
?>
