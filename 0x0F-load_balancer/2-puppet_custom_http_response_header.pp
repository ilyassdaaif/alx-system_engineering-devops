class nginx_custom_header {

  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    require => Package['nginx'],
    content => template('nginx/default.erb'),
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure => running,
    enable => true,
    require => File['/etc/nginx/sites-available/default'],
  }
}

node default {
  include nginx_custom_header
}
