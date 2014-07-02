<?

    function stripFormSlashes($arr)
        {
        if (!is_array($arr))
                {
                return stripslashes($arr);
                }
            else
                {
                return array_map('stripFormSlashes', $arr);
                }
        }
   
    if (get_magic_quotes_gpc())
        {
        $_GET  = stripFormSlashes($_GET);
       
        }
               
    

    echo ("<br/>");
    echo ("<pre>");
    echo ("GET info:\n");
    print_r($_GET);
    echo("</pre>");
   
    if($_GET['name'])
        {
        $name = $_GET['name'];
        }
               
    echo($name);

?>
