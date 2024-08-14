# 0-strace_is_your_friend.pp

# Ensure Apache is installed
package { 'apache2':
  ensure => installed,
}

# Ensure the necessary directories have correct permissions
file { '/var/www/html':
  ensure  => directory,
  mode    => '0755',
  owner   => 'www-data',
  group   => 'www-data',
}

# Ensure the Apache configuration is correct (example for a specific file)
file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => file,
  source  => 'puppet:///modules/apache/000-default.conf',
  notify  => Service['apache2'], # Restart Apache if the config changes
}

# Ensure Apache service is running
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/apache2/sites-available/000-default.conf'], # Restart if config changes
}

