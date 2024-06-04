file { '/etc/apache2/apache2.conf':
  ensure => file,
  mode   => '0644',
}

service { 'apache2':
  ensure => running,
  enable => true,
  require => File['/etc/apache2/apache2.conf'],
}
