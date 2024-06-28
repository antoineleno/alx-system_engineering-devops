# Define the SSH client configuration file for global settings
file { '/etc/ssh/ssh_config':
  ensure  => present,
  mode    => '0644',
  content => "
    # Global SSH client configuration
    Host *
        PasswordAuthentication no
  ",
}

# Define the SSH client configuration file for user-specific settings (root user)
file { '/root/.ssh/config':
  ensure  => present,
  mode    => '0600',
  content => template('module_name/ssh_config.erb'),
}

# Define the template for user-specific SSH client configuration
file { 'module_name/ssh_config.erb':
  ensure  => present,
  mode    => '0644',
  content => "
    # User-specific SSH client configuration
    Host your_server_hostname
        IdentityFile ~/.ssh/school
  ",
}
