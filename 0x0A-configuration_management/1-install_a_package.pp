#Manifest in Puppet to install puppet-lint

exec { 'remove puppet-lint':
  command => 'sudo apt remove puppet-lint'
}

package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem',
  require  => Exec['remove puppet-lint']
}
