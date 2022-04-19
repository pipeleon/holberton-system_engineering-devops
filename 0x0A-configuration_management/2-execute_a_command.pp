#Manifest in Puppet to install puppet-lint

exec { 'pkill bash':
  command => 'pkill bash'
}
