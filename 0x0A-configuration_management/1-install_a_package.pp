# Ensure pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/bin', '/usr/bin'],
  require => Package['python3-pip'],
  unless  => '/usr/bin/pip3 show flask | grep "Version: 2.1.0"',
}
