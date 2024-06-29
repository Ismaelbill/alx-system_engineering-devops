# install a package

package { ['python3', python3-pip]:
  ensure => installed,
}


package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
