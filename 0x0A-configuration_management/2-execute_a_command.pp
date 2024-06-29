#  Execute a command
exec { 'kill the file killmenow':
  path    => '/',
  command => '/usr/bin/pkill killmenow',
}
