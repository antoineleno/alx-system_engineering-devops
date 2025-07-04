# Puppet manifest to add custom HTTP header

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

file { '/etc/nginx/templates/default.erb':
  ensure  => file,
  content => epp('nginx/default.erb.epp'),
}

service { 'nginx':
  ensure => running,
  enable => true,
}

augeas { 'add custom header':
  context => '/files/etc/nginx/sites-available/default/server',
  changes => [
    "set add_header 'X-Served-By $hostname;'"
  ],
  notify  => Service['nginx'],
}
