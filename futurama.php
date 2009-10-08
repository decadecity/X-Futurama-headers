<?php

class Futurama {
  public static function get_header()
  {
    $handle = @fopen(dirname(__FILE__).'/futurama.csv','rb');
    if (!$handle) {
      throw new Exception('Fatal error: Unable to open: '.dirname(__FILE__).'/futurama.csv');
    }
    $quote_list = array();
    while (($line = fgetcsv($handle)) !== False) {
      if (count($line) == 2) {
        $quote_list[] = $line;
      }
    }
    fclose($handle);
    $quote = $quote_list[array_rand($quote_list)];
    $quote[0] = 'X-'.strtr($quote[0],' ','-');
    return $quote;
  }
}

if ($argv[0] == str_ireplace(dirname(__FILE__).'/','',__FILE__)) {
  print_r(Futurama::get_header());
}
