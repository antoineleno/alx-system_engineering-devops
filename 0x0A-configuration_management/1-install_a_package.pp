# Install falsk version 2.1.0 using pip3
package { 'flask': # Antoine
  ensure   => '2.1.0', #Antoine
  provider => 'pip3', # Antoine
}
