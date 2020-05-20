<!DOCTYPE html>
<html>
<head>
<style>
table {
    width: 100%;
    border-collapse: collapse;
}

table, td, th {
    border: 1px solid black;
    padding: 5px;
}

th {text-align: left;}
</style>
</head>
<body>

<?php
$servername = "localhost";
$username = "root";
$password = "aventador";
$dbname = "product_data";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT shop_id,shop_product_name,amazon_product_price,shopclues_product_price,snapdeal_product_price,flipkart_product_price FROM `price_details` ";
$result = $conn->query($sql);
echo "<table>
<tr>
<th>shop_id</th>
<th>shop_product_name</th>
<th>amazon_product_price</th>
<th>shopclues_product_price</th>
<th>snapdeal_product_price</th>
<th>flipkart_product_price</th>
</tr>";

if ($result->num_rows > 0) {
    // output data of each row
    while($row = mysqli_fetch_array($result)) {
    echo "<tr>";
    echo "<td>" . $row['shop_id'] . "</td>";
    echo "<td>" . $row['shop_product_name'] . "</td>";
    echo "<td>" . $row['amazon_product_price'] . "</td>";
    echo "<td>" . $row['shopclues_product_price'] . "</td>";
    echo "<td>" . $row['snapdeal_product_price'] . "</td>";
    echo "<td>" . $row['flipkart_product_price'] . "</td>";
  echo "</tr>";
}
}
echo "</table>";
mysqli_close($con);
?>
</body>
</html>
