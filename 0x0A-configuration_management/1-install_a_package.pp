#Manifest in Puppet to install puppet-lint

exec { 'apt-get update':
  command => '/usr/bin/apt-get update'
}

package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem',
  require  => Exec['apt-get update']
}
